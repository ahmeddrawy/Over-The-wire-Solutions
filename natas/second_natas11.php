GIF89a

<?php 
$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in, $key) {
    // $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$decoded = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$cipher = base64_decode($decoded);
// echo bin2hex( base64_decode($decoded));
// $decodedbasee64_hex = "0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c";
// echo xor_encrypt(json_encode($defaultdata) , $cipher);
/// we reached a state where we have 2 xor encrypted and we get the key
$default_js =  json_encode($defaultdata);
// ech
function xor_encrypt2($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
echo  base64_encode( xor_encrypt2( json_encode($defaultdata)));
?>