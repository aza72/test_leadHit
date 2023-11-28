import requests
def run():
    url = 'http://127.0.0.1:8000/api/get_form/'
    data = [
        {'Number':'+79526886210', 'name':'text'},
        {'day':'21.09.2022', 'surname':'alekseev'}
    ]
    #big = '?name=21.05.2022&Number=+79526886210'
    for d in data:
        response = requests.post(url, data=d)
        #print(response)
        if response.status_code == 200:
            user = response.json()
            print(user)
        else:
            print('Error:', response.status_code)

