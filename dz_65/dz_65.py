import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
