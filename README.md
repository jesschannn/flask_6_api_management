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
5. Navigate to the "local.settings.json" file and edit the following file to have the following code:
```
{
      "IsEncrypted: false,
      "Values: {
         "FUNCTIONS_WORKER_RUNTIME": "python"
         "AzureWebJobsFeatureFlags: "EnableWorkerIndexing",
         "AzureWebJobsStorage: "UseDevelopmentStorage=true"
      }
}
```
6. Input code into function_app.py file. My code is shown below:
 ```
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="feeling"
def emotion_get(req: func.HttpRequest) -> func.HttpResponse:
    emotion = req.params.get("emotion")
    if not emotion:
       emotion = "nothing"
    if emotion:
       return func.HttpResponse(f'Why are you feeling {emotion}?')
```
7. Create a resource group with the following code:

``` az group create --name AzureFunctionsQuickstart-rg --location <insert location>```

8. Create a storage account with the following code:

``` az storage account create --name <name of storage account> --location <insert location> --resource-group <insert resource group name> --sku Standard_LRS ```

9. Create a function app with the following code:
    
```az functionapp create --resource-group <insert resource group name> -rg --consumption-plan-location <insert location> --runtime python --runtime-version 3.9 --functions-version 4 --name <name of function app> --os-type linux --storage account <name of storage account> ```

10. Deploy app with the following code:
    
```func azure functionapp publish flaskapp504```

11. A link should appear in the console after running the previous code

Azure Link: https://flask-slim.azurewebsites.net/api/feeling 

# Challenges and Conclusions

A challenge that I faced when completing this assignment was 
