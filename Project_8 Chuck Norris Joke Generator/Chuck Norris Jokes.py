# DSC 510
# Week 10
# 10.1 Programming Assignment Week 10
# Author Brian Bonertz
# 02/13/2023



def main():
    import requests
    import json

    print("Hello and welcome!")

    loop1 = True
    while loop1:
        joke = input("Would you like to hear a Chuck Norris Joke? Y or N ")
        jokecap = joke.upper()
        if jokecap == "N":
            print("\nOK, Thanks for using my program!")
            loop1 = False
        elif jokecap == "Y":
            url = "https://api.chucknorris.io/jokes/random?category=science"
            response = requests.request("GET", url)
            message = response.text
            data = json.loads(message)
            print("===============")
            print(data['value'])
            loop1 = False
        else:
            print("You did not enter a valid response. Please try again.")

    loop2 = True
    while loop2:

        url = "https://api.chucknorris.io/jokes/random?category=science"

        response = requests.request("GET", url)

        message = response.text

        data = json.loads(message)

        newjoke = input('\nWould you like to hear another joke? Y or N ')
        newjokecap = newjoke.upper()

        if newjokecap == "N":
            print("\nOK, thanks for visiting!")
            loop2 = False
        elif newjokecap == "Y":
            print("===============")
            print(data['value'])
        else:
            print('\nYou did not enter a valid response. Please try again')


if __name__ == "__main__":
    main()
