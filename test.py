shoping_list = list()
wrong_words = ("ex", "exit", "quit")


def sotsl():
    for item in shoping_list:
        print(item)


while True:
    item = input("Enter Items ")
    clean_item = item.lower()

    if item in wrong_words:
        sotsl()
        break
    else:
        shoping_list.append(item)
