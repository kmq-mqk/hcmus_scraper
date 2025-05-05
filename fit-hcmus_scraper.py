import requests
import json

# Call API to get target JSON
originUrl = "https://www.fit.hcmus.edu.vn/"
EndpointUrl = "https://www.fit.hcmus.edu.vn/vn/Default.aspx?tabid=57"
boundary = "----"

headers = {
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    "Origin": "https://www.fit.hcmus.edu.vn",
    "Referer": "https://www.fit.hcmus.edu.vn/vn/Default.aspx?tabid=57",
    "User-Agent": "Mozilla/5.0 Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "X-OFFICIAL-REQUEST": "TRUE",
}

payload = (
    f"--{boundary}\r\n"
    'Content-Disposition: form-data; name="action"\r\n\r\n'
    "getPosts\r\n"
    f"--{boundary}\r\n"
    'Content-Disposition: form-data; name="data"\r\n\r\n'
    '{"CategoryId":1,"PageSize":20,"PageIndex":1,"Keyword":""}\r\n'
    f"--{boundary}--\r\n"
)

response = requests.post(EndpointUrl, headers=headers, data=payload.encode())

# Get needed data
fout = open('fit-hcmus.txt', 'w')

json_re = response.json()
for post in json_re["Results"]["Posts"]:
  PostUrl = originUrl + post['PostDetailsUrl']
  fout.write(f"{post['LastUpdate']} _ [ {post['PostTitle']} ]\r\n{PostUrl}\r\n\r\n")