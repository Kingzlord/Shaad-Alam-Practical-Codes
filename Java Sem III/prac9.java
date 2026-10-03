import java.util.*;

interface calculator{
    void add(int a, int b);
    void sub(int a, int b);
    void mul(int a, int b);
    void div(int a, int b);
}

class test implements calculator{
    public void add(int a, int b){
        System.out.print(a+b);
    }
    public void sub(int a, int b){
        System.out.print(a+b);
    }
    public void mul(int a, int b){
        System.out.print(a+b);
    }
    public void div(int a, int b){
        System.out.print(a+b);
    }
}


class prac9{
    public void main(String arg[]){
        System.out.println("hello");

    }

}
