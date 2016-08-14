#just testing hope this works.


name = input("Please enter your name : ")
while len(name) == 0:
    name = input("That is not valid. Please enter your name : ")

for i in range(0, len(name),2):
    print(name[i], end='')

