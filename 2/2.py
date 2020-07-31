# Code to count Occurrences in a string
print("\n")
s = input("Enter a sentence below that you want to count Occurrences :- \n")

x = set(s)
x = list(x)
x.sort(reverse=True)

print("\n\nThere are",len(x),"unique characters in your String.\n\n")

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
