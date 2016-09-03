$(document).ready(function(){

    primeiraSelecao = function(){
        $('.selecao-periodo:first').addClass('ativo');
    };

    $('.selecao-periodo').click(function(){
        var _id = $(this).attr('id');

        // Ajusta seleção
        $('.selecao-periodo.ativo').removeClass('ativo');
        $(this).addClass('ativo');

        // Exibe as linhas correspondentes
        if(_id != ""){
            $('.disciplina:not(' + _id +')').hide();
            $('.disciplina.'+_id).show();
        }else{
            $('.disciplina').show();
        }
    });

    primeiraSelecao();
});
