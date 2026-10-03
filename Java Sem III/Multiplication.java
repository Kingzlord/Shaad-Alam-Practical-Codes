
import java.util.Scanner;

class Num {

    public static void main(String args[]) {
        System.out.println("Enter two numbers");
        Scanner si = new Scanner(System.in);
        int a = si.nextInt();
        int b = si.nextInt();
        int c = a * b;
        System.out.println(a + " * " + b + " = " + c);
    }
}
