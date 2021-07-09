import requests

url = 'http://localhost:5000/predict'
req = requests.post(url,json={'petrolTax':9, 'averageIncome':3571, 'pavedHighway':1976, 'popDriverLicense': .525})
print(req.json())

