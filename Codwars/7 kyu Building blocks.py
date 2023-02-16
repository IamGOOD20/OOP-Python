class Block:
    def __init__(self, param):
        if len(param) == 3:
            self.get_width = param[0]
            self.get_length = param[1]
            self.get_height = param[2]
            self.get_volume = self.get_width * self.get_width * self.get_height

            self.get_surface_area = 2 * (self.get_width * self.get_length +
                                          self.get_length * self.get_height + self.get_width * self.get_height)

    # def get_volume(self):
    # return self.get_width * self.get_width * self.get_height

    #def get_surface_area(self):
    #   return 2 * (self.get_width * self.get_length + self.get_length * self.get_height + self.get_width * self.get_height)
    #b.get_volume() -> return 48

    #b.get_surface_area() -> return 88


block1 = Block([2, 4, 6])
print(block1.get_surface_area)
print(block1.get_length)
print(block1.get_height)
print(block1.get_width)
print(block1.get_surface_area)