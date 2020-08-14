<?php
$pathinfo = explode('/',$_SERVER['PATH_INFO']);
$headers = getallheaders();
if($pathinfo[1]!=='hn13'){
	echo "Maybe you can find somthing in /hn13 ";
	exit();
}else echo "<br />";
if($_SERVER['REQUEST_METHOD']!=='POST'){
	echo "POST method would be better";
	exit();
}
if(array_key_exists("X-Forwarded-For", $headers)){
    echo "<br />";
}else{
    echo "Use X-Forwarded-For to tell me where are you from!";
    exit();
}
if($headers['X-Forwarded-For']!=='hn13'){
    echo "Are you from 'hn13'?";
    exit();
}
if(!$_GET['&=&=&']){
	echo "I want a parameter called '&=&=&'.";
	exit();
}
if($_SERVER['HTTP_USER_AGENT']!=='hn13Browser'){
	echo "Use hn13Browser to access this site?";
	exit();
}
if($_SERVER['HTTP_REFERER']!=="https://www.hn13.top/"){
	echo "Your Referer should be 'https://www.hn13.top/'";
	exit();
}
echo "AWESOME!!! I've sent you the flag, go to find it!";
header("fl4g: zstuctf{W31c0me_t0_25tuc7f}");
