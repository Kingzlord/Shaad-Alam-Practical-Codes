
import java.util.Scanner;

interface Calculator {

    Float add(Float a, Float b);

    Float sub(Float a, Float b);

    Float mul(Float a, Float b);

    Float div(Float a, Float b);

}

class test implements Calculator {

    @Override
    public Float add(Float a, Float b) {
        return a + b;
    }

    @Override
    public Float sub(Float a, Float b) {
        return a - b;
    }

    @Override
    public Float mul(Float a, Float b) {
        return a * b;
    }

    @Override
    public Float div(Float a, Float b) {
        if (b == 0) {
            System.out.println("can't Divide by 0");
            return b;
        } else {
            return a / b;
        }
    }

}

public class Interface {

    public static void main(String[] args) {
        System.out.print("Enter two numbers: ");
        Scanner sc = new Scanner(System.in);
        Float a = sc.nextFloat();
        Float b = sc.nextFloat();

        test obj = new test();
        System.out.println(obj.add(a, b));
        System.out.println(obj.sub(a, b));
        System.out.println(obj.mul(a, b));
        System.out.println(obj.div(a, b));

    }
}
