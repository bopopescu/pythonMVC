<?php
/**************CORREO**************************/
define('CORREOLOCAL','alexanderbrache@gmail.com');
define('SUBJECT','correo de overclocktech');
/**************CONFIGURACION******************/
define('BASE_URL', 'http://localhost:8080/');
define('DEFAULT_CONTROLLER', 'noticias');
define('DEFAULT_LAYOUT', 'default');
define ('DEVELOPMENT_ENVIRONMENT',true);
/********************************************/
define('APP_NAME', 'Mi Framework');
define('APP_SLOGAN', 'mi primer framework php y mvc...');
define('PIE','&copy; OVERCLOCKTECH 2014');
/************AUTOCARGAR CLASE*******************/
define ('AUTOCARGA',false);
/****************BACKUP***********************/
define('BACKUP_DIR', 'C:\wamp\www\omegaweapon\backup' ) ;
define('HOST','127.0.0.1');
define('DB','simple');
define('FORMATO','sql');
/***********DATABASE****************/
define('DB_HOST', 'host=127.0.0.1;');
define('DRIVER', 'mysql:');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'dbname=simple;');
define('DB_CHAR', 'utf8');
/******************************************/
function setReporting() {
if (DEVELOPMENT_ENVIRONMENT == true) {
    error_reporting(E_ALL);
    ini_set('display_errors','On');
} else {
    error_reporting(E_ALL);
    ini_set('display_errors','Off');
    ini_set('log_errors', 'On');
    ini_set('error_log', ROOT.DS.'logs'.DS.'error.log');
}
}
setReporting();

?>