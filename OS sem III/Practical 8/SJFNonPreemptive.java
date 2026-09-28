
import java.util.*;

class Process {

    int pid;
    int arrivalTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;
    boolean completed;

    Process(int pid, int arrivalTime, int burstTime) {
        this.pid = pid;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
        this.completed = false;
    }
}

public class SJFNonPreemptive {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of processes:");
        int n = sc.nextInt();
        Process[] processes = new Process[n];
        for (int i = 0; i < n; i++) {
            System.out.print("\nProcess P" + (i + 1));
            System.out.print("Arrival Time:");
            int at = sc.nextInt();
            System.out.print("Burst Time:");
            int bt = sc.nextInt();
            processes[i] = new Process(i + 1, at, bt);
        }
        int currentTime = 0;
        int completed = 0;
        double totalWaitingTime = 0;
        double totalTurnaroundTime = 0;

        while (completed < n) {
            int shortest = -1;
            int minBurst = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                if (!processes[i].completed && processes[i].arrivalTime <= currentTime && processes[i].burstTime < minBurst) {
                    minBurst = processes[i].burstTime;
                    shortest = i;
                }
            }
//if no process arrive,move the time forward
            if (shortest == -1) {
                currentTime++;
                continue;
            }
            Process p = processes[shortest];
            currentTime += p.burstTime;
            p.completionTime = currentTime;
            p.turnaroundTime = p.completionTime = p.arrivalTime;
            p.waitingTime = p.turnaroundTime = p.burstTime;
            p.completed = true;
            completed++;
            totalWaitingTime += p.waitingTime;
            totalTurnaroundTime += p.turnaroundTime;
        }
        System.out.println("\nProcess\tAT\tBT\tCT\tTAT\tWT");
        for (Process p : processes) {
            System.out.println(
                    "P" + p.pid + "\t" + p.arrivalTime + "\t"
                    + p.burstTime + "\t"
                    + p.completionTime + "\t"
                    + p.turnaroundTime + "\t"
                    + p.waitingTime + "\t"
            );
        }
        System.out.printf("\n Average Waiting Time:%.2f", totalWaitingTime / n);
        System.out.printf("\n Average Turnaround Time:%.2f", totalTurnaroundTime / n);
        sc.close();
    }
}
