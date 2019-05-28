# **Pokegym-backend**
This API allows to get a specific list of pokemons from [PokeAPI](https://pokeapi.co/)

### Endpoints:

**GET** `/pokeapi/`

Return: JSON array with a pokemon object with names and ids.

| Key  | Value |
| ---- | ----- |
| id   | String with pokemon id |
| name | String with pokemon name |

Example:

```json
[
  {"id": "4", "name": "charmander"},
  {"id": "5", "name": "charmeleon"},
  {"id": "6", "name": "charizard"},
  {"id": "7", "name": "squirtle"},
  {"id": "8", "name": "wartortle"},
  {"id": "9", "name": "blastoise"},
  {"id": "10", "name": "caterpie"},
  {"id": "11", "name": "metapod"},
  {"id": "12", "name": "butterfree"},
  {"id": "13", "name": "weedle"},
  {"id": "14", "name": "kakuna"},
  {"id": "15", "name": "beedrill"},
  {"id": "16", "name": "pidgey"},
  {"id": "17", "name": "pidgeotto"},
  {"id": "18", "name": "pidgeot"},
  {"id": "19", "name": "rattata"},
  {"id": "20", "name": "raticate"},
  {"id": "21", "name": "spearow"}
]
```


For every API request, the list moves one element of the list.
So for this example, the next API request will contain indexes from 5 to the 22, in case of ids are contiguous.

## Usage

### Installation
This API is implemented in python, so for this you need to have installed python
```bash
$ sudo apt install python
```

The requirements are in file `requirements.txt` so run
```bash
$ sudo apt install python-pip
$ pip install -r requirements.txt
```

### Execution
To execute the app, just run
```bash
$ python uapp.py <port>
```
If no port specified, the API is going to run on **port 5081**.