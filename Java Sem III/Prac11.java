//WAP to define yuser-defined exceptions and raise them as oer the requirements

import java.util.*;

public class Prac11 extends Exception {

    static int a;

    public Prac11(String message) {
        super(message);
    }

    public static void main(String[] args) {

        try {
            System.out.println("Enter your age");
            Scanner sc = new Scanner(System.in);
            a = sc.nextInt();
            if (a < 18) {
                throw new Prac11("Not Eligible to vote");
            } else {
                System.out.println("You are Eligible to vote");
            }
        } catch (Prac11 e) {
            System.out.println("Error" + e);
        } catch (Exception e) {
            System.out.println("Error" + e);
        }
    }
}
