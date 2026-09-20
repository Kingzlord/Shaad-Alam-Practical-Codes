#include<iostream>
using namespace std;
class Operation{
    public:
        void perform(int a, char choice, int b){
            switch (choice)
            {
            case '+':
                cout<<a<<choice<<b<<"="<<a+b;
                break;
            case '-':
                cout<<a<<choice<<b<<"="<<a-b;
                break;
            case '*':
                cout<<a<<choice<<b<<"="<<a*b;
                break;
            case '/':
                if (b==0){
                    cout<<"Indefinite";
                }
                else{
                    cout<<a<<choice<<b<<"="<<a/b;
                }
                break;
            default:
                cout<<"Invalid";
                break;
            }
        }
};
int main(){
    Operation obj;
    int a,b;
    char c;
    cout<<"Enter operation (in A [operation] B format):\n";
    cin>>a>>c>>b;
    obj.perform(a,c,b);
    return 0;
}