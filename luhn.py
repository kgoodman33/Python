import sys


if sys.argv[1:]:
	number = sys.argv[1]
else:
	number = raw_input("What's the number, fool? > ")

nums = []

for i in number:
	nums.append(i)

nums2 = nums[::-1]

for i in range(len(nums2)):
	if i % 2 != 1:
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


print "The check digit is: %d " % check_digit
print "The card number is: %r" % int(nums3)









			
		