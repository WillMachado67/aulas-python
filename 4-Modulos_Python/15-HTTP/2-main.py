import requests

# http:// -> porta 80
# https:// -> porta 443

url = 'http://localhost:3333/'
response = requests.get(url)

print(response)
# print(response.status_code)
# print(response.headers)
# print(response.content) # Retorna o HTML em bites
# print(response.text)  # Retorna o HTML real
