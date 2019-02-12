<body><div class="todo"><script type="text/javascript" src="/js/jquery-2.1.1.js"></script>
    <div class="cabeza">{{script}}
    <a href="inicio"><div class="imglogo">
<!-- <h1>OVERCLOCK . TECH</h1> -->
</div></a>
<div class="mi">
  <a href="/inicio"><div class="col">Inicio</div></a>
  
  <a href="/acerca"><div class="col">Qu&iacute;enes Somos</div></a>
  <a href="/servicios"><div class="col">Servicios</div></a>
  <a href="/noticias"><div class="col"  id="activo">Noticias</div></a>
  <a href="/contacto"><div class="col">Contacto</div></a>
  <div class="buscar">

<form name="buscador" action="noticias"><input type="text" name="b" placeholder="Buscar:"/><button type="submit" class="buscardor"title="buscar"/></button></form>
</div>
</div>
    </div>

<div class="cuerpo">
<div class="limite">
<form  name="orden" method="get">
<input type="hidden" name="pagina" value="{{pag}}"/>
<label class="m custom-select">

<select onChange="from()" name="limit">
<option {{si}} value=5>5</option>
<option {{si2}} value=10>10</option>
<option {{si3}} value=15>15</option>
<option {{si4}} value=20>20</option>
<option {{si5}} value=25>25</option>
<option {{si6}} value=30>30</option>
</select>
</label>

<label class="n custom-select">
<select onChange="from()" name="cambio">
<option {{ok1}} value='DESC'>Publicaciones Nuevas</option>
<option {{ok}} value='ASC'>Publicaciones Anteriores</option>
</select>

</label> </form>
</div>
<div class="servicios">
<div class='noticias'>


<div id="noticia">

{% each noticias %}
<div class="articulo">
<img src="/{{it.foto}}" class="imart"/>

<div class="descrip">
  <h3 title="{{it.titulo}}">{{it.titulo}}</h3>
  <div class="date">
<p><small><i class="fa fa-calendar"></i>&nbsp;Publicado {{it.publicado}}</small></p>
<p><small><i class="fa fa-user"></i>&nbsp;{{it.user}}</small></p>
<p><small><i class="fa fa-eye"></i>&nbsp;{{it.visitas}}&nbsp; Visitas</small></p>
<p><small><i class="fa fa-comments"></i>&nbsp;{{it.comentarios}} Comentarios</small></p>
<p><small><i class="fa fa-tags"></i>&nbsp;{{it.categoria}}</small></p></div>
<div class='contenido'><p>{{it.contenido}}</p></div>
<div class="leer">
<a href="/noticias/simple/?id={{it.id}}" title="leer mas">Leer Mas</a>
</div>
</div>



</div>
{% endeach %}

<div class="paginador">
<ul class="pagina">
<li {{selected}}><a href="/noticias/index/?pag=1&orden={{orden}}&limite={{limite}}"><i class="fa fa-step-backward"></i></a></li>
<li {{selected}}><a href="/noticias/index/?pag={{ant}}&orden={{orden}}&limite={{limite}}"><i class="fa fa-angle-double-left"></i></a></li>
<li>{{pag}}</li>
<li {{selected2}}><a href="/noticias/index/?pag={{sig}}&orden={{orden}}&limite={{limite}}"><i class="fa fa-angle-double-right"></i></a></li>
<li {{selected2}}><a href="/noticias/index/?pag={{total}}&orden={{orden}}&limite={{limite}}"><i class="fa fa-step-forward"></i></a></li>
  </ul>
  </div>

</div>
<div class="categoria">
<h3>Categorias</h3>
<div class="cat">
  {% each categorias %}
<a href="/noticias/categorias/?cat={{it.categoria}}"><p><i class="fa fa-tags"></i> {{it.categoria}} </p></a>
{% endeach %}
</div>
<h3>Ultimos Comentarios</h3>
<div class="combello">
{% each comentarios %}
<a href="/noticias/simple/?id={{it.id_contenido}}"><div class="comecont">
<img src="/{{it.foto}}" class="fotocom"/>
<h6>Escrito por:&nbsp;<i class="fa fa-user"></i> &nbsp; {{it.autor}}</h6>
<p><small><i class="fa fa-calendar"></i>&nbsp;{{it.publicado}}&nbsp;<i class="fa fa-tags"></i>&nbsp;{{it.categoria}}</small></p>
<p>{{it.comentario}}...</p>

</div></a>
{% endeach %}

</div>

<!--AUDIOPLAYER-->
<audio id="audio" preload="auto" tabindex="0" controls="" type="audio/mpeg">
        {% each musin %}
        <source type="audio/mp3" src="/{{it.musica}}">
        {% endeach %}
    </audio>
            <ul id="playlist">
              {% each musica %}
        <li>
            <a href="/{{it.musica}}">
                {{it.titulo}}
            </a>
        </li>
       {% endeach %}
    </ul>      
<!--chatbox-->
<div class="shout_caja">
  <div class="toggle_chat">
  <div class="message_box">
    </div>
    <div class="user_info">
   <input name="shout_message" id="shout_message" type="text" placeholder="Escribe un mensaje y Pulsa Enter" maxlength="100" />
   <span id="es"></span> 
    </div>
    </div>
</div>
<!--chatbox-->

</div>

</div></div>

</div>
