#!/usr/bin/php7.2

<?
    $_REQUEST["username"] ="admin\" or \"\"=\"\"\";//"; 
	$_REQUEST["password"] = "admin or \"\"=\"\"";  
    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    echo $query;
  ?>