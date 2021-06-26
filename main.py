import os


def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        cook_list = [line.strip() for line in file]
        for itm, elm in enumerate(cook_list):
            if elm.isdigit():
                cook_book[cook_list[itm - 1]] = []
                for recept in cook_list[itm + 1:itm + int(elm) + 1]:
                    ingredient_name = recept.split('|')[0]
                    quantity = int(recept.split('|')[1])
                    measure = recept.split('|')[2]
                    cook_book[cook_list[itm - 1]].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
    return cook_book





def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    for key in dishes:
        if key in cooking_book.keys():
            print(key)
            for value in cooking_book[key]:
                value['quantity'] *= person_count
                print(value)
            else:
                pass
get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], get_cook_book('recept.txt'), 5)