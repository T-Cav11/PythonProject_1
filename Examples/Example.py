password = input("Enter password ")

while password != "Pass123":
    password = input("Enter password")

print("Password was correct")

x = 1

while x<= 6:
    print(x)
    x = x+1


filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
for filename in filenames:
    filename = filename.replace(".","-",1)
    print(filename)

waiting_list = ["Sen", "Ben", "John"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item}"
    print(row)

file = open("bear.txt", "r")
content = file.read()
file.close()

print(content)

file = open('file.txt', 'w')
file.write('snail')
file.close()

filenames = ["1.doc", "2.doc", "3.presentation"]
filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]
print(filenames)


