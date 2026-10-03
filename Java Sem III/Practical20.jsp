<%-- 
    Document   : action
    Created on : 3 Sep, 2026, 1:54:03 PM
    Author     : admin
--%>

<%@page import="java.sql.*" contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            int a = 34;
            int b = 21;
        %>
        <%
            void addition(int a, int b){
                return a+b;
            }
        %>
        <%
            out.println(addition(a,b))
        %>
    </body>
</html>
