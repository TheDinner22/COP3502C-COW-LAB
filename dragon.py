from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)
        self.image = image

    # does this need to take in self?
    # could be static??
    def can_breathe_fire(self):
        return True

    def print(self, msg):
        assert self.image != None, "this cow was not initilized properly"

        # can the dragon breath fire or not?
        can_or_cannot = "can" if self.can_breathe_fire() else "cannot"

        print(msg)
        print(self.image)
        print(f"This dragon {can_or_cannot} breathe fire.")

