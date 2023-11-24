# import os
# import sys
# import django
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_leadHit.settings')
# django.setup()
#
# from test_api.views import post
#
# if __name__ == '__main__':
#     post()
import requests
def post_test():
    url = 'http://127.0.0.1:8000/api/get_form/'
    data = {'name': 'test', 'Number': '+79526886210'}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        user = response.json()
        print(user)
    else:
        print('Error:', response.status_code)

