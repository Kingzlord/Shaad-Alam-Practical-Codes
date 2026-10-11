
import java.util.*;

public class Pract10C {

    public static void main(String[] args) {

        Map<String, String> obj = new HashMap<String, String>();

        obj.put("ID", "528");
        obj.put("Age", "19");
        obj.put("Salary", "50,000");
        obj.put("Name", "Harshit");

        Scanner sc = new Scanner(System.in);

        System.out.println("Map Elements: " + obj);

        System.out.println("No. of Elements in Map: " + obj.size());

        System.out.println("Element Removed: " + obj.remove("Age"));

        System.out.println("After Removal: " + obj);

        System.out.println(obj.values());

        System.out.println(obj.keySet());

        System.out.println("If Map is Empty: " + obj.isEmpty());

        obj.clear();

        System.out.println("After Clear: " + obj);

        sc.close();
    }
}
