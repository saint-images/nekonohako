from core.catbox import Catbox


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
