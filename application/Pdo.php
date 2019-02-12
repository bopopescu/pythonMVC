<?php

class sdb 
{  
/*
*PDOStatement implements Traversable {
* Propiedades
*readonly string $queryString;
* Métodos 
*public bool bindColumn ( mixed $column , mixed &$param [, int $type [, int $maxlen [, mixed $driverdata ]]] )
*public bool bindParam ( mixed $parameter , mixed &$variable [, int $data_type = PDO::PARAM_STR [, int $length [, mixed $driver_options ]]] )
*public bool bindValue ( mixed $parameter , mixed $value [, int $data_type = PDO::PARAM_STR ] )
*public bool closeCursor ( void )
*public int columnCount ( void )
*public void debugDumpParams ( void )
*public string errorCode ( void )
*public array errorInfo ( void )
*public bool execute ([ array $input_parameters ] )
*public mixed fetch ([ int $fetch_style [, int $cursor_orientation = PDO::FETCH_ORI_NEXT [, int $cursor_offset = 0 ]]] )
*public array fetchAll ([ int $fetch_style [, mixed $fetch_argument [, array $ctor_args = array() ]]] )
*public string fetchColumn ([ int $column_number = 0 ] )
*public mixed fetchObject ([ string $class_name = "stdClass" [, array $ctor_args ]] )
*public mixed getAttribute ( int $attribute )
*public array getColumnMeta ( int $column )
*public bool nextRowset ( void )
*public int rowCount ( void )
*public bool setAttribute ( int $attribute , mixed $value )
*public bool setFetchMode ( int $mode )
*}
*
*****************************
*PDOStatement::bindColumn — Vincula una columna a una variable de PHP
*PDOStatement::bindParam — Vincula un parámetro al nombre de variable especificado
*PDOStatement::bindValue — Vincula un valor a un parámetro
*PDOStatement::closeCursor — Cierra un cursor, habilitando a la sentencia para que sea ejecutada otra vez
*PDOStatement::columnCount — Devuelve el número de columnas de un conjunto de resultados
*PDOStatement::debugDumpParams — Vuelca un comando preparado de SQL
*PDOStatement::errorCode — Obtiene el SQLSTATE asociado con la última operación del gestor de sentencia
*PDOStatement::errorInfo — Obtiene información ampliada del error asociado con la última operación del gestor de sentencia
*PDOStatement::execute — Ejecuta una sentencia preparada
*PDOStatement::fetch — Obtiene la siguiente fila de un conjunto de resultados
*PDOStatement::fetchAll — Devuelve un array que contiene todas las filas del conjunto de resultados
*PDOStatement::fetchColumn — Devuelve una única columna de la siguiente fila de un conjunto de resultados
*PDOStatement::fetchObject — Obtiene la siguiente fila y la devuelve como un objeto
*PDOStatement::getAttribute — Recupera un atributo de sentencia
*PDOStatement::getColumnMeta — Devuelve metadatos de una columna de un conjunto de resultados
*PDOStatement::nextRowset — Avanza hasta el siguiente conjunto de filas de un gestor de sentencia multiconjunto de filas
*PDOStatement::rowCount — Devuelve el número de filas afectadas por la última sentencia SQL
*PDOStatement::setAttribute — Establece un atributo de sentencia
*PDOStatement::setFetchMode — Establece el modo de obtención para esta sentencia
*/
    static private $db;
    private $driver=DRIVER;
     private $host=DB_HOST; 
     private $database=DB_NAME;
     private $attr=ARRAY(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION,PDO::ATTR_PERSISTENT=>true,PDO::MYSQL_ATTR_INIT_COMMAND=>"SET NAMES 'utf8'");
     private $usuario=DB_USER;
     private $pass =DB_PASS;    
    public function __construct() 
    {
        if(!self::$db) { 
            try {
               self::$db = new PDO($this->driver.$this->host.$this->database, $this->usuario, $this->pass, $this->attr);
            } catch (PDOException $e) { 
               die("PDO CONNECTION ERROR: ".$e->getMessage()."<br/>");
            }
        }
        return self::$db;              
    }

protected function __clone()
   {
 
   }
    public function beginTransaction() {
        return self::$db->beginTransaction();
    }
    
    public function commit() {
        return self::$db->commit();
    }
    
    public function errorCode() {
        return self::$db->errorCode();
    }
    
    public function errorInfo() {
        return self::$db->errorInfo();
    }
    
    public function exec($statement) {
        return self::$db->exec($statement);
    }
   
    public function getAttribute($attribute) {
        return self::$db->getAttribute($attribute);
    }

    public function getAvailableDrivers(){
        return Self::$db->getAvailableDrivers();
    }
    
    public function lastInsertId($name) {
        return self::$db->lastInsertId($name);
    }
    
    public function prepare ($statement, $driver_options=false) {
        if(!$driver_options) $driver_options=array();
        return self::$db->prepare($statement, $driver_options);
    }
   
    public function query($statement) {
        return self::$db->query($statement);
    }
   
    public function fetchAll($statement) {
        return self::$db->query($statement)->fetchAll(PDO::FETCH_ASSOC);
    }
    
    public function fetch($statement) {
        return self::$db->query($statement)->fetch(PDO::FETCH_ASSOC);      
    }
 
    public function fetchColumn($statement) {
        return self::$db->query($statement)->fetchColumn();        
    }
    

    public function quote ($input, $parameter_type=0) {
        return self::$db->quote($input, $parameter_type);
    }

    public function rollBack() {
        return self::$db->rollBack();
    }      
  
    public function setAttribute($attribute, $value  ) {
        return self::$db->setAttribute($attribute, $value);
    }
}