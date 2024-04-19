import json
import asyncio
from bits_api import APIQueue
from time import sleep, time

open_requests = []

API = APIQueue(120)
start = int(time())

async def populate_queue():
    for i in range(1):
        open_requests.append(await API.request())
    for i in range(1):
        open_requests.append(await API.request(priority=True))

asyncio.run(populate_queue())

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

            values[ID] = {"Response": response, 'TIME': int(time())-start}

    for ID in to_remove:
        open_requests.remove(ID)

    print(finished, len(API.manager.active_threads))

print(f"Took {int(time())-start} seconds")
sleep(2)
print("LAST CALL")
last_call = API.request()
while not API.is_ready(last_call):
    pass
print(API.read_response(last_call))

with open('timed_output.json', 'w') as file:
    file.write(json.dumps(values, indent=2))