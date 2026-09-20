#include<iostream>
#include<string.h>
using namespace std;
class Number{
    public:
        int a,b;
        void getinput();
        void showinput();
        int add();
};
void Number::getinput(){
    cout<<"Enter any two numbers: ";
    cin>>a>>b;
};
void Number::showinput(){
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b<<endl;
};
int Number::add(){
    return(a+b);
};
int main(){
    Number n1;
    n1.getinput();
    n1.showinput();
    int res = n1.add();
    cout<<"Addition = "<<res;
}