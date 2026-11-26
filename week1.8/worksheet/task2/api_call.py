
import httpx, random

base_url = "https://dummyjson.com/"

content = "products/search?q=apple"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)
print(random.choice([k for k in range(3,21,2)]))
