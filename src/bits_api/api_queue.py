from bits_api.api_call import APICall
import random
from threading import Thread


class APIQueue():
    def __init__(self, max_threads: int = -1) -> None:
        """Initializes an APIQueue instance.
    
        Args:
            max_threads (int): The maximum number of threads to use for API requests. Default is -1 for no limit.
        """
        super().__init__()
        self.max_threads = max_threads
        self.responses = {}
        self.manager = self.thread_manager(self)
        self.manager.running = False

    async def request(self, top_level: str = '', specific: str = '', items_per_page: int = None, priority: bool = False) -> int:
        """
        Adds a request to the queue.
    
        Generates a random ID, adds the request to the priority queue or regular 
        queue based on the priority flag, and returns the ID.
    
        Args:
            top_level (str): The top level API endpoint for the request.
            specific (str): Filter for a specific result.
            items_per_page (int): Number of items per page for pagination.
            priority (bool): Whether this is a priority request.
    
        Returns:
            The generated random ID (int) for the request.
        """
        made_manager = False
        if not self.manager.running:
            made_manager = True
            self.manager = self.thread_manager(self)

        ID = random.randrange(1000, 9999)
        while ID in self.manager.queue or ID in self.manager.priority_queue or ID in self.responses or ID == self.manager.active or ID in self.manager.active_threads:
            ID = random.randrange(1000, 9999)

        if priority:
            self.manager.priority_queue[ID] = (
                top_level, specific, items_per_page)
        else:
            self.manager.queue[ID] = (top_level, specific, items_per_page)

        if made_manager:
            await self.manager.run()

        return ID

    def is_ready(self, ID: int) -> bool:
        """Checks if a request with the given ID has completed.
    
        Args:
            ID (int): The request ID to check.
            
        Returns:
            bool: True if the request has completed, False otherwise.
        """
        return ID in self.responses

    def read_response(self, ID: int) -> dict:
        """Reads the response for the given request ID.
    
        Checks if the ID exists in the responses dict, the active requests, 
        the priority queue, the regular queue, and returns the appropriate 
        response or error.
        
        Deletes response after response is read

        Args:
            ID (int): The request ID to get the response for.
        
        Returns:
            dict: The response data if found, or a status message if not.
        """
        if self.is_ready(ID):
            response = self.responses[ID]
            del self.responses[ID]
            return {"Status": "Done", "Result": response}
        elif ID == self.manager.active or ID in self.manager.active_threads:
            return {"Status": "Working"}
        elif ID in self.manager.priority_queue:
            return {"Status": "Queue", "Queue": "Priority", "Position": list(self.manager.priority_queue.keys()).index(ID)}
        elif ID in self.manager.queue:
            return {"Status": "Queue", "Queue": "Normal", "Position": list(self.manager.queue.keys()).index(ID)}
        else:
            return {"Status": "Error", "Error": "Not Found"}

    def stop(self):
        """Forces stop of processing queues
        """
        self.manager.running = False

    class thread_manager():
        def __init__(self, main):
            self.main = main
            self.max_threads = main.max_threads
            self.priority_queue = {}
            self.queue = {}
            self.active = None
            self.active_threads = {}
            self.running = True

        async def run(self):
            while self.running:
                if len(self.priority_queue) > 0 and (len(self.active_threads) < self.max_threads or self.max_threads in (-1, 0)):
                    request = list(self.priority_queue.keys())[0]
                    if self.max_threads == 0:
                        self.active = request
                        self.main.responses[request] = await APICall(*self.queue[request])
                        del self.queue[request]
                        self.active = None
                    else:
                        self.active_threads[request] = await self.download_thread(self, request, *self.priority_queue[request])
                        del self.priority_queue[request]

                elif len(self.queue) > 0:
                    request = list(self.queue.keys())[0]
                    self.active = request
                    self.main.responses[request] = await APICall(*self.queue[request])
                    del self.queue[request]
                    self.active = None

                if len(self.priority_queue) == 0 and len(self.active_threads) == 0 and len(self.queue) == 0:
                    self.running = False

        class download_thread(Thread):
            async def __init__(self, manager, threadID, top_level: str = '', specific: str = '', items_per_page: int = None):
                super().__init__()
                self.ID = threadID
                self.manager = manager
                self.result = None
                self.top = top_level
                self.specific = specific
                self.items = items_per_page
                await self.start()

            async def run(self):
                self.manager.main.responses[self.ID] = await APICall(self.top, self.specific, self.items)
                del self.manager.active_threads[self.ID]
