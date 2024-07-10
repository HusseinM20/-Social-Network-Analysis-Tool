from graph import Graph


class User(Graph): 
    def __init__(self):
        super().__init__()
        self.user_id = user_id
        self.name = name
        self.friends = [] 
        self.interests = []
        self.posts = []

