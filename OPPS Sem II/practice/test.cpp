#include<iostream>
using namespace std;
class test{
    public:
        char name[25];
        void getname(const char n[25]){
            int i;
            for(i=0;n[i]!='\0';i++){
                // if(n[i] != '\0'){
                //     name[i] = n[i];
                // }
                name[i] = n[i];
            }
            name[i]='\0';
        }
        // void getname(char n[25]){
        //     name[25] = n[25];
        // }
        ~test(){
            cout<<"\ndestroying everything";
            // name[25]='\0';
        }
};
int main(){
    test b;
    char nm[25];
    cout<<"Enter you name: ";
    cin>>nm;
    b.getname(nm);
    cout<<b.name;
}
