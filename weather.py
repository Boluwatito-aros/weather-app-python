import requests

API_KEY = "YOUR_API_KEY_HERE"  # Remove your real key before uploading to GitHub


def current_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        r = requests.get(url)
        r.raise_for_status()  # Catches HTTP errors (e.g. 404, 401)
        w_info = r.json()
        temp = w_info["main"]["temp"]
        description = w_info["weather"][0]["description"]
        humidity = w_info["main"]["humidity"]
        wind_speed = w_info["wind"]["speed"]
        return (
            f"Temperature:   {temp - 273.15:.2f}°C\n"
            f"Description:   {description}\n"
            f"Humidity:      {humidity}%\n"
            f"Wind Speed:    {wind_speed * 3.6:.1f} km/h"
        )
    except Exception:
        return "City not found. Please check the city name and try again."


def five_day_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        f_info = r.json()
        days = 0
        for day_forecast in f_info["list"]:
            if "12:00:00" in day_forecast["dt_txt"]:
                date = day_forecast["dt_txt"][:10]
                temp = day_forecast["main"]["temp"] - 273.15
                description = day_forecast["weather"][0]["description"]
                humidity = day_forecast["main"]["humidity"]       
                wind_speed = day_forecast["wind"]["speed"] * 3.6  
                print(
                    f"{date}: {temp:.2f}°C, {description}, "
                    f"Humidity: {humidity}%, Wind: {wind_speed:.1f} km/h"
                )
                days += 1
                if days == 5:
                    break
    except Exception:
        print("City not found. Please check the city name and try again.")


def main():
    print("Welcome to the Weather Forecast Application!")
    print()
    while True:  # Loop so user can check multiple cities without restarting
        print("Choose an option:")
        print("  1. Get current weather conditions")
        print("  2. Get 5-day forecast")
        print("  3. Exit")
        print()
        option = input("Enter your choice (1/2/3): ").strip()
        print()
        if option == "1":
            city = input("Enter the city name: ").strip()
            print(f"\nCurrent Weather in {city}:")
            print(current_weather(city))
        elif option == "2":
            city = input("Enter the city name: ").strip()
            print(f"\n5-Day Forecast for {city}:")
            five_day_forecast(city)
        elif option == "3":
            print("Thank you for using the Weather Forecast Application!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
        print()


if __name__ == "__main__":
    main()









