import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)

result = requests.get(url)
print(str(result.status_code))
print(result.text)

assert 200 == result.status_code
print("Success")

result.encoding = 'utf-8'  # important !
check = result.json()
check_info = check.get("categories")
check_info_value = check.get("value")
print(check_info)
print(check_info_value)
