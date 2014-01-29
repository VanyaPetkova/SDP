# Goal Object

GOAL_LENGTH = 60
GOAL_WIDTH = 1
GOAL_HEIGHT = 10

class Goal:

    def __init__(self, gid, zone, x, y, r):
        self.id = gid
        self.zone = zone
        self.dimension = (GOAL_LENGTH, GOAL_WIDTH, GOAL_HEIGHT)
        self.position = (x, y, r, 0)

    def get_id(self):
        return self.id

    def get_zone(self):
        return self.zone

    def get_position(self):
        return self.position

    def get_dimension(self):
        return self.dimension