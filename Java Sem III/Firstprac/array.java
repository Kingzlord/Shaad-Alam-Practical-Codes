//To print the smallest and largest element in array
import java.util.Arrays;
import java.util.Scanner;
public class array{
    public static void main(String[] arg){
        int[] a = new int[5];
        System.out.println("Enter any 5 numbers array:");
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            a[i] = sc.nextInt();
        }
        Arrays.sort(a);
        for (int j : a) {
            System.out.print(j + ",");
        }
        System.out.println();
        System.out.println("Smallest Element:"+a[0]+"\nLargest Element:"+a[9]);

    }


}
