package com.fear;
import java.util.Scanner;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static void main() {
        /*Multiplication table*/
//        System.out.println("Enter a number");
//        Scanner sc = new Scanner(System.in);
//        String num = sc.nextLine();
//        System.out.println("Multiplication Table of "+num);
//        for(int i = 1; i<=10 ; i++){
//            System.out.println(num+" * "+i+" = "+num*i);
//        }


        /*Pattern of '*'*/
        System.out.println("Enter a number");
        Scanner pat = new Scanner(System.in);
        int pattern = pat.nextInt();
        for(int i=pattern; i>=1; i--){
            for(int j=1; j<=i; j++){
                System.out.print("*");
            }
            System.out.println(" ");
        }

        System.out.println("Enter a number");
        Scanner pat2 = new Scanner(System.in);
        int pattern2 = pat.nextInt();
        for(int i2=1; i2<=pattern2; i2++){
            for(int j2=1; j2<=i2; j2++){
                System.out.print("*");
            }
            System.out.println(" ");
        }
    }
}
