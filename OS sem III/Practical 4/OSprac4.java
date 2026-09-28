
import java.util.*;

public class OSprac4 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of frames:");
        int frames = sc.nextInt();

        System.out.println("Enter no of pages:");
        int n = sc.nextInt();

        System.out.println("Enter page reference string:");
        int[] pages = new int[n];

        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }

        Queue<Integer> queue = new LinkedList<>();

        int pageFaults = 0;
        int pageHits = 0;

        System.out.println("\nPage\tFrames\tStatus");

        for (int page : pages) {

            if (queue.contains(page)) {
                pageHits++;

                System.out.println(page + "\t" + queue + "\t\tHit");
            } else {
                pageFaults++;

                if (queue.size() == frames) {
                    queue.poll();
                }

                queue.add(page);

                System.out.println(page + "\t" + queue + "\t\tPage Fault");
            }
        }

        System.out.println("\nTotal page faults: " + pageFaults);
        System.out.println("Total page Hit: " + pageHits);

        sc.close();
    }
}
