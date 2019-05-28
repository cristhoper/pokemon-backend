import json
from threading import Lock
import requests
from flask import Flask
from flask_cors import CORS

# Lock to populate queue
populate_lock = Lock()
populate_lock.acquire()

# Queue implemented, simple array.
queue = []

# Implement Flask with CORS, to allow Cross-Origin
uapp = Flask(__name__)
cors = CORS(uapp)

# Get values for pokemon list.
pokedata = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=1", timeout=10)
data = pokedata.json()
# get max resource available
max_element = int(data['count'])

# Run GET using amx limit
url = "https://pokeapi.co/api/v2/pokemon/?limit={}".format(max_element)
pokedata = requests.get(url, timeout=10)
data = pokedata.json()

# populate queue
for pokemon in data['results']:
    p_id = str(pokemon['url']).split('/')[6]
    queue.append({'id': p_id, 'name': pokemon['name']})
offset = 0

# Unlock queue, allowing connections.
populate_lock.release()


@uapp.route('/pokeapi/')
def pokeapi():
    """
    Endpoint to get 18 elements, moving inside queue one by one.
    """

    # Populate small array, to return just 18 elements.
    poke_array = []
    # Check if populate is locked
    if populate_lock.locked():
        for i in range(18):
            poke_array.append({
                'id': '-',
                'name': 'waiting for a pokemon'
            })
        # return dummy list with info about API
        return json.dumps(poke_array)

    global offset, max_element
    # populate array with pokemon info.
    for i in range(18):
        # Boundary condition. Run circular.
        current_index = (i + offset) % max_element
        poke_array.append({
            'id': queue[current_index]['id'],
            'name': queue[current_index]['name']
        })
    # Set boundary condition, to avoid endless increment.
    offset = offset + 1 if offset + 1 < max_element else 0

    # return JSON object service.
    return json.dumps(poke_array)


if __name__ == '__main__':
    uapp.run(debug=True, port=5081)
