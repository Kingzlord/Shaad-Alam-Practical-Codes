#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
// int main(){
//     // // ofstream rd; //ofstream is used to write the content of file
//     // // ifstream wr; //ifstream is used to read contetns in the file
//     // // fstream file; //to open the file in either of the modes
//     // // file.open("hello.txt",ios::out); //open/create a file in reading mode
//     // // file.open("hello.txt",ios::in) //open a file in writing mode

//     // /*WAP to create a file student.txt to store student details such as rollno and name*/
//     // ofstream wr;                            
//     // wr.open("student.txt");
//     // int rollno;
//     // char name[50];
//     // cout<<"Enter your Roll No. and Name";
//     // cin>>rollno>>name;                                  
//     // wr<<"Roll No.:"<<rollno<<"\nName: "<<name;
//     // wr.close();

//     // /*reading the file*/
//     // ifstream rd;
//     // rd.open("student.txt");
//     // char temp;
//     // while(rd){
//     //     cout<<temp;
//     //     rd>>temp;
//     //     cout<<" ";
//     // }

//     /*pointers: WAP to display a value & address of var using pointer;*/

//     // int a=5;
//     // int *p;
//     // p = &a; //pointing to a var
//     // cout<<p<<endl; //address of var using pointer
//     // cout<<*p; //value of var using pointer
//     // return 0;
    

// }

/*to demonstrate the use of pointer on obj*/

// class test{
//     public:
//     int a=5;
//     void show(){
//         cout<<"Value of a="<<a;
//     }

// };

// int main(){

//     test obj,*p;
//     p = &obj;
//     cout<<"Call function of class using pointer"<<endl;
//     p->show();

//     return 0;
// }

/*WAP to calc area of a square using pure virtual func*/

// Note: Pure virtual uses =0 whereas normal virtual doesn't

// class Shape{
//     public:
//     float a,side;
//     void getData(){
//         cout<<"Enter the sides of sqr";
//         cin>>side;
//     }
//     virtual float area()=0; // for normal virtaul [virtual float area();]
// };

// class Square:public Shape{
//     public:
//     float area(){
//         a = side*side;
//         return a;
//     }

// };
// int main(){
//     float area;
//     Square obj;
//     obj.getData();
//     area = obj.area();
//     cout<<"Area = "<<area;
// }

/*Inheritence*/
// WAP to create a base class Shape with width and height data members and
// setData() function to initialize width and height. Create sub class Rectangle with
// calArea() function to return area of rectangle.

// class Shape{
//     public:
//     float lg,wd;
//     void getData(){
//         cout<<"Enter the Length and breadth: ";
//         cin>>lg>>wd;
//     }
// };

// class Rect:public Shape{
//     public:
//     float area(){
//         float a = lg*wd;
//         return a;
//     }

// };
// int main(){
//     float area;
//     Rect obj;
//     obj.getData();
//     area = obj.area();
//     cout<<"Area = "<<area;
// }

/*Hybrid Inheritence*/
// Write a program to create Employee class to get id and name of the employee.
// Create a sub class workinghrs to get number of working hours of an employee.
// Create another class commission to get commission amount from user. Create a
// sub class Salary from base classes workinghrs and commission to calculate and
// display net salary where basic salary of each employee is 20,000 and 300 hourly
// basis

// class Emp{
//     public:
//     int id;
//     char name[50];
//     void getData(){
//         cout<<"Enter Name and id: ";
//         cin>>name>>id;
//     }
// };

// class workinghrs:public Emp{
//     public:
//     int hrs;
//     void getHrs(){
//         cout<<"Enter your working hours: ";
//         cin>>hrs;
//     }
// };

// class Commission{
//     public:
//     int comamt;
//     void getCom(){
//         cout<<"Enter commission amount: ";
//         cin>>comamt;
//     }
// };

// class Sal:public workinghrs, public Commission{
//     public:
//     int netsal;
//     void calcNetSal(){
//         netsal = 20000+300*hrs+comamt;
//         cout<<"Net Salary = "<<netsal;
//     }
// };

// int main(){
//     Sal obj;
//     obj.getData();
//     obj.getHrs();
//     obj.getCom();
//     obj.calcNetSal();
// }

/*Polymorphism*/
/*Funtion overloading...
WAP to find area of rectangle and circle using function overloading*/

// #include<iostream> 
// using namespace std;
// void area(int l,int b){ 
//  	int a=l*b; 
//  	cout<<"Area of Rect= "<<a<<endl; 
// } 
// void area(float r){ 
//  	float a=3.14*r*r; 
//  	cout<<"Area of Circle= "<<a<<endl; 
// } 
// int main(){    		
// 	int m,n;
// 	float x; 
//  	cout<<"Enter Length and Breadth below:";
// 	cin>>m>>n; 
//  	cout<<"Enter Radius below:";  			
// 	cin>>x;
// 	area(m,n);
// 	area(x);
// 	return 0; 
// } 

/*operator overloading
WAP to calculate the addition of two complex problems using operator overloading
*/

// class Complex{
//     public:
//     int real, img;
//     void getData(){
//         cout<<"Enter the real part and img part";
//         cin>>real>>img;
//     }
//     void show(){
//         cout<<real<<"+"<<img<<"i";
//     }
//     Complex operator +(Complex c2){
//         Complex c3;
//         c3.real = this->real + c2.real;
//         c3.img = this->img + c2.img;
//         return c3;
//     }
// };

// int main(){
//     Complex c1,c2,c3;
//     c1.getData();
//     c2.getData();

//     c3 = c1 + c2;
//     c3.show();
//     return 0;
// }

/*Constructor overloading*/
/*WAP to demonstrate Constructor overloading and WAP to demonstrate types of contructor*/

// class Test{
//     public:
//     Test(){
//         cout<<"this is normal constructor"<<endl;
//     }
//     Test(int a){
//         cout<<"Value"<<a<<endl;
//     }
//     Test(int a, int b){
//         int c;
//         c = a+b;
//         cout<<c<<endl;
//     }
//     Test(Test &obj){  
//         cout<<"Object copied"<<endl;
//     }
// };

// int main(){
//     Test obj1;
//     Test obj2(5);
//     Test obj3(5,6);
//     Test obj4(obj1);
//     return 0;
// }

/*Function Overriding*/
// class base{
//     public:
//     void samename(){
//         cout<<"this func is going to be over riden";
//     }
// };

// class child:public base{
//     public:
//     void samename(){
//         cout<<"This is child class";
//     }
// };

// int main(){
//     child obj;
//     obj.samename();
//     return 0;
// }


/*Destructor*/
// class test{
//     public:
//     test(){
//         cout<<"Constructor is called!"<<endl;
//     }
//     ~test(){
//         cout<<"Destructor came and destroyed everything!!";
//     }
// };

// int main(){
//     test obj;
//     return 0;
// }


/*Static function*/
/*WAP */

// class test{
//     static int id;
//     public:
//     static void getData(int a){
//         id = a;
//     }
//     static void display(){
//         cout<<"id = "<<id;
//     }
// };

// int test::id=0; //in static we redefine static members functions (vars)

// int main(){
//     // test obj;
//     // obj.getData(50);
//     // obj.display();
//     test::getData(50);
//     test::display();
// }

/*String manipulation*/
// int main(){
//     char a[50],b[50];
//     cout<<"Enter a and b string";
//     cin>>a>>b;
//     cout<<strlen(a)<<" "<<strlen(b)<<endl;
//     cout<<strupr(a)<<" "<<strlwr(a)<<endl;
//     cout<<strupr(b)<<" "<<strlwr(b)<<endl;
//     if (strcmp(a,b)>0){
//         cout<<"A is greater then B"<<endl;
//     }
//     else{
//         cout<<"B is greater then A"<<endl;
//     }
//     cout<<" "<<strrev(a);
//     strcpy(a,b);
//     strcat(a,b);
// }

/*Switch statement*/
/*WAP to make a simple calce*/
// int main(){
//     int a,b;
//     int op;
//     cout<<"Enter the operands"<<endl;
//     cin>>a>>b;
//     cout<<"For Addition type 1\nSub 2\nMul 3\nDiv 4"<<endl;
//     cin>>op;
//     switch (op)
//     {
//     case 1:
//         cout<<a<<"+"<<b<<"="<<a+b;
//         break;
//     case 2:
//         cout<<a<<"-"<<b<<"="<<a-b;
//         break;
//     case 3:
//         cout<<a<<"*"<<b<<"="<<a*b;
//         break;
//     case 4:
//         cout<<a<<"/"<<b<<"="<<a/b;
//         break;
//     default:
//         cout<<"Invalid!";
//         // break;
//     }
// }

/*Arrays*/
/*WAP to declare two dimensional array with some elements and diplay them on screen*/
// int main(){
//     int a[2][2]{{0,0},{1,1}};
//     for(int i=0;i<=1;i++){
//         for(int j=0;j<=1;j++){
//             cout<<a[i][j]<<"\t";
//         }
//         cout<<endl;
//     }
// }


/*while and continue*/
// int main(){
//     int i = 0;
//     cout<<"\nDisplay nos. between 1 and 20 except 15"<<endl;
//     while (i<20){
//         i++;
//         if(i==15) {
//             continue;
//         }
//         else{     
//             cout<<i<<"\t";
//         }
        
//     }
// }

/*do-while and continue*/

// int main(){
//     int i = 0;
//     cout<<"\nDisplay nos. between 1 and 20 except 15"<<endl;
//     do{
//         i++;
//         if(i==15) {
//             continue;
//         }
//         else{     
//             cout<<i<<"\t";
//         }
//     }while(i<20);
//     return 0;
// }

/*Break*/
/*when i==4 jump of of the loop and display entered values;*/
// int main(){
//     int a;
//     for(int i=0;i<=10;i++){
//         if(i==4){
//             cout<<"Breaking";
//             break;
//         }
//         cout<<i<<"\t";
//     }
// }

/*WAP to find largest number among three nos using logical and*/
// int main(){
//     int a,b,c;
//     cout<<"Enter a b and c: ";
//     cin>>a>>b>>c;
//     if(a>b && a>c){
//         cout<<a<<" is the greatest";
//     }
//     if(b>a && b>c){
//         cout<<b<<" is the greatest";
//     }
//     if(c>b && c>a){
//         cout<<c<<" is the greatest";
//     }
// }

/*using ternary operator*/
// int main(){
//     int a,b,c;
//     cout<<"Enter any three numbers: ";
//     cin>>a>>b>>c;
//     int larg = (a>b)? ((a>c)? a:c) : ((b>c)? b:c);

//     cout<<"The numebr "<<larg<<" is the greatest";
// }

/*conditional statement basically either if else or else-if ladder*/
// int main(){
//     int a,b,c;
//     cout<<"Enter: ";
//     cin>>a>>b>>c;
//     // if(a>b && a>c){
//     //     cout<<a<<" is the greatest";
//     // }
//     // if(b>a && b>c){
//     //     cout<<b<<" is the greatest";
//     // }
//     // else{
//     //     cout<<c<<" is the greatest";
//     // }
//     if(a>b && a>c){
//         cout<<a<<" is the greatest";
//     }
//     else if(b>c){
//         cout<<b<<" is the greatest";
//     }
//     else{
//         cout<<c<<" is the greatest";
//     }
//     return 0;
// }

/*Pre and post increament and decreament */

// int main(){
//     int a=5;
//     cout<<++a<<endl; //pre-increament
//     cout<<a++<<endl; //post-increament
//     cout<<a<<endl;
//     cout<<--a<<endl; //pre-decreament
//     cout<<a--<<endl; //post-decreament
//     cout<<a;
// }

/*greates among 2 numbers using ternary*/
// int main(){
//     int a,b;
//     cout<<"Enter: ";
//     cin>>a>>b;
//     int res = (a>b)? a:b;
//     cout<<"Greatest number is: "<<res;
// }