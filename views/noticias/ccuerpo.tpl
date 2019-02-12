<div id="noticia">

{% each noticias %}
<div class="articulo">
<h2 title="{{it.titulo}}">{{it.titulo}}</h2>
<img src="/{{it.foto}}" class="imart"/>
<div class="descrip">
<p>{{it.contenido}}</p>
</div>
<div class="leer">
<a href="/noticias/simple/?id={{it.id}}" class="boton"title="leer mas">Leer Mas...</a>
</div>
<div class="date">
<p><i class="fa fa-calendar"></i> &nbsp;PUBLICADO {{it.publicado}} </p>
<p class="autor"> <i class="fa fa-user"></i>&nbsp; {{it.user}}</p>
<p><i class="fa fa-eye"></i>&nbsp; {{it.visitas}}&nbsp; Visitas</p>
<p class="autor"><i class="fa fa-comments"></i>&nbsp; {{it.comentarios}} COMENTARIOS</p>
<p><i class="fa fa-tags"></i>&nbsp; {{it.categoria}}</p></div>
</div>
{% endeach %}

<div class="paginador">
<ul class="pagina">
<li {{selected}}><a href="/noticias/categorias/?pag=1&cat={{cate}}&orden={{orden}}&limite={{limite}}">Inicio</a></li>
<li {{selected}}><a href="/noticias/categorias/?pag={{ant}}&cat={{cate}}&orden={{orden}}&limite={{limite}}">Anterior</a></li>
<li>{{pag}}</li>
<li {{selected2}}><a href="/noticias/categorias/?pag={{sig}}&cat={{cate}}&orden={{orden}}&limite={{limite}}">Siguiente</a></li>
<li {{selected2}}><a href="/noticias/categorias/?pag={{total}}&cat={{cate}}&orden={{orden}}&limite={{limite}}">Fin</a></li>
</ul>
</div>
</div>