class Furniture(object):

    def __init__(self, category, material, length, width, height, quantity, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__quantity = quantity
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set__price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def get_item_price(self):
        return self.__price * self.__quantity

    def __str__(self):
        line_item = self.__category + "   Material: " + self.__material + "   Length: " + str(
            self.__length) + "   Width: " + str(self.__width) + "   Height: " + str(self.__height) + "   Quantity: " + str(
            self.__quantity) + "   Each: ${:0,.2f}".format(self.__price) + "   Total= ${:0,.2f}".format(
            self.get_item_price())
        return line_item


class Desk(Furniture):

    def __init__(self, category, material, length, width, height, drawers, location, quantity, price):

        Furniture.__init__(self, category, material, length, width, height, quantity, price)
        self.__drawers = drawers
        self.__location = location

    def set_drawers(self, drawers):
        self.__drawers = drawers

    def set_location(self, location):
        self.__location = location

    def get_drawers(self):
        return self.__drawers

    def get_location(self):
        return self.__location

    def __str__(self):
        line_item = "Product: " + self.get_category() + "   Material: " + self.get_material() + "   Length: " + str(
            self.get_length()) + "   Width: " + str(self.get_width()) + "   Height: " + str(
            self.get_height()) + "   Number of Drawers: " + str(
            self.get_drawers()) + "   Drawer Location: " + self.get_location() + "   Quantity: " + str(
            self.get_quantity()) + "   Each: ${:0,.2f}".format(self.get_price()) + "   Total= ${:0,.2f}".format(
            self.get_item_price())
        return line_item
