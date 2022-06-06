class nekonohako:

    REQUEST_URL = 'https://catbox.moe/user/api.php'

    def __init__(self, config):
        self.user_hash = config.user_hash

    def test(self):
        print(self.user_hash)
