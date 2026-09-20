def recu(n):
	if n==0 or n==1:
		return 1
	else:
		return n * recu(n-1)
	
n = 5
fact = recu(n)
print(fact)

'''
1. define a fucntion recur and pass the variable 'n' whose fact we need to find
2. check if the number is equal to 0 or 1 and then return 1
3. else return n * recur(n-1)
4. take the input n from the user 
5. call the funtion recur and and store the output in variable fact
6. print fact
'''