class Restaurant:
    def __init__(self) -> None:
        self.dict_of_rests = {
            "Paradise": [{"item1": 400, "item2": 300, "item3": 200}, 3],
            "Grill9": [{"item1": 400, "item2": 300, "item3": 200}, 3],
            "ABS": [{"item1": 400, "item2": 300, "item3": 200}, 3],
        }

    def register(self):

        wish = True

        while True:
            if wish == False:
                break
            name = input("Enter restaurant name")
            proc_cap = int(input("Enter processing capacity"))
            menu = self.menu_registering()

            self.dict_of_rests[name] = [menu, proc_cap]

            choice = input("Do you want to register another restaurant?(T/F)")

            if choice == "T":
                continue
            else:
                wish = False

    def menu_registering(self):
        menu = dict()
        more = True

        while True:
            if more == False:
                break
            print(more)
            item = input("enter the item")
            price = input(f"enter the price for {item}")
            menu[item] = price
            choice = input("Do you want to register another menu item?(T/F)")
            if choice == "T":
                continue
            else:
                more = False
        print(menu)
        return menu
