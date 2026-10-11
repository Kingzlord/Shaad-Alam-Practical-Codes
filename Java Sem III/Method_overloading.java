
public class Method_overloading {

    static void add(int a, int b) {
        int c = a + b;
        System.out.println("Addition of " + a + "+" + b + "=" + c);
    }

    static void add(int a, int b, int c) {

        System.out.println("Addition of " + a + "+" + b + "+" + c + "=" + (a + b + c));
    }

    public static void main(String[] args) {
        add(5, 4);
        add(5, 4, 9);
    }
}
