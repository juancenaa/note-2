def make_card(name, age, message="Have a good day."):
    return f"Hello {name} ({age} years old)!\n{message}"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(make_card(name, age))