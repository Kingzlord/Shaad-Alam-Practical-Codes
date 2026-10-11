
import java.util.*;

//For construtor public key word is optional
class Addition {

    public Addition() {
        System.out.print("Enter two number: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Addition of " + a + " + " + b + " = " + (a + b));
    }

    public Addition(int a, int b) {
        int c = a + b;
        System.out.println("Addition of " + a + " + " + b + " = " + c);
    }
}

public class ConstructorOverloading {

    public static void main(String[] args) {
        Addition obj = new Addition();
        Addition obj2 = new Addition(5, 6);
    }
}
