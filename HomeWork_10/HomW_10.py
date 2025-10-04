import json

# with open('weather_data.json', 'r', encoding='utf-8') as file:
#     cities = json.load(file)
#
# city_temps = {}
# for entry in cities['weather']:
#     city = entry['city']
#     temp = entry['temperature']
#
#     if city not in city_temps:
#         city_temps[city] = []
#     city_temps[city].append(temp)
# max_avg_temp = -1
# hottest_city = []
#
# for city, temps in city_temps.items():
#     avg_temp = sum(temps) / len(temps)
#     if avg_temp > max_avg_temp:
#         max_avg_temp = avg_temp
#         hottest_city = city
# print(f'Город с самой высокой средней температурой: {hottest_city}')
# print(f'Cредняя температура: {max_avg_temp:.2f}°C')



# with open('movies.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# result = []
# for movie in data['movies']:
#     if movie['year'] > 2015 and movie['rating'] > 7:
#         print(f'{movie["title"]} - {movie["director"]}, {movie["year"]}, {movie["rating"]}, {movie["genres"]} ')
#         result.append(movie)
#
# with open('filtered_movies.json', 'w', encoding='utf-8') as file:
#     json.dump(result, file, ensure_ascii=False, indent=4)


with open('sales.json', 'r', encoding='utf-8') as file:
    sales  = json.load(file)

quantity = {}
total = 0

for sale in sales['sales']:
    total += sale['total']
    product = sale['product']
    if product not in quantity:
        quantity[product] = 0
    quantity[product] += sale['quantity']

output = {'total': total, 'products': quantity}

with open('sales_report.json', 'w') as output_file:
    json.dump(output, output_file, indent=4)



