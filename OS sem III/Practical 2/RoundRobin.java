import java.util.Scanner;
public class RoundRobin{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number of processes:- ");
        int n=sc.nextInt();
        int[]burstTime=new int[n];
        int[]remainingTime=new int[n];
        int[]waitingTime=new int[n];
        int[]turnaroundTime=new int[n];
        System.out.println("Enter Burst time for each process:- ");
        for(int i=0;i<n;i++){
            System.out.print("P"+(i+1)+":");
            burstTime[i]=sc.nextInt();
            remainingTime[i]=burstTime[i];
        }
        System.out.print("Enter Time Quantum:- ");
        int quantum=sc.nextInt();
        int time=0;
        while(true){
            boolean done=true;
            for(int i=0;i<n;i++){
                if(remainingTime[i]>0){
                    done=false;
                    if(remainingTime[i]>quantum){
                        time+=quantum;
                        remainingTime[i]-=quantum;
                    }
                    else{
                        time+=remainingTime[i];
                        waitingTime[i]=time-burstTime[i];
                        remainingTime[i]=0;
                    }
                }
            }
            if(done)
                break;
        }
        double totalWT=0,totalTAT=0;
        System.out.println("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time");
            for(int i=0;i<n;i++){
            turnaroundTime[i]=burstTime[i]+waitingTime[i];
            totalWT+=waitingTime[i];
            totalTAT+=turnaroundTime[i];
            System.out.println("P"+(i+1)+"\t\t"+burstTime[i]+"\t\t"+waitingTime[i]+"\t\t"+turnaroundTime[i]);
            }
        System.out.printf("\nAverage Waiting Time=%.2f\n",totalWT/n);
        System.out.printf("\nAverage Turanaround Time=%.2f\n",totalTAT/n);
        sc.close();
    }
}
