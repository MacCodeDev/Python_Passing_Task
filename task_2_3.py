import requests
import threading

def fetch_universities(country, result_dict):
    response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    universities = [uni['name'] for uni in response.json()]
    result_dict[country] = universities

countries = ["Poland", "Germany", "France", "Spain", "Italy", "United Kingdom", "Netherlands", "Sweden", "Norway", "Denmark", "Finland", "Austria", "Belgium", "Greece", "Portugal"]
result_dict = {}

threads = []
for country in countries:
    thread = threading.Thread(target=fetch_universities, args=(country, result_dict))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(result_dict)