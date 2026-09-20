#include<iostream>
using namespace std;
int main(){
    int n,i;
    cout<<"Enter the number of rows: ";
    cin>>n;
    cout<<"\nPatern of * triangles is as follows:"<<endl;
    for(i=n;i>=0;i--){
        for (int j=i;j>=0;j--){
            cout<<"*";
        }
        cout<<"\n";
    }
    // for(i=0;i<=n;i++){
    //     for (int j=0;j<=n-i;j++){
    //         cout<<" ";
    //     }
    //     for (int k=0; k<2 * i - 1;k++){
    //         cout<<"*";
    //     }
    //     cout<<"\n";
    // }
}