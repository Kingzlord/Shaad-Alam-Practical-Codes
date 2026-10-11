
import java.util.Scanner;

public class expections {

    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter your age: ");
            int age = sc.nextInt();
            if (age == 18) {
                System.out.println("You are eligible to vote: ");
            } else {
                throw new IllegalArgumentException("You are not eligible to vote");
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
