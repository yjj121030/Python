import requests
with requests.get("https://api.uomg.com/api/rand.music?sort=%E6%8A%96%E9%9F%B3%E6%A6%9C&format=json") as f:
    print(f.status_code,f.reason)
    
    pass