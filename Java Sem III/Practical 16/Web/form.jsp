<%-- 
    Document   : form
    Created on : 25 Aug, 2026, 2:08:04 PM
    Author     : admin
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <form action="http://localhost:8080/Practical16/servlet">
            <h3>Enter Your Name</h3>
            <input type="text" name="txtnm" value="" />
            
            <h3>Enter Your Roll no.</h3>
            <input type="text" name="txtrol" value="" /> <br>    
            <input type="submit" value="Submit" /> 
        </form>
    </body>
</html>
