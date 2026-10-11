
import java.util.*;

public class Pract10A {

    public static void main(String[] args) {

        List<String> obj = new ArrayList<>();

        obj.add("Ananya");
        obj.add("Tanisha");
        obj.add("Ali");
        obj.add("Shaad");

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
