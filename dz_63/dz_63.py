import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}  # {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1  # {1: 2}
        except KeyError:
            todos_by_user[todo['userId']] = 1  # {1: 1, 2: 1, 3: 1}
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)  # [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]

max_complete = top_users[0][1]
print(max_complete)  # 12

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:  # 11 < 12
        break
    users.append(str(user))
print(users)  # ['5', '10']

max_users = " and ".join(users)
print(max_users)
print(f"Users {max_users} completed {max_complete} Todos")
# ====================
print('=' * 40)

users_int = list(map(int, users))
list_users = []
for todo in todos:
    if todo['completed'] and todo['userId'] in users_int:
        list_users.append(todo)

print(list_users)

with open('user.json', 'w') as f:
    json.dump(list_users, f, indent=2)
