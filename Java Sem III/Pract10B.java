
import java.util.*;

public class Pract10B {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Set<String> obj = new HashSet<String>();

        System.out.println("Enter 5 programming languages:");

        for (int i = 0; i < 5; i++) {
            String x = sc.nextLine();
            obj.add(x);
        }

        System.out.println(obj);
        System.out.println("Size of Set: " + obj.size());

        SortedSet<String> obj1 = new TreeSet<String>(obj);

        System.out.println("The sorted set is:");
        System.out.println(obj1);

        System.out.println("Enter element to be removed:");
        String y = sc.nextLine();

        obj.remove(y);

        System.out.println("Set after remove: " + obj);

        sc.close();
    }
}
