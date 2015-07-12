from math import sqrt

PRIME_TO_FIND = 10001

primeList = []

number = 2

#Keep going until the correct number of primes has been found
while(len(primeList)<PRIME_TO_FIND):
	#square_root = sqrt(number)
	isPrime = True;
	
	#Determine whether a number is prime or not
	for prime in primeList:
		#There is no need to check whether it is divisible by numbers
		#greater than its square root
		if prime>square_root:
			break
		#A number is prime if and only if it is not divisible by any of
		#its previous primes
		if number % prime == 0:
			isPrime = False
			break
			
	if isPrime:
		primeList.append(number)
		
	number += 1
	
print(primeList[PRIME_TO_FIND-1])