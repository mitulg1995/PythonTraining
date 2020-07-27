#This is my first code to import anmes from CSV file and arrange them in vertical order

import csv

print("")
print("")
name = input("Enter the name of File : ") + ".csv"
print("")
print("-------------------------------------------------------")
print("")
with open(name) as pl:
	read = csv.reader(pl)
	for l in read:
		break
		
print("List of names : ", l)

print("")

x = len(l)

print("There are "+ str(x) + " names in list.")
print("")
print("")

for i in range(x):
	a = 0
	z = len(l[i]) 
	print(str(i+1) + ")")
	while a<z:
		print(l[i][a])
		a += 1
	print("")
