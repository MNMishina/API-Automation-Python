students = ["Dan", "Stan", "Emma", "Beth", "Fred", "Alan"]

for f in students:
    if f == "Alan":
        var = "Developer " + f
        print(var)

print("-----------")

for f in students[:3]:      # first 3 elements of the list
    print(f)