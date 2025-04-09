date = input("Enter today's date: ")
mood = input("how would your rate your mood from 1 to 10?:")
thoughts = input("Let your thoughts flow:\n")

with open(f"../Journal/{date}.txt", "w") as file:
    file.write(mood + "\n")

    file.write(thoughts)