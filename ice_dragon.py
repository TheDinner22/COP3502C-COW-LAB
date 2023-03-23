from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)

    # does this need to take in self?
    # could be static??
    def can_breathe_fire(self):
        return False

