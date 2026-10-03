package prac13;

import java.sql.*;

public class Prac13 {

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/shaad26","root","mysql");
            Statement st = con.createStatement();
            String sqlq1 = "insert into Employee values (1,'Shaad',2024,50000)";
            String sqlq2 = "insert into Employee values (2,'Rashid',2024,50000)";
            String sqlq3 = "insert into Employee values (3,'Abdullah',2024,50000)";
//            st.addBatch(sqlq1);
//            st.addBatch(sqlq2);
//            st.addBatch(sqlq3);
//            String update = "update Employee set salary= 25000 where id=3;";
//            st.addBatch(update);
            String remove = "delete from employee where id = 3";
            st.addBatch(remove);
            st.executeBatch();
            System.out.println("Is it working?");
        } catch (Exception e) {
            System.out.println("Something- went wrong here is the error: " + e);
        }
    }
}
