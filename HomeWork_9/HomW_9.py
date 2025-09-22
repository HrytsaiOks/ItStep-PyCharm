# with open('data.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('output.txt', 'w') as file:
#     content = file.write('Python is a powerful and easy-to-learn programming language. It is widely used for web development, data analysis, and automation. Thanks to its simple syntax, Python is great for beginners and professionals alike. ')

# with open('output.txt', 'a') as file:
#     content = file.write('Python is used in artificial intelligence and machine learning projects because of its rich libraries and community support. ')

with open('output.txt', 'r+') as file:
    content = file.read()
    file.write('Many developers choose Python because it allows them to write clean and readable code. ')
    print(content)