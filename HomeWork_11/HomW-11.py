import json

new_file = []
with open('books.json', 'r', encoding='utf-8') as file:
    app = json.load(file)

for book in app['data']['books']:
    print(f'{book["title"]} - {book["genres"]}')
    new_file.append({"title": book["title"],"genres": book["genres"]})

with open('books_output.json', 'w', encoding='utf-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)




with open('cities.json', 'r', encoding='utf-8') as file:
    wep = json.load(file)

result = []
for city in wep['data']['cities']:
    print(f'{city["name"]} - {city["country"]}')
    result.append({"name": city["name"],"country": city["country"]})

with open('cities_output.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)