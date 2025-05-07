#Write a text file
with open("TextFile.txt", 'w') as file:
    file_text = file.write("To zuando receba ")

#Read a text file
with open("TextFile.txt", 'r') as file:
    file_text = file.read()
print(file_text)

#open a text file
with open("TextFile.txt", 'a') as file:
    file_text = file.write("seu cabeçudo")

#open a text file
with open("TextFile.txt", 'r') as file:
    file_text = file.read()
print(file_text)
