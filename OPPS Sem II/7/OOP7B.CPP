//Practical 7B: Program to demonstrate Operator Overloading. 
//CODE:- 
#include<iostream> 
using namespace std;
class complex{
	public: 
 	int real,img;
	void getdata(){ 
		cout<<"Enter real part of Complex numbers: "; 	
		cin>>real; 
 	 	cout<<"Enter img part of Complex numbers: "; 
 	 	cin>>img; 
 	 	} 
 	void display(){ 
 	 	cout<<real<<"+"<<img<<"i"<<endl; 
 	 	} 
 	complex operator+(complex obj2){  	 	
		complex obj3; 
 	 	obj3.real=this->real+obj2.real;  	 	
		obj3.img=this->img+obj2.img;  	 	
		return obj3; 
 	 	} 
 	}; 
void main() 
{
	complex obj1,obj2,obj3; 
	obj1.getdata(); 
	obj2.getdata(); 
	obj3=obj1+obj2; 
	obj3.display();
} 
