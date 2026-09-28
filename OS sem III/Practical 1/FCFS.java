import java.util.*;

public class FCFS {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] bt = new int[n];
        int[] wt = new int[n];
        int[] tat = new int[n];

        // Input burst time
        for (int i = 0; i < n; i++) {
            System.out.print("Enter Burst Time for Process " + (i + 1) + ": ");
            bt[i] = sc.nextInt();
        }

        // Waiting time
        wt[0] = 0;

        for (int i = 1; i < n; i++) {
            wt[i] = wt[i - 1] + bt[i - 1];
        }

        // Turnaround time
        for (int i = 0; i < n; i++) {
            tat[i] = wt[i] + bt[i];
        }

        double totalWT = 0, totalTAT = 0;

        System.out.println("\n---------------------------------------------");
        System.out.printf("%-10s %-12s %-14s %-15s\n",
                "Process", "Burst", "Waiting", "Turnaround");
        System.out.println("---------------------------------------------");

        for (int i = 0; i < n; i++) {
            System.out.printf("%-10s %-12d %-14d %-15d\n",
                    "P" + (i + 1), bt[i], wt[i], tat[i]);

            totalWT += wt[i];
            totalTAT += tat[i];
        }

        System.out.println("---------------------------------------------");

        System.out.printf("Average Waiting Time = %.2f\n", totalWT / n);
        System.out.printf("Average Turnaround Time = %.2f\n", totalTAT / n);

        sc.close();
    }
}

/*
 * Save the file with .java extension.
 *
 * Steps to open/run:
 * 1. Open CMD
 * 2. cd pathname (e.g. Documents)
 * 3. javac FCFS.java
 * 4. java FCFS
 */