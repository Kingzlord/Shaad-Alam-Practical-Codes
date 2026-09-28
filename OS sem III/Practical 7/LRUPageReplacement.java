
import java.util.*;

public class LRUPageReplacement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of pages:");
        int n = sc.nextInt();
        int[] pages = new int[n];
        System.out.println("Enter page reference String:");
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }
        System.out.println("Enter number of frames:");
        int frames = sc.nextInt();
        ArrayList<Integer> memory = new ArrayList<>();
        int pageFaults = 0;
        for (int page : pages) {
            if (memory.contains(page)) {
                //Page is already in memory
                memory.remove((Integer) page);
                memory.add(page);
            } else {
                //Page Fault
                pageFaults++;
                if (memory.size() == frames) {
                    //Remove least recently used page
                    memory.remove(0);
                }
                memory.add(page);
            }
            System.out.println("Page" + page + "->" + memory);
        }
        System.out.println("\n Total Page Faults=" + pageFaults);
        System.out.println("Total Page Hits=" + (n - pageFaults));
        sc.close();
    }
}
