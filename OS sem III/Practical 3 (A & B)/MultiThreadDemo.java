// Multi thread Practical N.: 03 [B]

import java.util.Scanner;
class EvenOddThread extends Thread{
 int num;
 EvenOddThread(int num){
  this.num=num;
 }
 public void run(){
  if(num%2==0){
   System.out.println(num+ "is Even.");
  }else{
   System.out.println(num+ "is Odd.");
  }
 }
}
class ReverseThread extends Thread{
 String str;
 ReverseThread(String str){
  this.str=str;
 }
 public void run(){
  String reverse="";
  for(int i=str.length()-1;i>=0;i--){
   reverse+=str.charAt(i);
  }
  System.out.println("Reversed String:"+reverse);
 }
}
public class MultiThreadDemo{
 public static void main(String[] args){
  Scanner sc=new Scanner(System.in);
  System.out.print("Enter a number:");
  int number=sc.nextInt();
  sc.nextLine();
  System.out.print("Enter a string:");
  String text=sc.nextLine();
  EvenOddThread t1=new EvenOddThread(number);
  ReverseThread t2=new ReverseThread(text);
  t1.start();
  t2.start();
  sc.close();
 }
}
