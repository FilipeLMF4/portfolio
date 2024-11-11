import requests


def add_email(fname, lname, mail):
    sheety_endpoint = "https://api.sheety.co/165a242f0a4568d9bcf7ccb27dacea11/flightDeals/users"

    params = {
        "user": {
            "firstName": fname,
            "lastName": lname,
            "email": mail,
        }
    }

    response = requests.post(url=sheety_endpoint, json=params)
    response.raise_for_status()
    if response.status_code == 200:
        print("\nYou're in the club!")
    else:
        print("\nSorry, something went wrong. Please try again.")
    pass


print("Welcome to Filipe's Flight Club.")
print("We find you the best flight deals and email you.")
first_name = input("Please enter your first name: \n")
last_name = input("Please enter your last name: \n")
email = input("Please enter your email: \n")

if email == input("Please type your email again: \n"):
    add_email(first_name, last_name, email)
else:
    print("Emails do not match! Please try again.")
