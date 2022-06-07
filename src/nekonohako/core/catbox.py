import requests
from .const import RequestParams, Methods


class Catbox:
    REQUEST_URL = 'https://catbox.moe/user/api.php'

    def __init__(self, config):
        self.user_hash = config['user_hash']

    @staticmethod
    def __request(params):
        result = requests.post(Catbox.REQUEST_URL, data=params)
        print(result.text)

    def upload_url(self, url):
        params = {
            RequestParams.REQUEST_TYPE: Methods.URL_UPLOAD,
            RequestParams.URL: url,
        }

        if self.user_hash != '':
            params[RequestParams.USER_HASH] = self.user_hash

        Catbox.__request(params)

    def upload_file(self, file_path):
        pass
