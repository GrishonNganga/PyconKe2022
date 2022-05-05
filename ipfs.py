import requests

def upload(file_name):
    headers = {
        'pinata_api_key': '7a1f59937cb69ffa86f9',
        'pinata_secret_api_key': 'f6bfbb866bbe665dbd325cf88c4c3436debfca419d6d9e81e0bf0e01f3509db1'
    }

    files = {
        'file': open("output/" + file_name, 'rb'),
    }

    response = requests.post('https://api.pinata.cloud./pinning/pinFileToIPFS', headers=headers, files=files)
    return response.json()