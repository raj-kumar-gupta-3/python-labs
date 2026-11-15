name = input("Enter your name: ")
goal = input("Enter your goal: ")
with open("notes.txt", "w") as file:
  file.write("Name: " + name + "\n")
  file.write("Goal: " + goal + "\n")
  print("Saved to notes.txt")
  with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
