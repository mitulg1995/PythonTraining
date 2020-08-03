# Code to count Occurrences in a string
print("\n")
s0 = input("Enter any text below that you want to count Occurrences :- \n")
s = "".join(s0.split(" "))


x = set(s)
x = list(x)
x.sort(reverse=True)

print("\n\n")
#print("In your submission, There are",len(s0.split(".")),"sentences and",len(s0.split(" ")),"words.\n")
print("There are",len(x),"unique characters.")
print("\n\n")


x2 = {}
for a in x:
	c = s.count(a)
	print(a,"---",c)
	x2[a] = int(c)	

	
print("\n\n")
x3 = list(x2.items())
x3 = sorted(x2.items(), key=lambda student: student[1])
x3.reverse()


print("\nPyramid :-")
j=0
z=("")
while (j < len(x2)):
	for a,b in x3: 
		b = x3[j][1]
		z = z+a
		print (z)
		j += 1

