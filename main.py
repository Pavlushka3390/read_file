with open("recept.txt", encoding= "utf-8") as file:
    lines = file.readlines()
    cook_book = {}
    for line in lines:
        line_lst = line.split(' | ')
        if len(line_lst) < 3 and not line[:1].isdigit() and len(line) != 1:
            dish = line[:-1]

            cook_book[dish] = []
        if len(line_lst) == 3:
            cook_book[dish].append({'ingredient_name': line_lst[0], 'quantity': line_lst[1], 'measure': line_lst[2].replace('\n', '')})

print(cook_book, end = "\n")