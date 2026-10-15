
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class Pract10B {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Set<String> set = new HashSet<>();

        System.out.println("Enter 5 programming languages:");

        for (int i = 0; i < 5; i++) {
            String x = sc.nextLine();
            set.add(x);
        }

        System.out.println(set);
        System.out.println("Size of Set: " + set.size());

        SortedSet<String> set1 = new TreeSet<String>(set);

        System.out.println("The sorted set is:");
        System.out.println(set1);

        System.out.println("Enter element to be removed:");
        String y = sc.nextLine();

        set.remove(y);

        System.out.println("Set after remove: " + set);

        sc.close();
    }
}
