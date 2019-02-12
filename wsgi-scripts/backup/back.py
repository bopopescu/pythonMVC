class Request
{
    private $_controlador;
    private $_metodo;
    private $_argumentos;

    public function __construct() {
        if(isset($_GET['url'])){
            $url = filter_input(INPUT_GET, 'url', FILTER_SANITIZE_URL);
            $url = explode('/', $url);
            $url = array_filter($url);

            $this->_controlador = strtolower(array_shift($url));
            $this->_metodo = strtolower(array_shift($url));
            $this->_argumentos = $url;
        }

        if(!$this->_controlador){
            $this->_controlador = DEFAULT_CONTROLLER;
        }

        if(!$this->_metodo){
            $this->_metodo = 'index';
        }

        if(!isset($this->_argumentos)){
            $this->_argumentos = array();
        }
    }

    public function getControlador()
    {
        return $this->_controlador;
    }

    public function getMetodo()
    {
        return $this->_metodo;
    }

    public function getArgs()
    {
        return $this->_argumentos;
    }
}

#import urlparse
#query = os.environ.get('QUERY_STRING')
#parsed = os.environ.get('REQUEST_URI')
#parsed = parsed.split("/")
#cabeza ='maqueta/cabeza.tpl'
#pagina = 'views/'+parsed[1]+'/index.tpl'
#pie='maqueta/pie.tpl'
#print "Content-Type: text/html;charset=utf-8"
#head =open(cabeza).read()
#body=open(pagina).read()
#foot=open(pie).read()
#print
#print head
#print body
#print foot
