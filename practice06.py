subjects = ["Linux", "Networking", "SQL"]
print("My subjects:", subjects)

new_subject = input("Add a new subject: ")
subjects.append(new_subject)
print("After adding:", subjects)

print("Total subjects:", len(subjects))

print("All subjects, one by one:")
for item in subjects:
    print("-", item)

subjects.remove("SQL")
print("After removing SQL:", subjects)
