#!C:\Python27\python.exe -u
#!/usr/bin/env python
import cgitb
cgitb.enable()
import cgi
import urlparse
import os, string
parsed = os.environ.get('REQUEST_URI')
print "Content-Type: text/html;charset=utf-8"
print
print parsed
print'''
<html>
<head>
<title>
OVERCLOCKTECH
</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<LINK REL="SHORTCUT ICON" HREF="imagenes/youtube.png">
<meta name="generator" content="">
<meta name="reply-to" content="alexanderbrache@gmail.com">
<meta name="author" content="http://www.overclocktech.net">
<meta name="author" content="Alexander Brache">  
<meta name="description" content="overclocktech,computer,hack,electronics,programing,games,css,php,c#,html,javascript,python,ruby">
<meta name="keywords" content="overclocktech,computer,hack,electronics,programing,games,css,php,c#,html,javascript,python,ruby">
<link rel="stylesheet" type="text/css" href="css/estilo.css">
<link href="test/rss.php" rel="alternate" type="application/rss+xml" title="RSS www.overclocktech.com" />
<link href="css/sliderstyle.css" type="text/css" rel="stylesheet">
<link href="css/font-awesome.css" type="text/css" rel="stylesheet">
<link href='http://fonts.googleapis.com/css?family=Rancho&effect=shadow-multiple|3d-float|neon|fire-animation|3d|anaglyph|brick-sign|canvas-print|crackle|decaying|destruction|distressed|distressed-wood|emboss|fire|fragile|grass|ice|mitosis|outline|putting-green|scuffed-steel|shadow-multiple|splintered|static|stonewash|vintage|wallpaper' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/jquery-1.8.0.js"></script>
<script type="text/javascript" language="javascript" src="js/todo.js"></script>

</head>
<body><div class="todo">
    <div class="cabeza">
    <a href="inicio"><div class="imglogo">

<p><span class="font-effect-3d-float">OVERCLOCK<span class="b">.</span>TECH</span></p>
</div></a>
<div class="mi">
	<a href="inicio"><div class="col">Inicio</div></a>
	<a href="productos"><div class="col">Productos</div></a>
	<a href="proyectos"><div class="col">Proyectos</div></a>
	<a href="acerca"><div class="col">Qu&iacute;enes Somos</div></a>
	<a href="servicios"><div class="col">Servicios</div></a>
	<a href="blog"><div class="col">Noticias</div></a>
	<a href="contacto"><div class="col" id="activo">Contacto</div></a>
</div>
    </div>
<div class="cuerpo">
  <div class="logeo">
  <div id="l_error"></div>
  <form action="./" method="get">

  <input type="text"id="lusuario"placeholder="Usuario :"name="usuario"title="usuario">
  <input type="text"id="lpass"name="pass"title="contrase&ntilde;a"placeholder="Contrase&ntilde;a :">
  <input type="submit" class="boton"value="Entrar"id="dale"title="entrar">
  <a href="registro"title="registrarse">Registrarse</a>
  <a href="recuperar"title="recuperar contrase&ntilde;a">Recuperar Contrase&ntilde;a</a>
</form><div id="bien">Bienvenido</div><a href="salir">Cerrar Session</a>
</div>

<div class="buscar">
<h2 class="h2 font-effect-3d-float">Contacto</h2>
<form name="buscador" action="blog"><input type="text" name="b" placeholder="Buscar:"/><input type="submit" value="buscar"title="buscar"/></form>
</div>
<ul class="mm">
<li><a href="inicio">Inicio</a></li>
<li class="divider"></li>
<li class="activo"><a>Contacto</a></li>
</ul>

<iframe width="1225" height="306" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.es/?ie=UTF8&amp;ll=18.455659,-69.93982&amp;spn=0.011907,0.021136&amp;t=m&amp;z=16&amp;output=embed"></iframe><br/>
<div class="form">
	<div class="span">
	<h2 class="font-effect-3d-float">Imformaci&oacute;n de Cont&aacute;cto</h2>
	<h5>Sarasota # 40 Esq Higuemota Residencial Los Robles Apartamento 1 A 2.</h5>

<address>
<b>OverclockTech.<br>
Sarasota # 40 Esq Higuemota,<br>
Residencial Los Robles.</b><br>
<i class="fa fa-phone-square"></i> Telefono: +1 829-384-0994<br>
<i class="fa fa-print"></i> FAX: +1 809-535-0381<br>
<i class="fa fa-envelope"></i> E-mail: <a href="mailto:alexanderbrache@gmail.com">alexanderbrache@gmail.com</a><br>
<spa class="usuario"></spa>
Alexander Brache
</address>
	</div>
<div class="cform">
<h2 class="font-effect-3d-float">Cont&aacute;ctenos</h2>
<fieldset id="contact_form">
<div id="result"></div>
<input type="text" placeholder="Nombre:" name="name" id="name">
<input type="text" placeholder="E-mail:" name="email" id="email">
<input type="text" placeholder="Telefono:" name="phone" id="phone">
<textarea name="message" id="message" placeholder="Mensaje:"></textarea>
<input type="submit" id="submit_btn" class="csubmit" value="ENVIAR">
<input type="reset" Value="Borrar" id="borrar">
</fieldset>
</div>
</div>
<div class="billete">
<a href="test/rss.php" title="lector de noticias"><img src="imagenes/rss.png" class="rss"/></a>
<a href="http://www.youtube.com" title="Vea nuestros videos en youtube"><img src="imagenes/youtubeFooter.png" class="rss"/></a>
<a href="http://www.instagram.com" title="Vea nuestras fotos mas recientes en instagram"><img src="imagenes/instagramf.jpg" class="rss"/></a>
<a href="http://www.facebook.com" title="Siguenos en facebook"><img src="imagenes/facebook_01.gif" class="rss"/></a>

</div>
</div>

    <div class="pie"><hr>
 <center>
<h3><b><span class="font-effect-3d-float">&copy; OVERCLOCKTECH 2014</span></b></h3></center>
 <center><p title="Dise&ntilde;o y Programac&iacute;on Todos los derechos reservados &copy; Alexander Brache inf 829-384-0994"><span class="font-effect-3d-float">Dise&ntilde;o y Programac&iacute;on Todos los derechos reservados &copy; Alexander Brache</span></p></center>
 <ul class="cont">
<li><img src="./imagenes/adr.png"> Sarasota # 40 Esq Higuemota</li>
<li><img src="./imagenes/tel.png"> 809-535-0381 / 829-384-0994</li>
</ul>
 <ul class="social">
 	<h4><b style="color:#da823b">S&iacute;guenos</b> <span style="color:#f0eeee">en:</span></h4>
<li class="face"></li>
<li class="twi"></li>
<li class="gog"></li>
<li class="cor"></li>
</ul>
    </div>
</div>
<!--chatbox-->
<div class="shout_box">
<div class="header">overclocktech chat <div class="close_btn">&nbsp;</div></div>
  <div class="toggle_chat">
  <div class="message_box">
    </div>
    <div class="user_info">
    <input name="shout_username" id="shout_username" type="text" placeholder="Tu Nombre" maxlength="15" />
   <input name="shout_message" id="shout_message" type="text" placeholder="Escribe un mensaje y Pulsa Enter" maxlength="100" /> 
    </div>
    </div>
</div>
<!--chatbox-->

</body>
</html>
'''
