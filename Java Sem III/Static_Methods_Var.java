
import java.util.Scanner;

public class Static_Methods_Var {

    static String name;
    static int roll;
    static String classnm;
    static String coll = "Royal College";
    static int eng, math, sci;

    static void getdata() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Roll No.:");
        roll = sc.nextInt();

        System.out.print("Enter Name .:");
        name = sc.next();

        System.out.print("Enter Class .:");
        classnm = sc.next();
    }

    static void calc() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter marks in English (out of 100)");
        eng = sc.nextInt();
        System.out.println("Enter marks in Maths (out of 100)");
        math = sc.nextInt();
        System.out.println("Enter marks in Science (out of 100)");
        sci = sc.nextInt();

        int Tit = eng + sci + math;
        int per = (Tit / 3);
        System.out.println("Total Marks Obtained: " + Tit);
        System.out.println("Percentage Obtained: " + per);
    }

    public static void main(String[] args) {
        getdata();
        calc();
    }
}
