import requests

# 建立url的資料。
url = "http://api.open-notify.org/iss-now.json"
# 建立response的變數，並運用requests的get方法，取得資料。
response = requests.get(url)
print(response.status_code) # <Response [200]>

# 可以這個方式是否status code為200。
response.raise_for_status()

# Method: 1
# if response.status_code == 404:
#     raise Exception(f"That status code is { 404 }")
# elif response.status_code == 401:
#     raise Exception(f"That status code is { 401 }")

# 把資料轉換成json。
data = response.json()
print(data)

# 找到對應的 iss_position
iss_position_data = response.json()['iss_position']
print(iss_position_data)

# 找到對應的 longitude 對應的值
longitude = response.json()['iss_position']["longitude"]
print(longitude)

# 找到對應的 latitude 對應的值
latitude = response.json()['iss_position']["latitude"]
print(latitude)

# 把longitude, latitude做成一個tuple。
iss_position = (longitude, latitude)
print(iss_position)