import sys


if sys.argv[1:]:
	number = sys.argv[1]
else:
	number = raw_input("What's the number, fool? > ")

nums = []

for i in number:
	nums.append(i)

nums2 = nums[::-1]

last_digit = nums2[0]
for i in range(len(nums2)):
	if i % 2 == 0:
		nums2[i] = int(nums2[i]) * 2
	else:
		nums2[i] = int(nums2[i])

for i in range(len(nums2)):
	if int((nums2[i]) >= 10):
		z = ((int(nums2[i]) / 10) + (int(nums2[i]) % 10))
		nums2[i] = int(z)

sum = 0
for i in range(len(nums2)):
	sum += nums2[i]
	


check_digit = (sum * 9) % 10


nums.append(str(check_digit))
nums3 = ''.join(nums)





if int(check_digit) == 0:
	print "The card is valid!"
else:
	print "The card is invalid!"









			
		
