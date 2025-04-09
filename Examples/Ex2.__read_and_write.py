filenames = ["doc.txt", "report.txt", "presentation.txt"]

for files in filenames:
    file = open(f"{files}.txt", "w")
    file.write("Hello")
    file.close()

filenames1 = ["a.txt", "b.txt", "c.txt"]

for filename in filenames1:
    file = open(filename, "r")
    content = file.readlines()
    print(content)

    file.close()