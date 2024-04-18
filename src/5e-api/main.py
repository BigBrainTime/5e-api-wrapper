import requests
import warnings
import json
import random
from threading import Thread
from time import sleep, time

api = 'https://www.dnd5eapi.co/api/'

class APICall():
    def __init__(self, top_level: str = '', specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes APICall with top level and specific endpoints.
    
        Parameters:
        - top_level (str): Top level endpoint, empty string for base API url 
        - specific (str): Specific endpoint 
        - items_per_page (int): Number of items per page for pagination
        
        Sets attributes:
        - response: API response 
        - status: response status code
        - data: JSON response data
        - pages: paginated results 
        - results: API results
        - count: number of results
        
        Handles API errors and pagination.
        """
        if top_level == '':
            self.response = requests.get(f'{api}')
        else:
            self.response = requests.get(f'{api}/{top_level}/{specific}')
        self.status = self.response.status_code
        self.data = json.loads(self.response.text)

        self.pages = []

        if self.status not in (200,404):
            self.results = []
            self.count = 0
            warnings.warn('Invalid response from API')
        
        elif self.status == 404:
            self.results = self.data
            self.count = 0

        elif top_level == '':
            self.count = len(self.data)
            self.results = self.data
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]

        elif specific == '':
            self.count = self.data['count']
            self.results = self.data['results']
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]

        else:
            self.count = 1
            self.results = self.data
            if itemes_per_page is not None:
                self.paginate_results(len(self.results))
            else:
                self.pages = self.results if isinstance(self.results, list) else [self.results]


    def paginate_results(self, items_per_page: int):
        """Paginates the results into pages of items_per_page items each.
    
        Iterates through the results and appends pages of items_per_page items to 
        the self.pages list. Any remaining items are added as a final partial page.
        """
        self.pages=[]
        new_page = []
        for page in self.results:
            if len(new_page) >= items_per_page:
                self.pages.append(new_page)
                new_page = []

            new_page.append(page)

        if len(new_page) > 0:
            self.pages.append(new_page)

    def __str__(self) -> str:
        data = {
            "status":self.status,
            "count":self.count,
            "results":self.results
        }
        return json.dumps(data)
    

class AbilityScores(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an AbilityScores API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('ability-scores', specific, itemes_per_page)


class Alignments(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an Alignments API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('alignments', specific, itemes_per_page)


class Backgrounds(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Backgrounds API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('backgrounds', specific, itemes_per_page)


class Classes(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Classes API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('classes', specific, itemes_per_page)


class Conditions(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Conditions API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('conditions', specific, itemes_per_page)


class DamageTypes(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a DamageTypes API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('damage-types', specific, itemes_per_page)


class Equipment(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Equipment API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('equipment', specific, itemes_per_page)


class EquipmentCategories(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes an EquipmentCategories API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('equipment-categories', specific, itemes_per_page)


class Feats(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Feats API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('feats', specific, itemes_per_page)


class Features(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Features API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('features', specific, itemes_per_page)


class Languages(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Languages API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('languages', specific, itemes_per_page)


class MagicItems(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a MagicItems API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('magic-items', specific, itemes_per_page)


class MagicSchools(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a MagicSchools API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('magic-schools', specific, itemes_per_page)


class Monsters(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Monsters API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('monsters', specific, itemes_per_page)


class Proficiencies(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Proficiencies API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('proficiencies', specific, itemes_per_page)


class Races(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Races API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('races', specific, itemes_per_page)


class Rules(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Rules API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('rules', specific, itemes_per_page)


class Skills(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Skills API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('skills', specific, itemes_per_page)


class Spells(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Spells API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('spells', specific, itemes_per_page)


class Subclasses(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Subclasses API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('subclasses', specific, itemes_per_page)


class Subraces(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Subraces API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('subraces', specific, itemes_per_page)


class Traits(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a Traits API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('traits', specific, itemes_per_page)


class WeaponProperties(APICall):
    def __init__(self, specific: str = '', itemes_per_page: int = None) -> None:
        """Initializes a WeaponProperties API call.

        Args:
        specific (str): Optional filter to get a specific ability score by name.
        itemes_per_page (int): Optional number of items per page for pagination.
        """
        super().__init__('weapon-properties', specific, itemes_per_page)


class APIQueue():
    def __init__(self, max_threads:int=-1) -> None:
        """Initializes an APIQueue instance.
    
        Args:
            max_threads (int): The maximum number of threads to use for API requests. Default is -1 for no limit.
        """
        super().__init__()
        self.max_threads = max_threads
        self.responses = {}
        self.manager = self.thread_manager(self)
        self.manager.running = False
        
    def request(self, top_level: str = '', specific: str = '', items_per_page: int = None, priority: bool = False) -> int:
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

        ID = random.randrange(1000,9999)
        while ID in self.manager.queue or ID in self.manager.priority_queue or ID in self.responses or ID == self.manager.active or ID in self.manager.active_threads:
            ID = random.randrange(1000, 9999)

        if priority:
            self.manager.priority_queue[ID] = (top_level, specific, items_per_page)
        else:
            self.manager.queue[ID] = (top_level, specific, items_per_page)

        if made_manager:
            self.manager.start()

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
            return {"Status":"Done","Result":response}
        elif ID == self.manager.active or ID in self.manager.active_threads:
            return {"Status": "Working"}
        elif ID in self.manager.priority_queue:
            return {"Status": "Queue", "Queue": "Priority", "Position": list(self.manager.priority_queue.keys()).index(ID)}
        elif ID in self.manager.queue:
            return {"Status": "Queue", "Queue": "Normal", "Position": list(self.manager.queue.keys()).index(ID)}
        else:
            return {"Status":"Error","Error": "Not Found"}


    def stop(self):
        """Forces stop of processing queues
        """
        self.manager.running = False

    class thread_manager(Thread):
        def __init__(self, main):
            super().__init__()
            self.main = main
            self.max_threads = main.max_threads
            self.priority_queue = {}
            self.queue = {}
            self.active = None
            self.active_threads = {}
            self.running = True


        def run(self):
            while self.running:
                if len(self.priority_queue) > 0 and (len(self.active_threads) < self.max_threads or self.max_threads in (-1,0)):
                    request = list(self.priority_queue.keys())[0]
                    if self.max_threads == 0:
                        self.active = request
                        self.main.responses[request] = APICall(*self.queue[request])
                        del self.queue[request]
                        self.active = None
                    else:
                        self.active_threads[request]=self.download_thread(self, request, *self.priority_queue[request])
                        del self.priority_queue[request]

                elif len(self.queue) > 0:
                    request = list(self.queue.keys())[0]
                    self.active = request
                    self.main.responses[request] = APICall(*self.queue[request])
                    del self.queue[request]
                    self.active = None

                if len(self.priority_queue) == 0 and len(self.active_threads) == 0 and len(self.queue) == 0:
                    self.running = False


        class download_thread(Thread):
            def __init__(self, manager, threadID, top_level: str = '', specific: str = '', items_per_page: int = None):
                super().__init__()
                self.ID = threadID
                self.manager = manager
                self.result = None
                self.top = top_level
                self.specific = specific
                self.items = items_per_page
                self.start()


            def run(self):
                self.manager.main.responses[self.ID] = APICall(self.top,self.specific,self.items)
                del self.manager.active_threads[self.ID]


if __name__ == "__main__":
    API = APIQueue(120)
    open_requests = []
    start = int(time())
    for i in range(10):
        open_requests.append(API.request())
    for i in range(1000):
        open_requests.append(API.request(priority=True))

    values = {}
    finished = 0
    while len(open_requests) > 0:
        to_remove = []
        for ID in open_requests:
            response = API.read_response(ID)

            if response["Status"] == "Done":
                to_remove.append(ID)
                del response['Result']
                finished += 1

                values[ID] = {"Response": response, 'TIME':int(time())-start}
        
        for ID in to_remove:
            open_requests.remove(ID)

        print(finished, len(API.manager.active_threads))
        sleep(3)
    print(f"Took {int(time())-start} seconds")
    sleep(2)
    print("LAST CALL")
    last_call = API.request()
    while not API.is_ready(last_call):
        pass
    print(API.read_response(last_call))

    with open('timed_output.json','w') as file:
        file.write(json.dumps(values,indent=2))