//WAP to implement round robin
package osprac2;

import java.util.*;

public class OSprac2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of processes: ");
        int n = sc.nextInt();
        int[] burstTime = new int[n];
        int[] remainingTime = new int[n];
        int[] waitingTime = new int[n];
        int[] turnaroundTime = new int[n];

        System.out.print("Enter Burst Time for each process: ");
        for (int i = 0; i < n; i++) {
            System.out.print("P" + (i + 1) + ":");
            burstTime[i] = sc.nextInt();
            remainingTime[i] = burstTime[i];
        }
        System.out.print("Enter Time Quantum: ");
        int qt = sc.nextInt();
        int time = 0;
        while (true) {
            boolean done = true;
            for (int i = 0; i < n; i++) {
//                done=false;
                if (remainingTime[i] > 0) {
                    done = false;
                    if (remainingTime[i] > qt) {
                        time += qt;
                        remainingTime[i] -= qt;
                    } else {
                        time += remainingTime[i];
                        waitingTime[i] = time - burstTime[i];
                        remainingTime[i] = 0;
                    }
                }

            }
            if (done) {
                break;
            }
        }
        double totalWt = 0, totalTAT = 0;
        System.out.println("\nProcess\tBurst Time\tWaiting Time\tTurnaround TIme");
        for (int i = 0; i < n; i++) {
            turnaroundTime[i] = burstTime[i] + waitingTime[i];
            totalWt += waitingTime[i];
            totalTAT += turnaroundTime[i];
            System.out.print("P" + (i + 1) + "\t\t" + burstTime[i] + "\t\t" + waitingTime[i] + "\t\t" + turnaroundTime[i] + "\n");
        }
        System.out.printf("\nAverage Waiting Time = %.2f\n", totalWt /n);
        System.out.printf("\nAverage Turnaround Time = %.2f\n", totalTAT /n);
        sc.close();

    }
}
