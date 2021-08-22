import requests, json

class Client:

    access_token = None 
    refresh_token = None 

    def __init__(self, email, password, licence_type):
        self.email = email
        self.password = password
        self.licence_type = licence_type

    def login(self):

        try:

            body = { "Email" : self.email, "Password" : self.password}

            headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8"}

            url = "https://www.37austen.com/api/login"

            response = requests.post(url, headers = headers, json = body)

            resp = response.json()
            
            self.access_token = resp['access_token']
            self.refresh_token = resp['refresh_token']

        except:

            return("Failed Login.")

    def token_refresh(self):

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.refresh_token}

        url = "https://www.37austen.com/api/refresh"

        response = requests.post(url, headers = headers)

        resp = response.json()

        self.access_token = resp['access_token']
       

    def future_movement(self, data):

        if not isinstance(data,dict):

            return({"Error":{"Type":"The submitted price data must be submitted as a dict."}})

        body = data

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.access_token}

        url = "https://www.37austen.com/api/" + f"{self.licence_type}" + "/futuremovement"

        response = requests.post(url, headers = headers, json = body)

        return(response.json())

    def future_movement_group(self, data):
    
        if not isinstance(self.data,dict):

            return({"Error":{"Type":"The submitted price data must be submitted as a dict."}})

        body = data

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.access_token}

        url = "https://www.37austen.com/api/" + f"{self.licence_type}" + "/futuremovement/group"

        response = requests.post(url, headers = headers, json = body)

        return(response.json())

    def future_movement_fx(self, data):
        
        if not isinstance(self.data,dict):

            return({"Error":{"Type":"The submitted price data must be submitted as a dict."}})

        body = data

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.access_token}

        url = "https://www.37austen.com/api/" + f"{self.licence_type}" + "/futuremovement/fx"

        response = requests.post(url, headers = headers, json = body)

        return(response.json())

    def future_movement_token(self, data):
        
        if not isinstance(self.data,dict):

            return({"Error":{"Type":"The submitted price data must be submitted as a dict."}})

        body = data

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.access_token}

        url = "https://www.37austen.com/api/" + f"{self.licence_type}" + "/futuremovement/token"

        response = requests.post(url, headers = headers, json = body)

        return(response.json())

    def correlation(self, data):
        
        if not isinstance(self.data,dict):

            return({"Error":{"Type":"The submitted price data must be submitted as a dict."}})

        body = data

        headers = {"Content-Type" : "application/json", "Accept" : "application/json; charset=UTF-8", "Authorization" : "Bearer " + self.access_token}

        url = "https://www.37austen.com/api/" + f"{self.licence_type}" + "/correlation"

        response = requests.post(url, headers = headers, json = body)

        return(response.json())
    
