# def function(products):
#   count = 1
#   for product in products:
#     print(count, product)
#     count = count + 1

#     choose = int(input("choose product: "))
#     money = int(input("please enter money: "))

#     if choose == 1 and money >= 2:
#       return "Cola"
#     if choose == 2 and money >= 1:
#       return "Borjomi"
#     if choose == 3 and money >= 4:
#       return "Snickers"
#     else:
#       print("invalid option")

# print(function(["Cola 2.00 Borjomi 1.00 Snickers 4.00"]))

# def add(num1, num2):
#   return num1 + num2

# print(add(1939, 97))

# def print_products(products):
#     count = 1
#     for product in products:
#         print(count, product)
#         count = count + 1

# def get_product(choice, products):
#     return products[choice]

# def check_products(choice, products):
#     choice = choice - 1
#     if choice >= 0 and choice < len(products):
#         return choice

# def vending_machine(products):
#     print_products(products)

#     choice = int(input("Please enter choice: "))

#     choice = check_products(choice, products)

#     result = get_product(choice, products)

#     return result


# print(vending_machine(["Cola 2.00", "Borjomi 5.00", "Snickers 3.00", "Pomidori"]))

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == '*':
        return num1 * num2
    else:
        return "Error: Invalid operator"
    
print(calculate(10, 20, "+"))