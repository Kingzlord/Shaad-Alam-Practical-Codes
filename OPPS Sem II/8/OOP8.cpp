//Practical 8: Program to display the value of variable using pointer and display the sum. 
//CODE:-
#include<iostream> 
using namespace std;
int main(){  	
	int a=3,b=8;  	
	int *p=&a,*q=&b; 
 	cout<<" value of 'a' using pointer: "<<*p<<endl;  	
	cout<<" value of 'b' using pointer: "<<*q<<endl;  	
	int sum= *p + *q;  	
	cout<<" Sum is: "<<sum<<endl;  	  	
	return 0;
}

