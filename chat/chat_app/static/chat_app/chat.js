$(document).ready(function(){

	var socket = new WebSocket('ws://127.0.0.1:8000/chat/');
	socket.onopen = websocket_conexion_ok;
	socket.onmessage = websocket_msj_recibido;

	$('#formulario').submit(function(e){
		e.preventDefault();
		datos = {
			'nombre' : $('input[name="nombre"]').val(),
			'mensaje': $('input[name="texto"]').val()
		}
		socket.send(JSON.stringify(datos));
		$('#formulario')[0].reset();
	});

});

function websocket_conexion_ok(){
	alert('La conexión se ha establecido');
}

function websocket_msj_recibido(e){
	datos = JSON.parse(e.data);
	codigo = '<div class="col s12">'				+
				'<div class="nombre">'				+
					'<h4>'+ datos.nombre +'</h4>'	+
				'</div>'							+
				'<div class="contenido">'			+
					'<p>'+ datos.mensaje +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversacion').append(codigo);
}