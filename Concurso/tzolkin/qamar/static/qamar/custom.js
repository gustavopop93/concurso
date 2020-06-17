$(window).load(function(){
  /*Al terminar de cargar el sitio, primero se va la animación del Preloader*/
  $("#loader").fadeOut();
  /*Medio segundo despues, se va poco a poco el fondo del preloader*/
  $("#loader-wrapper").delay(10).fadeOut("slow")
})