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

    def remove_user(self, user_id):
        if user_id in self.users:
            self.remove_vertex(user_id)
            self.users.pop(user_id)
            print(f"User {user_id} has been removed from the social network.")
        else:
            print(f"User {user_id} is not in the social network.")

    def add_friendship(self, user1_id, user2_id):
        if user1_id in self.users and user2_id in self.users:
            self.add_edge(user1_id, user2_id)
            self.users[user1_id].add_friend(user2_id)
            self.users[user2_id].add_friend(user1_id)
            print(f"Friendship added between {user1_id} and {user2_id}.")
        else:
            print(f"Both users must exist in the network to form a friendship.")

          