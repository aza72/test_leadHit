import requests
def run():
    url = 'http://127.0.0.1:8000/api/get_form/'
    data = {'Number': '+79526886210','name': 'ghy'} #(({'name': '21.12.2014'}), '&',({ 'Number': '+79526886210'}))
    big = '?name=21.05.2022&Number=+79526886210'
    response = requests.post(url+big)
    print(response)
    if response.status_code == 200:
        user = response.json()
        print(user)
    else:
        print('Error:', response.status_code)

