MAX = 1000;

sum = 0

for number in range(1,MAX):
	if number%3 == 0 or number%5 == 0:
		sum+= number
		
print(sum)