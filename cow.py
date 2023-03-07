# joe goodman
# 03/07/23
# cow, a data class

# from heifer_generator import HeiferGenerator

class Cow:
    def __init__(self, name):
        self.name = name
        self.image = None

    # Returns the name of the cow. Note: the name property should NOT have a def setter.  
    def get_name(self): 
        return self.name
      
    # Returns the image used to display the cow (this should be called after the message has been displayed): pass.  
    def get_image(self):
        return self.image
      
    # Sets the image used to display the cow.  
    def set_image(self, image):
        self.image = image

