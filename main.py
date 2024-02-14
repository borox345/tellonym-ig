## TODO
## [-] Create function that will generate token for specify username and password
## [-] Words blacklist
## [-] Save all with datetime and more

from cgitb import text
import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
from image import generate_tell_image

load_dotenv()
tells_storage = dict()

class Main:

    def __init__(self):
        username = os.getenv('TELLONYM_USERNAME')
        password = os.getenv('TELLONYM_PASSWORD')
        TOKEN = os.getenv('TELLONYM_TOKEN')
        self.base_url = 'https://api.tellonym.me'
        self.login_url = self.base_url + '/tokens/create'
        self.get_tells_url = self.base_url + '/tells'
        self.auth = 'Bearer ' + TOKEN
        self.auth_header = {'Authorization': self.auth,
                            'user-agent': 'Tellonym/737 CFNetwork/1240.0.4 Darwin/20.6.0',
                            'tellonym-client': 'ios:2.81.1:737:14:iPhone10,6'}
        self.non_auth_header = {'tellonym-client': 'ios:2.81.6:764:15:iPhone10,6', 'User-Agent': 'Tellonym/764 CFNetwork/1312 Darwin/21.0.0'}


    def get_tells(self):
        r = requests.get("https://api.tellonym.me/tells?limit=25", headers=self.auth_header).json()


        for index, _ in enumerate(r['tells']):
            try:
                tell = r['tells'][index]['tell']
                if tell not in tells_storage:
                    tells_storage[tell] = tell
                    print('+ to list')
                    #tells.append(tell)
                    #generate_tell_image(tell, f'tell{index}')
                else:
                    print('already in storage')
                
            except Exception as e:
                continue

        return

if __name__ == "__main__":
    main = Main()
    main.get_tells()