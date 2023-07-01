shoping_list = list()
wrong_words = ("ex", "exit", "quit")


def sotsl():
    for item in shoping_list:
        print(item)

<<<<<<< HEAD
print(result)
hmac.
=======

while True:
    item = input("Enter Items ")
    clean_item = item.lower()

    if item in wrong_words:
        sotsl()
        break
    else:
        shoping_list.append(item)
>>>>>>> f0e64c92c0272aa3a2d1eb2a2ddbec1f2c1cfe89
