<?php
ini_set('display_errors',0);
error_reporting(0);
session_set_cookie_params(1800);
session_start();
header("Content-Type: application/json");
header('Access-Control-Allow-Origin: *');

echo "I am a sluggard, so I got no front-end for you.\n";
//echo type($_POST['username']);
$username=$_POST['username'];
//echo $username;
$password=$_POST['password'];
//echo $password;
$i = rand(0, 5);
$words = array("Give me something i want", "I want your passion and something!", "Show me something!", "Tell me who you are!", "hn13 forever!", "q-m-m :)");
if(!$_POST){
	echo $words[$i];
	exit();
}
if (strlen($username)>100 || strlen($password)>100){
    $res=array("code"=>404,"message"=>'username or password too long<br>');
}
if (strlen($username)>0 && strlen($password)>0){
	if($username!='admin')
		$res=array("code"=>404,"message"=>'You should be amdin to get what you want!');
    include('file/sql.php');
    $res=array("code"=>0,"message"=>$res);
}else{
    $res=array("code"=>404,"message"=>'You didnt give me what I want!');
}
die(json_encode($res));
?>