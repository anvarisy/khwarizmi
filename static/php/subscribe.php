<?php
	require_once("mailchimp/MCAPI.class.php");
	$mcapi = new MCAPI('c94a1d38b6683d601a324aeeb4d4ffe3-us1');
	//$mcapi = new MCAPI('PUT YOUR API KEY HERE...');
	$lists = $mcapi->lists();

	if($lists) {
		$merge_vars = Array('EMAIL' => $_REQUEST['mc_email']);
		$list_id = '314bbca712';
		//$list_id = 'PUT A VALID LIST ID...';
	
		if($mcapi->listSubscribe($list_id, $_REQUEST['mc_email'], $merge_vars ) ):
			echo '<span class="success-msg">Success!&nbsp; Check your inbox or spam folder for a message containing a confirmation link.</span>';
		else:
			echo '<span class="error-msg"><b>Error:</b>&nbsp;'.$mcapi->errorMessage.'</span>';
		endif;
	}
	else {
		echo '<span class="error-msg"><b>Error:</b>&nbsp;Mailchimp API is not Valid.</span>';
	}
?>