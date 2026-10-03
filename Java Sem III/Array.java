
import java.util.Arrays;
import java.util.Scanner;

public class Array {

    public static void main(String[] args) {
        System.out.println("How many elements you want to store in an array");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        System.out.println("Enter " + n + " elements below: ");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);
        System.out.println("Smallest element is " + a[0]);
        System.out.println("Largest element is " + a[n - 1]);
    }
}
