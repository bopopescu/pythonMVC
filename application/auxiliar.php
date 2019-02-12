<?php
class auxiliar extends Pdo
{   
    private $conect;
    public function __construct()
    {
        $this->conect = new sdb();
    }
    public function co($id="")
    {   
        
        $query=$this->conect->query("SELECT COUNT(*) AS cuantos FROM comentario WHERE id_contenido='$id'");
        if($data=$query->fetch(PDO::FETCH_ASSOC)){echo $data["cuantos"];}
        return $data["cuantos"];
        
    }

    function get_file_size_unit($file_size){
switch (true) {
    case ($file_size/1024 < 1) :
        return intval($file_size ) ." Bytes" ;
        break;
    case ($file_size/1024 >= 1 && $file_size/(1024*1024) < 1)  :
        return intval($file_size/1024) ." KB" ;
        break;
    default:
    return intval($file_size/(1024*1024)) ." MB" ;
}
}

function backup()
{
$fileName = 'mysqlbackup--' . date('d-m-Y') . '@'.date('h.i.s').'.sql' ; 

if(function_exists('max_execution_time')) {
if( ini_get('max_execution_time') > 0 )     set_time_limit(0) ;
}

if (!file_exists(BACKUP_DIR)) mkdir(BACKUP_DIR , 0700) ;
if (!is_writable(BACKUP_DIR)) chmod(BACKUP_DIR , 0700) ; 
 
$content = 'deny from all' ; 
$file = new SplFileObject(BACKUP_DIR . '/.htaccess', "w") ;
$file->fwrite($content) ;

$return = "-- Base de datos: " . DB . "\n";
$return .= "--\n";

$tables = array() ; 

$result = $conect->query('SHOW TABLES' ) ; 

while ($row = $result->fetch_row()) 
{
$tables[] = $row[0] ;
}
 foreach($tables as $table)
 { 
$result = $conect->query('SELECT * FROM '. $table) ;
$num_fields = $conect->field_count  ;
$return .= '--ESTRUCTURA DE TABLA `' . $table . '`' ."-----------". "\n" ;
$return .= 'DROP TABLE  IF EXISTS `'.$table.'`;' . "\n" ; 
$shema = $conect->query('SHOW CREATE TABLE '.$table) ;
$tableshema = $shema->fetch_row() ; 
$return .= $tableshema[1].";" . "\n\n" ;
$return .= '--CONTENIDO TABLA `' . $table . '`' ."-----------". "\n";
while($rowdata = $result->fetch_row()) 
{ $return .= 'INSERT INTO `'.$table .'`  VALUES ( '  ;
for($i=0; $i<$num_fields; $i++) 
{ $return .= '"'.$rowdata[$i] . "\"," ; }
 $return = substr("$return", 0, -1) ;
 $return .= ");" ."\n" ; } 
 $return .= "\n\n" ; }
$conect->close() ;
$zip = new ZipArchive() ;
$resOpen = $zip->open(BACKUP_DIR . '/' .$fileName.".zip" , ZIPARCHIVE::CREATE) ;
if( $resOpen ){
$zip->addFromString( $fileName , "$return" ) ;
    }
$zip->close() ;
$fileSize = $this->get_file_size_unit(filesize(BACKUP_DIR . "/". $fileName . '.zip')) ; 
echo "<b>$fileName  </b> and it's file-size is :   $fileSize" ; 
}

function get($fileName) {
        $fileName = ROOT.DS.'tmp'.DS.'cache'.DS.$fileName;
        if (file_exists($fileName)) {
            $handle = fopen($fileName, 'rb');
            $variable = fread($handle, filesize($fileName));
            fclose($handle);
            return unserialize($variable);
        } else {
            return null;
        }
    }
    
    function set($fileName,$variable) {
        $fileName = ROOT.DS.'tmp'.DS.'cache'.DS.$fileName;
        $handle = fopen($fileName, 'a');
        fwrite($handle, serialize($variable));
        fclose($handle);
    }

    function stripSlashesDeep($value) {
    $value = is_array($value) ? array_map('stripSlashesDeep', $value) : stripslashes($value);
    return $value;
}

function removeMagicQuotes() {
if ( get_magic_quotes_gpc() ) {
    $_GET    = stripSlashesDeep($_GET   );
    $_POST   = stripSlashesDeep($_POST  );
    $_COOKIE = stripSlashesDeep($_COOKIE);
}
}

/** Check register globals and remove them **/

function unregisterGlobals() {
    if (ini_get('register_globals')) {
        $array = array('_SESSION', '_POST', '_GET', '_COOKIE', '_REQUEST', '_SERVER', '_ENV', '_FILES');
        foreach ($array as $value) {
            foreach ($GLOBALS[$value] as $key => $var) {
                if ($var === $GLOBALS[$key]) {
                    unset($GLOBALS[$key]);
                }
            }
        }
    }
}

function autocarga()
{
    if(AUTOCARGA==true){
spl_autoload_register(function ($clase) {
 if(file_exists('libs'.DS.strtolower($class).'.php')){
    include('libs'.DS. $clase . '.php');
 }
},true,true); }

}

}