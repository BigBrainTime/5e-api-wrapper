# Tutorial: Using the D&D 5E API Wrapper

The `main.py` file in `src/5e-api` provides a wrapper for easily accessing the [D&D 5E API](https://www.dnd5eapi.co/). Here is a tutorial on how to use it:

## Making API Calls

To make an API call, first import the wrapper:

```py
from main import APICall
```

Then initialize an APICall instance, passing the top level endpoint and any filters:

```py
ability_scores = APICall('ability-scores')
```

This will make a request to the `ability-scores` endpoint and store the response.

You can also pass a specific filter:

```py
strength = APICall('ability-scores', 'strength')
```

And control pagination:

```py
spells = APICall('spells', items_per_page=50)
```

The response data is stored in the `results` attribute:

```py
print(ability_scores.results)
```

## Using the Queue

For managing multiple requests, use the `APIQueue` class.

Initialize it:

```py
from main import APIQueue

API = APIQueue()
```

Add requests:

```py
request1 = API.request('classes')
request2 = API.request('spells', items_per_page=30)
```

Check if a request is done:

```py
if API.is_ready(request1):
   print(API.read_response(request1))
```

Prioritize requests:

```py
priority = API.request('monsters', priority=True)
```

To limit the number of priority requests in the queue, pass the max priority requests as max_priority when initializing APIQueue:

```py
API = APIQueue(max_threads=10)
```

This will limit the active priority requests to 10 request threads. Additional priority requests will be added to the priority queue.

Stop the queue:

```py
API.stop()
```
