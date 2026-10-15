
import java.util.Scanner;

class pattern {

    public static void main(String[] var0) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            for (int j = 0; j < i; j++) {
<<<<<<< HEAD
                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) {
=======
>>>>>>> 2e2091a8de0b1f9b14fee0a73ff0ed3f5e294da7
                System.out.print("*");
            }

            System.out.println();
        }

    }
}
