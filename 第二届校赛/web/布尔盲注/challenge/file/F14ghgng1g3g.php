<?php

echo "SO COOL, If you can bypass this one, you can get what you want~ <br />";

if(isset($_GET['hn13'])){
    $Q = $_GET['hn13'];
	if(!preg_match('/[a-z0-9]/is',$Q)) eval($Q);
}else{
    highlight_file(__FILE__);
}
