import requests

payload={
    'month':9,
    'day':28
}
# r=requests.get('https://httpbin.org/get',params=payload)
r=requests.post('https://httpbin.org/post',data=payload,timeout=3)

# with open('comic.png','wb') as f:
#     f.write(r.content)
# r.json()
print(r.text)