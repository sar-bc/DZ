import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
with open("json.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(todos[0].keys()))
    writer.writeheader()
    for w in todos:
        writer.writerow(w)
    print("Запись в файл выполнена.")




        
