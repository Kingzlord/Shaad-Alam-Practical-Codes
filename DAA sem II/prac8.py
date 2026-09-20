#PRAC 8(B)
#fibonacci series:
'''def fib(n):
    a,b=0,1
    print("Fibonacci series upto",n,"terms.")
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
if __name__=="__main__":
    n=int(input("Enter the value of fibonacci series: "))

    fib(n)'''
##recursive
'''
def fib(n):
    if n<0:
        print("Invalid")

    elif n==0:
        return 0

    elif n==1 or n==2:
        return 1
    
    else:
        return fib(n-1) + fib(n-2)
a = int(input("Etner the range of firbonacci: "))
print("fibonacci series" ,fib(a))
'''

#PRAC 8(A)

# factorial (recursion):
# Factorial recursive
'''
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1) 
# print(fact(5))

if __name__ == "__main__":
    n = int(input("Enter a number to find factorial: "))
    print(fact(n))
'''

# factorial iterative 
'''
n = int(input("Enter any number: "))
f = 1
for i in range(1,n+1):
    f *= i
print("factorial is: ",f)
'''

## Tower of hanoi iterative method
'''
n = int(input("Etner the number of disks: "))
src = 'A'
aux = 'C'
des = 'B'

total_moves = 2**n - 1
print("Total possible moves using iteration method", total_moves)

if n % 2 == 0:
    des, aux = aux, des

rods = {'A': list(range(n, 0, -1)),
        'B': [],
        'C': []}

for move in range(1, total_moves + 1):

    if move % 3 == 1:
        from_rod, to_rod = ('A', 'B') if (
            rods['A'] and (not rods['B'] or rods['A'][-1] < rods['B'][-1])
        ) else ('B', 'A')

    elif move % 3 == 2:
        from_rod, to_rod = ('A', 'C') if (
            rods['A'] and (not rods['C'] or rods['A'][-1] < rods['C'][-1])
        ) else ('C', 'A')

    else:
        from_rod, to_rod = ('B', 'C') if (
            rods['B'] and (not rods['C'] or rods['B'][-1] < rods['C'][-1])
        ) else ('C', 'B')

    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    print(f"Move disk {disk} from {from_rod} to {to_rod}")

'''
##Recursive
'''
n = int(input("Enter the number of disks: "))
src = 'A'
aux = 'B'
des = 'C'
i=0

def move_disks(n,src,des,aux):
    global i
    if n==1:
        i+=1
        print(f"{i}: Move disk 1 from {src} to {des}")
        return
    move_disks(n-1,src,aux,des)

    i+=1
    print(f"{i}: Move disk {n} from {src} to {des}")
    move_disks(n-1,aux,des,src)

    
move_disks(n,src,des,aux)
'''
