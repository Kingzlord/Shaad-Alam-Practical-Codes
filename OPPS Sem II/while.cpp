#include<iostream>
using namespace std;
int main(){
    int i = 0;
    cout<<"\nDisplay nos. between 1 and 20 except 15"<<endl;
    while (i<20){
        i++;
        if(i==15) {
            continue;
        }
        else{     
            cout<<i<<"\t";
        }
        
    }
}