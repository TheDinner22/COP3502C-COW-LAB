from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)
        self.image = image

    # does this need to take in self?
    # could be static??
    def can_breathe_fire(self):
        return True

