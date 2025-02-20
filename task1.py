import requests
import matplotlib.pyplot as plt
import os

api_key = "API KEY HERE"
cities = ["Bhubaneswar", "Delhi", "Bangalore", "Hyderabad", "Kolkata"]
temperatures = []

for city in cities:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            temperatures.append(temp)
        else:
            print(f"Error fetching data for {city}: {data.get('message', 'Unknown error')}")
            temperatures.append(None)

    except Exception as e:
        print(f"Exception occurred while fetching data for {city}: {e}")
        temperatures.append(None)


if any(t is not None for t in temperatures):
    plt.figure(figsize=(8, 5))
    plt.bar(cities, temperatures, color='skyblue')
    plt.xlabel("Cities")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature in Different Cities in India")
    plt.ylim(min(filter(None, temperatures)) - 2, max(filter(None, temperatures)) + 2)  
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
else:
    print("No valid temperature data available to plot.")
