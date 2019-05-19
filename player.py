
""" class Player """


class Player:

    def __init__(self,robot,identifiant,client):
        self.robot = robot
        self.id = identifiant
        self.client = client

    def get_position(self):
        return self.robot
    
    def get_id(self):
        return self.id
    