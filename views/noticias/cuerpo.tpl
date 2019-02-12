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
<p>{{it.contenido}}</p>
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