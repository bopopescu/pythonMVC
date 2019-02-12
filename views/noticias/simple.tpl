<body><div class="todo"><script type="text/javascript" src="/js/jquery-2.1.1.js"></script>
    <div class="cabeza">{{script}}
    <a href="inicio"><div class="imglogo">

<h1>OVERCLOCK . TECH</h1>
</div></a>
<div class="mi">
  <a href="/inicio"><div class="col">Inicio</div></a>
  <a href="/acerca"><div class="col">Qu&iacute;enes Somos</div></a>
  <a href="/servicios"><div class="col">Servicios</div></a>
  <a href="/noticias"><div class="col"  id="activo">Noticias</div></a>
  <a href="/contacto"><div class="col">Contacto</div></a>
</div>
    </div>

<div class="cuerpo">
<div class="servicios">
<div class="noticias">
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
<div><p>{{it.contenido}}</p></div>
<div class="leer">
<a href="/noticias"title="atras">Atras</a>
</div>
</div>


</div>
{% endeach %}


  <div class="comentar">
  <h3>Comentarios</h3>
  <div class="comentarios">


{% each comxid %}
<div class="comentarioscont">
<img src="/{{it.foto}}" class="fotocom"/>
<h6>Escrito por:&nbsp; {{it.autor}}</h6>
<p><small><i class="fa fa-calendar"></i>&nbsp; {{it.publicado}}</small></p>
<p>{{it.comentario}}</p>

</div>
{% end %}
</div>
<div class="formcom">
<form method="post" action="noticias/com">
<h3>Comentar</h3>
<input type="text" name="autor" placeholder="Nombre:"/>
<input type="text" name="correo" placeholder="Correo:"/>
<input type="hidden" name="id" value="{id}"/>
<input type="hidden" name="foto" value="imagenes/anonimo.png"/>
<input type="hidden" name="categoria" value="[categ]"/>
<textarea placeholder="Deja tu Comentario:" name="comentario"></textarea> 
<p><input type="submit" value="Enviar"/></p>
</form>
</div></div>


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
<p><i class="fa fa-calendar"></i> {{it.publicado}}
 <span class="autor"><i class="fa fa-tags"></i> {{it.categoria}}</span></p>
<p>{{it.comentario}}</p>

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
</div>
</div>
</div>

</div>
