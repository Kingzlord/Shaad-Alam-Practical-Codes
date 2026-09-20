//Practical 7A: Program to demonstrate Function Overloading. 
//CODE:- 
#include<iostream> 
using namespace std;
void area(int l,int b){ 
 	int a=l*b; 
 	cout<<"Area of Rect= "<<a<<endl; 
} 
void area(float r){ 
 	float a=3.14*r*r; 
 	cout<<"Area of Circle= "<<a<<endl; 
} 
int main(){    		
	int m,n;
	float x; 
 	cout<<"Enter Length and Breadth below:";
	cin>>m>>n; 
 	cout<<"Enter Radius below:";  			
	cin>>x;
	area(m,n);
	area(x);
	return 0; 
} 
 
 
 

