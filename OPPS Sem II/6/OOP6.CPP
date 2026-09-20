#include<iostream>
#include<cstring>
using namespace std;
class emp{
	public:
	int id;
	char name[20];
	emp(){
		cout<<"\nEnter ID: ";
		cin>>id;
		cout<<"\nEnter Name: ";
		cin>>name;
	}
	emp(int a,const char b[20]){
		id=a;
		strcpy(name,b);
	}
	emp(emp &obj){
		id=obj.id;
		strcpy(name,obj.name);
	}
	void show(){
		cout<<"\nID of employee: "<<id;
		cout<<"\nName of employee: "<<name<<endl;
	}
	~emp(){
		cout<<"\nDestructor Called."<<endl;
	}
};
int main(){
	emp obj1;
	obj1.show();
	emp obj(44,"Ali");
	obj.show();
	emp obj2=obj1;
	obj2.show();
	return 0;
}