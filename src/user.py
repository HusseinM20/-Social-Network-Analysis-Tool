from graph import Graph


class User(Graph): 
    def __init__(self):
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.friends = [] 
        self.interests = []
        self.posts = []

    def add_friend(self, friend_id):
        if friend_id not in self.friends:
            super().add_edge(self.user_id, friend_id)
            self.friends.append(friend_id)
            print(f"{friend_id} has been added to {self.user_id}'s friends list.")
        else:
            print(f"{friend_id} is already a friend of {self.user_id}.")   

    def remove_friend(self, friend_id):
        if friend_id in self.friends:
            super().remove_edge(self.user_id, friend_id)
            self.friends.remove(friend_id)
            print(f"{friend_id} has been removed from {self.user_id}'s friends list.")
        else:
            print(f"{friend_id} is not a friend of {self.user_id}.")

