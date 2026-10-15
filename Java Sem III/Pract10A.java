
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Pract10A {

    public static void main(String[] args) {

        List<String> list = new ArrayList<>();
        System.out.println("Enter size of list");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        sc.nextLine();

        for (int i = 1; i <= n; i++) {
            System.out.println("Enter string in list: ");
            String s = sc.nextLine();
            list.add(s);
        }

        System.out.println("Elements of list are: " + list);

        System.out.println("Element at index 1: " + list.get(1));

        list.set(1, "Harshit");

        System.out.println("Updated list: " + list);

        list.remove("Ali");

        System.out.println("List after removing element: " + list);

        list.clear();

        System.out.println("List after removing all elements: " + list);
    }
}
