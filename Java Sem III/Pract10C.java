
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Pract10C {

    public static void main(String[] args) {

        Map<String, String> map = new HashMap<>();

        map.put("ID", "528");
        map.put("Age", "19");
        map.put("Salary", "50,000");
        map.put("Name", "Harshit");

        Scanner sc = new Scanner(System.in);

        System.out.println("Map Elements: " + map);

        System.out.println("No. of Elements in Map: " + map.size());

        System.out.println("Element Removed: " + map.remove("Age"));

        System.out.println("After Removal: " + map);

        System.out.println(map.values());

        System.out.println(map.keySet());

        System.out.println("If Map is Empty: " + map.isEmpty());

        map.clear();

        System.out.println("After Clear: " + map);

        sc.close();
    }
}
