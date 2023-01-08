def vend():
    w = {"item": "red bull", "rate": 10, "available stock": 30}
    x = {"item": "barbican", "rate": 7, "available stock": 18}
    y = {"item": "monster", "rate": 15, "available stock": 20}
    z = {"item": "sting", "rate": 2, "available stock": 60}
    items = [w, x, y, z]
    cim = 0  # cash in machine
    print("How can I help you! \n***")

    # show items, prices
    def show(items):
        print("\nitems available \n***")

        for item in list(items):
            if item.get("available stock") == 0:
                items.remove(item)
        for item in items:
            print(item.get("item"), item.get("rate"))

        print("*\n")

    # have user choose item
    while True:
        show(items)
        selected_item = input("select drink: ")
        for item in items:
            if selected_item == item.get("item"):
                rate = item.get("rate")
                while cim < rate:
                    try:
                        cim += float(input("insert " + str(rate - cim) + ": "))
                    except ValueError:
                        print("Please enter a valid amount.")
                        continue
                else:
                    print("availed items " + item.get("item"))
                    item["available stock"] -= 1
                    cim -= rate
                    print("cash remaining: " + str(cim))
                    a = input("buy something else? (y/n): ")
                    if a == "n":
                        if cim != 0:
                            print(str(cim) + " refunded")
                            cim = 0
                            print("Enjoy your drink!\n")
                            return  # exit both loops
                        else:
                            print("Enjoy your drink!\n")
                            return  # exit both loops
                    else:
                        continue


vend()
