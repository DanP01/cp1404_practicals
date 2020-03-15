
# 1:

user_name = 'name.txt'
name_file = open(user_name, 'w')
enter_name = input("Please enter name: ")
print(" Your name is: {} ".format(enter_name), file = name_file)
name_file.close()

# 2:

read_name_file = open('name.txt', 'r')
file_to_read = read_name_file.read().strip()
read_name_file.close()
print(file_to_read)

# 3:

in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

