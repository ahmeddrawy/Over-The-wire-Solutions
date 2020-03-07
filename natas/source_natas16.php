#!/usr/bin/php7.2

<?php
$key = ".\" /etc/natas_webpass/natas17#";
// echo "hello";
// if(array_key_exists("needle", $_REQUEST)) {
    // $key = $_REQUEST["needle"];
// }

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        echo("grep -i \"$key\" dictionary.txt");
    }
}
?>