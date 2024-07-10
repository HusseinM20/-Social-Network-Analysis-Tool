from graph import Graph
class SocialNetwork(Graph):
    def __init__(self):
        super().__init__()
        self.users = {}
    
    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)
            print(f"{name} has been added to the social network.")
        else:
            print(f"{name} is already in the social network.")
