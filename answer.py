import json
from csv import DictReader

# Сохранить список книг
books_list = []
with open("books.csv", "r") as file:
    reader = DictReader(file)

    for row in reader:
        books_list.append({
            "title": row["Title"],
            "author": row["Author"],
            "pages": row["Pages"],
            "genre": row["Genre"]
        })

# Сохранить список юзеров
users_list = []
with open("users.json", "r") as file:
    json_users = json.loads(file.read())
    for json_user in json_users:
        users_list.append(
            dict(name=json_user['name'], gender=json_user['gender'],
                 address=json_user['address'], age=json_user['age'],
                 books=[]))

# Раздаем книги юзерам
result = users_list
user_index = 0
while len(books_list) > 0:
    book = books_list[0]
    result[user_index]['books'].append(book)
    books_list.remove(book)
    if user_index != len(users_list) - 1:
        user_index += 1
    else:
        user_index = 0

with open('result.json', 'w') as file:
    file.write(json.dumps(result, indent=2))
