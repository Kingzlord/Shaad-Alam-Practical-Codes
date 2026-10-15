
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Pract10A {

    public static void main(String[] args) {

        List<String> obj = new ArrayList<>();
        System.out.println("Enter size of list");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        sc.nextLine();

        for (int i = 1; i <= n; i++) {
            System.out.println("Enter string in list: ");
            String s = sc.nextLine();
            obj.add(s);
        }

        System.out.println("Elements of list are: " + obj);

        System.out.println("Element at index 1: " + obj.get(1));

        obj.set(1, "Harshit");

        System.out.println("Updated list: " + obj);

        obj.remove("Ali");

        System.out.println("List after removing element: " + obj);

        obj.clear();

        System.out.println("List after removing all elements: " + obj);
    }
}
