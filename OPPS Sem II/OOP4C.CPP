#include<iostream.h>
#include<conio.h>
class Input{
	int num;
	public:
	void getnum(){
		do{
		cout<<"Enter numbers until 0 is reached.";
		cin>>num;
		}
	while(num!=0);
	}
};
int main(){
	clrscr();
	Input obj;
	obj.getnum();
	getch();
	return 0;
}