# flask_6_api_management
Assignment #6 for HHA 504

# How to Set Up and Test Flask Endpoint

I created numerous endpoints, one for "home", one called "pets", and one called "feeling". 

## "Home" Endpoint

- Charcterized by "@app.route('/')"
- Returns and displays text that says "Welcome to my Flask Endpoint :)"

## "Pets" Endpoint

- Characterized by "app.route('/pets')
- Takes in information about number of pets and type of pet
- Returns and displays text that says "I have {number} {pet}!"
- In the URL, the format should be "https:// .... dev/pets?number=<insert number>&pet=<insert pet>"

## "Feeling" Endpoint

- Characterized by "app.route('/feeling')
- Takes in information about emotion
- Returns and displays text that says "Why are you feeling {emotion}?"
- In the URL, the format should be "https:// .... dev/feeling?emotion=<insert emotion>"
- Example:

![image](https://github.com/jesschannn/flask_6_api_management/assets/123782059/21ad426a-7fdc-4cbf-ad7e-92504ed3b288)

# Documentation of your API, especially focusing on the standard OpenAPI format

# Steps and observations on Azure API Management integration

1. Install Azure CLI with this code:
```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash```
2. Log in with this code:
```az login --use-device-code```
3. Install Azure Functions Core Tool with this code:
 ```sudo apt-get install azure-functions-core-tools-4```
4. Create Local Function Project folder with this code:
```func init```
5. 

# Any challenges encountered, solutions tried, and your conclusions

Azure Link: https://flask-slim.azurewebsites.net/api/feeling 
