import requests

response = requests.post(
    f"http://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer sk-8Cc814XgZREaqCX9Xgh6a6hBJjRsZtiq5Z262bEXu7aEHwnL",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Lighthouse on a cliff overlooking the ocean",
        "output_format": "webp"
    },
)

if response.status_code == 200:
    with open("./ligthhouse.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
