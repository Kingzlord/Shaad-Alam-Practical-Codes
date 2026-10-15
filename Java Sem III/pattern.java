
import java.util.Scanner;

class pattern {

    public static void main(String[] var0) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }

            System.out.println();
        }

    }
}
