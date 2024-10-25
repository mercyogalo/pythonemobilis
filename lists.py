people=["Mercy", "Linet", "Nancy", "Violet","Alfred","Doe"]

#the index is just like an array
print(people[3])

#length of the list
print(len(people))

index=len(people)-1

print(people[index])

#range of data in a lists
print(people[0:6])

people.insert(0, "Susan")
people.remove("Doe")

print(people)
