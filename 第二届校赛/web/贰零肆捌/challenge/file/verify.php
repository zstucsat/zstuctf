<?php
include 'totp.php';

$otop_key='JBHDCMZSGIZFCTKN';

@$score=$_POST['score'];
@$totp=$_POST['totp'];
if($score>=500000){
	if(Google2FA::verify_key($otop_key, $totp)){
		header("Flag: zstuctf{C0ngr4tola7ion!_T1m3T0getFl4g.php}");
	}else{
		header("Flag: zstuctf{H4ck3r_Y0u_B4d_B4d}");
	}
}
header("Flag: zstuctf{H1gh3r_F4st3r_S7r0ng3r!}");
?>