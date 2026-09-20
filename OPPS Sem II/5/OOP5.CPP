#include<iostream>
using namespace std;
class matrix
{
    int a[2][2],b[2][2],c[2][2];
    public:
    int i,j;
    void input()
    {
        cout<<"Enter elements for matrix a:\n";
        for(i=0;i<2;i++)
        {
            for(j=0;j<2;j++){
                cin>>a[i][j];
         }
        }
        for(i=0;i<2;i++)
        {
            cout<<"Enter elements for matrix b:\n";
            for(j=0;j<2;j++)
            {
                cin>>b[i][j];
            }
        }
    }
    void display()
    {
        cout<<"Resultant matrix: \n";
        for(i=0;i<2;i++)
        {
            for(j=0;j<2;j++)
    {
    c[i][j]=a[i][j]+b[i][j];
    cout<<c[i][j]<<" ";
    }
    cout<<endl;
    }
    }
    };
int main()
{
matrix m;
m.input();
m.display();
return 0;
}