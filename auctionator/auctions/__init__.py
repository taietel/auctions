from flask import Blueprint


class AuctionsBlueprint(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        self.add_url_rule('/users', view_func=self.get_users)

    def get_users(self):
        return {}
