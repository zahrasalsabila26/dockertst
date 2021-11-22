<?php
ob_start();
getenv('MYSQL_DBHOST') ? $db_host=getenv('MYSQL_DBHOST') : $db_host="localhost";
getenv('MYSQL_DBPORT') ? $db_port=getenv('MYSQL_DBPORT') : $db_port=3306;
getenv('MYSQL_DBUSER') ? $db_user=getenv('MYSQL_DBUSER') : $db_user="root";
getenv('MYSQL_DBPASS') ? $db_pass=getenv('MYSQL_DBPASS') : $db_pass="";
getenv('MYSQL_DBNAME') ? $db_name=getenv('MYSQL_DBNAME') : $db_name="logintst";

$conn = mysqli_connect("$db_host", 
"$db_user", 
"$db_pass", 
"$db_name", 
"$db_port"
);

if ($conn->connect_error) 
	die("Connection failed: " . $conn->connect_error);
?>