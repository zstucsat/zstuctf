<?php
show_source(__FILE__);
//Let's warm up first, babe.
if(isset($_POST['ezmd51'])&&isset($_POST['ezmd52'])){
	if($_POST['ezmd51']!==$_POST['ezmd52']){
		if(md5($_POST['ezmd51'])===md5($_POST['ezmd52']))
			echo "Ok, Let's try something more intersting~</ br>";
		else
			die("Maybe you should leaen about md5 collision");
	}else{
		die("nonono");
	}
}else{
	die("Give Hn13 what he want!");
}
//PHP is the best language in the world!
if (isset($_POST['QnnM'])) {
	$password = $_POST['QnnM'];
	if (is_numeric($password)) {
		echo "I dont want a number</br>";
	}elseif ($QnnM == 776) {
		echo "Yeah!</br>";
	}
}
//Now, It's md5's revenge!
if(isset($_GET['hdmd5'])){
	$md5 = $_GET['hdmd5'];
	if($md5==md5($md5))
		echo "Well done. Hn13 bless you.</ br>";
	
}else{
	die("Cant you read php?");
}
//Last one
if(isset($_GET['hn13'])){
	$hn13 = $_GET['hn13'];
	if(strpos($hn13, ' ')!==flase){
		$hn13 = str_ireplace("cat", "zstuctf", $hn13);
		$hn13 = str_ireplace("more", "zstuctf", $hn13);
		$hn13 = str_ireplace("tail", "zstuctf", $hn13);
		$hn13 = str_ireplace("less", "zstuctf", $hn13);
		$hn13 = str_ireplace("head", "zstuctf", $hn13);
		$hn13 = str_ireplace("tac", "zstuctf", $hn13);
		$hn13 = str_ireplace("sort", "zstuctf", $hn13);
		$hn13 = str_ireplace("nl", "zstuctf", $hn13);
		$hn13 = str_ireplace("$", "zstuctf", $hn13);
		$hn13 = str_ireplace("curl", "zstuctf", $hn13);
		$hn13 = str_ireplace("bash", "zstuctf", $hn13);
		$hn13 = str_ireplace("nc", "zstuctf", $hn13);
		$hn13 = str_ireplace("php", "zstuctf", $hn13);
		if (preg_match("/['\*\"[?]/", $hn13)) {
			echo "come on!";
		}
		echo "Finally!";
		system($hn13);
	}
}
