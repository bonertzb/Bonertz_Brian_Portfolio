# DSC 510
# Week 12
# 12.1 Final Project Week 12
# Author Brian Bonertz
# 03/03/2023

import requests
import json


def zip_function(zip_code, uom):
    #  URL to get the lon / lat information by searching zip code. I tried using a try block here, but couldn't get it to work
    #  So after watching your week 10 video, you said we can use if statements as well. This seemed to work better
    zip_url_build = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip_code + ",US&units=" + uom + "&appid=4610b97842296466830700b9ced3e895"

    response = requests.request("GET", zip_url_build)

    if response.status_code != 200:
        print("\nThere was an error in the request.")
        print("You entered", zip_code)
        print("Please try again\n")
        main()
    else:
        message = response.text
        data = json.loads(message)
        coordinates = data['coord']
        longitude = str(coordinates['lon'])
        latitude = str(coordinates['lat'])
        lon_lat_uom = str(uom)
        lon_lat(longitude, latitude, lon_lat_uom)


def city_state(city, state, uom):
    #  URL to get the lon / lat information by searching city and state. I tried using a try block here, but couldn't get it to work
    #  So after watching your week 10 video, you said we can use if statements as well. This seemed to work better
    url_build = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + state + ",US&units=" + uom + "&appid=4610b97842296466830700b9ced3e895"
    url = url_build
    response = requests.request("GET", url)
    if response.status_code != 200:
        print("\nThere was an error in the request.")
        print("You entered", city, state.upper())
        print("Please try again\n")
        main()
    else:
        message = response.text
        data = json.loads(message)
        coordinates = data["coord"]
        longitude = str(coordinates['lon'])
        latitude = str(coordinates['lat'])
        lon_lat_uom = str(uom)
        lon_lat(longitude, latitude, lon_lat_uom)


def lon_lat(longitude, latitude, lon_lat_uom):  # this function uses the Lon / lat data from the previous look-up to fetch the weather data.

    coord_urlbuild = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid=4610b97842296466830700b9ced3e895&units=" + lon_lat_uom
    coord_url = coord_urlbuild
    coord_response = requests.request("GET", coord_url)
    coord_message = coord_response.text
    coord_data = json.loads(coord_message)
    weather = coord_data['main']  # pulls the weather information from the main dic
    city_name = coord_data['name']  # pulls the city name from the URL
    descrip = coord_data['weather']  # pulls the description from the URL
    city_id(city_name)
    weather_info(weather, descrip)


def city_id(city_name):  # function to retrieve and present the city name from the URL data
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("\nCurrent Weather Conditions for", city_name, ":")
    print("")


def weather_info(weather, descrip):  # Function to present the weather information.
    # I was going to use a "for" loop to present the key and values, but i didn't like the way the keys were formatted.
    cur_temp = str(weather['temp'])
    feel_temp = str(weather['feels_like'])
    high_temp = str(weather['temp_max'])
    low_temp = str(weather['temp_min'])
    press = str(weather['pressure'])
    humid = weather['humidity']
    des = str(descrip[0])
    print("Current Temp:", cur_temp, "Degrees")  # used to parse the weather information from the "main" dictionary
    print("Temp Feels Like:", feel_temp, "Degrees")
    print("Today's High is:", high_temp, "Degrees")
    print("Today's Low is:", low_temp, "Degrees")
    print("Pressure:", press, "hPa")
    print("Humidity:", humid, "%")
    atpos = des.find("'description': ")  # used the string parsing method in the book to pull the description
    sppos = des.find(",", atpos)
    host = des[atpos+1:sppos]
    print(host)

    print("")
    end_program()


def end_program():  # function to end the program. Probably not necessary.
    retry = str(input("Would you like to view weather information for another location?  Y or N  "))
    retrycap = retry.upper()
    if retrycap == "N":
        print("\nThanks for using my program!")
    elif retrycap == "Y":
        print("+++++++++++++++++++++++++++++++++++++")
        print('\n')
        main()
    else:
        print("You entered: ", retry)
        print("This is not a valid response. Please try again")
        end_program()


print("Hello and welcome!")


def main():  # main asks the user how they would like to search their weather information, and also asks for the unit of measure.

    loop = True
    while loop:  # While loop helps to validate the data and catches user data entry errors.
        print("How would you like to search weather information?")
        city_zip_entry = str(input("Please enter '1' to search by City and State, or '2' to search by Zip Code:  "))

        if city_zip_entry == "1":  # user input for city name and state
            city_entry = str(input("Please enter the city name:  "))
            city_cap = city_entry.title()  # User input is capitalized
            state_entry = str(input("Please enter the state abbreviation:  "))
            state_lower = state_entry.lower()  # state code is dropped to a lower case for the URL
            city = city_cap
            state = state_lower
            loop = True
            while loop:  # While loop to validate the data for the Unit of Measure look-up
                print("Would you like to view temps in Fahrenheit, Celsius, or Kalvin?")
                uom_input = str(input("Please enter 'F' for Fahrenheit, 'C' for Celsius, or 'K' for Kalvin:  "))
                uom_cap = uom_input.upper()  # User input is capitalized to avoid error and have consistent data
                if uom_cap == "F":
                    uom = "imperial"
                    loop = False
                elif uom_cap == "C":
                    uom = "metric"
                    loop = False
                elif uom_cap == "K":
                    uom = ""
                    loop = False
                else:
                    print("You entered", uom_input)
                    print("This is not a valid response. Please try again. \n")
            city_state(city, state, uom)
        elif city_zip_entry == "2":  # User input for zip_code
            zip_entry = str(input("Please enter the Zip Code:  "))
            zip_code = str(zip_entry)
            loop = True
            while loop:  # While loop to validate the data for the Unit of Measure look-up
                print("Would you like to view temps in Fahrenheit, Celsius, or Kalvin?")
                uom_input = str(input("Please enter 'F' for Fahrenheit, 'C' for Celsius, or 'K' for Kalvin:  "))
                uom_cap = uom_input.upper()  # User input is capitalized to avoid error and have consistent data
                if uom_cap == "F":
                    uom = "imperial"
                    loop = False
                elif uom_cap == "C":
                    uom = "metric"
                    loop = False
                elif uom_cap == "K":
                    uom = ""
                    loop = False
                else:
                    print("You entered", uom_input)
                    print("This is not a valid response. Please try again. \n")
            zip_function(zip_code, uom)
        else:
            print("You entered", city_zip_entry)
            print("This is not a valid response. Please try again")


if __name__ == "__main__":
    main()
