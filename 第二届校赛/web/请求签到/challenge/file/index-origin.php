<?php
$pathinfo = explode('/',$_SERVER['PATH_INFO']);
$headers = getallheaders();
if($pathinfo[1]!=='hn13'){
	echo "Maybe you can find somthing in hn13 ";
	exit();
}else echo "<br />";
if($pathinfo[2]!=='zstuctf'){
	echo "I think it would be better if your url ended with zstuctf";
	exit();
}
if($_SERVER['REQUEST_METHOD']!=='POST'){
	echo "I went to a post office to post my mail but i fogot the post code";
	exit();
}
if(array_key_exists("X-Forwarded-For", $headers)){
    echo "<br />";
}else{
    echo "Welcome to zstuctf. Tell me where are you from?";
    exit();
}
if($headers['X-Forwarded-For']!=='hn13'){
    echo "Are you from 'hn13'?";
    exit();
}
if(!$_GET['find']){
	echo "You URL didn't ask to `find` the `flag`.";
	exit();
}
if(!$_GET['&=&=&']){
	echo "I want a parameter called '&=&=&'.";
	exit();
}else {
	if($_GET['&=&=&']!=="%00\n"){
	echo "I need the &=&=& equal to '%00<br />'";
	exit();
	}
}
if(!$_SERVER['PHP_AUTH_USER']){
	echo "Do you know base auth?";
	exit();
}else{
	if($_SERVER['PHP_AUTH_USER']!=='hn13'){
		echo "Basically, you must be hn13 to access this site!!!";
		exit();
	}
	else{
		if(base64_decode($_SERVER['PHP_AUTH_PW'])!=='hn13isthebest'){
			echo "n1c3! And the password is the base64 encoded 'hn13isthebest' :p";
			exit();
		}
	}
}
if($_SERVER['HTTP_USER_AGENT']!=='hn13Browser'){
	echo "Dont you want to try the hn13Browser ?";
	exit();
}
if($_SERVER['HTTP_ACCEPT_LANGUAGE']!=='fr'){
	echo "Pouvez-vous parler français?";
	exit();
}
if($_SERVER['HTTP_CONNECTION']!=='Close'){
	echo "You see, I really dont wanna DIE, but Close would be better!";
	exit();
}
if($_SERVER['HTTP_REFERER']!=="https://www.hn13.top/"){
	echo "Why dont you just go to https://www.hn13.top/ to read some hn13's blogs first?";
	exit();
}
echo "AWESOME!!! I've sent you the flag, go to find it!";
header("fl4g: zstuctf{W31c0me_t0_25tuc7f}");
