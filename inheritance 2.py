import officeFurniture

def main():
    cabinet = officeFurniture.Furniture("File Cabinet", "Wood", 15, 16, 24, 3, 75.50)
    print("Product: " + cabinet.get_category())
    print("Material: " + cabinet.get_material())
    print("Length: " + str(cabinet.get_length()))
    print("Width: " + str(cabinet.get_width()))
    print("Height: " + str(cabinet.get_height()))
    print("Quantity: " + str(cabinet.get_quantity()))
    print("Price: ${:0,.2f}\n".format(cabinet.get_price()))

    print cabinet

main()
