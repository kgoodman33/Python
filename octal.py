# just for fun, I build a decimal > octal converter!  
# input an octal number, and this code will change
# it into a decimal number.  woo!


start = raw_input("> ")

digits = []

for x in start:
	digits.append(x)


digits.reverse()
a = 1
b = 0
length = len(digits)

first_number = digits[0]


num = 0
x = 1
y = 8

while ( x < length ):
	
	num += ( y * int(digits[x]) ) 
	x += 1
	y = y * 8

decimal = int(num) + int(first_number)

print first_number
if int(first_number) != 8 or first_number != 9:
	print decimal
else:
	print "That octal number has no decimal equivilent :( "
