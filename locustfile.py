from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(1, 2.5) #Simulated users wait 1-2.5 seconds after each task is executed
    
    def on_start(self):
        pass

    def on_stop(self):
        pass
    
    @task(1)
    def getPred(self):
        self.client.post("http://localhost:5000/predict", json={'petrolTax':9, 'averageIncome':3571, 'pavedHighway':1976, 'popDriverLicense': .525})