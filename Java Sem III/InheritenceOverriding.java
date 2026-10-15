
import java.util.Scanner;

class Dept {

    int deptId;

    public Dept() {
        System.out.println("********************************");
        System.out.print("Enter Dept ID: ");
        Scanner sc = new Scanner(System.in);
        deptId = sc.nextInt();
    }

}

class Emp extends Dept {

    static int empId, Bsal, yof;
    static String ename, post;

    public Emp() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Empid: ");
        empId = sc.nextInt();
        System.out.print("Enter Name: ");
        ename = sc.next();
        System.out.print("Enter Designation: ");
        post = sc.next();
        System.out.print("Enter Year of Exp: ");
        yof = sc.nextInt();
        System.out.print("Enter Basic Salary: ");
        Bsal = sc.nextInt();

    }

}

class Comm extends Emp {

    static int noofwkhrs;
    static int comamt;

    public Comm() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter No. of hours of working");
        int noofwkhrs = sc.nextInt();
        System.out.println("********************************");

        comamt = noofwkhrs * 500;
        int netsal = Bsal + comamt;

        System.out.println("Display net Sal");
        System.out.println(netsal);

    }

}

public class InheritenceOverriding {

    public static void main(String[] args) {
        Comm obj = new Comm();
    }
}
