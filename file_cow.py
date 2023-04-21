from cow import Cow

class FileCow(Cow):
    def __init__(self, name):
        super().__init__(name)

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow Image")
