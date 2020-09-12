$(document).ready(function () {

		$('#id_afiliado').on('change', function () {

			console.log("change");

			var id_afiliado = $('#id_afiliado').val();

			console.log(id_afiliado);

			if(id_afiliado == 'N'){
				$("#id_nroAfiliado").attr('disabled',true);
			}else{
				$("#id_nroAfiliado").removeAttr('disabled');
			}
		});
}