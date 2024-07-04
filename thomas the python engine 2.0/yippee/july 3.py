file = open("new_file.txt", "w")
file.write("apple \n")
file.write("orange \n")
file.write("banana \n")
file.write("cherries \n")
file.write("strawberry \n")
file.close()

text = file.read()

