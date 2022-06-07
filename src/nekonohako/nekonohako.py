from lib.catbox import Catbox


class NekoNoHako:
    instances = {}

    @staticmethod
    def get(user_hash='') -> Catbox:
        if user_hash not in NekoNoHako.instances:
            config = {
                'user_hash': user_hash
            }
            NekoNoHako.instances[user_hash] = Catbox(config)

        return NekoNoHako.instances[user_hash]


nknh = NekoNoHako.get('b81569b19e1bbbd316c48fa97')
nknh.upload_url('https://i.imgur.com/4QSOBiJ.jpg')
