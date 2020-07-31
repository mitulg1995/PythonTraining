# Code to count Occurrences in a string
print("\n")
s0 = input("Enter any text below that you want to count Occurrences :- \n")
s = "".join(s0.split(" "))

x = set(s)
x = list(x)
x.sort(reverse=True)

print("\n\n")
print("In your submission, There are",len(s0.split(".")),"sentences and",len(s0.split(" ")),"words.\n")
print("There are",len(x),"unique characters.")
print("\n\n")

for a in x:
	c = s.count(a)
	print(a,"---",c)

	
print("\nPyramid :-")	
b=0
z=("")
while (b < len(x)):
	y = x[b]
	z = z+y
	print(z)
	b += 1
