<%-- 
    Document   : footer
    Created on : 25 Aug, 2026, 1:37:49 PM
    Author     : admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Footer</title>
    </head>
    <body>
        <h1>This is a footer</h1>
        <%@ page import="java.util.Date" %>
        <marquee>
        <% 
            Date d = new Date();
            out.println(d + " year" );
            out.print(d.getYear() + 1900);
        %>
        </marquee>
    </body>
</html>
