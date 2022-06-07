import ntpath
import mimetypes
import requests
from .const import RequestParams, Methods


class Catbox:
    REQUEST_URL = 'https://catbox.moe/user/api.php'

    def __init__(self, config):
        self.user_hash = config['user_hash']

    def __prepare_params(self, params):
        if self.user_hash != '':
            params[RequestParams.USER_HASH] = self.user_hash

        return params

    @staticmethod
    def __read_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_name = ntpath.basename(file_path)
                file_type = mimetypes.guess_type(file_path)[0]
                return (file_name, file_content, file_type)
        except IOError:
            return None

    def upload_url(self, url):
        params = {
            RequestParams.REQUEST_TYPE: Methods.URL_UPLOAD,
            RequestParams.URL: url,
        }
        params = self.__prepare_params(params)

        result = requests.post(Catbox.REQUEST_URL, data=params)
        return result.text

    def upload_file(self, file_path):
        file_info = Catbox.__read_file(file_path)
        if file_info is None:
            return None

        params = {
            RequestParams.REQUEST_TYPE: Methods.FILE_UPLOAD,
        }
        params = self.__prepare_params(params)

        files = {
            RequestParams.FILE_TO_UPLOAD: file_info
        }

        result = requests.post(Catbox.REQUEST_URL, data=params, files=files)
        return result.text
