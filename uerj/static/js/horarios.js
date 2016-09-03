$(document).ready(function(){

    getDia = function(){
		var hoje = new Date();
		var dia = hoje.getDay();
		switch(dia){
			case 0: return "Seg"; //Domingo exibe os horários de segunda
			case 1: return "Seg";
			case 2: return "Ter";
			case 3: return "Qua";
			case 4: return "Qui";
			case 5: return "Sex";
			case 6: return "Sab";
		}
	};

    primeiraSelecao = function(){
        var dia = getDia();
        $('.table#' + dia).show();
        $('.seletor-dia#' + dia).addClass('ativo');
    };

    $('.seletor-dia').click(function(){
        var _id = $(this).attr('id');
        // Ajusta o item selecionado da lista
        $('.seletor-dia.ativo').removeClass('ativo');
        $(this).addClass('ativo');
        // Exibe a tabela correspondente
        $('.table:visible').hide();
        $('.table#' + _id).show();
    });

    primeiraSelecao();
});
