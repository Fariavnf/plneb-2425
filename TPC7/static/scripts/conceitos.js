function delete_term(termo){

    $.ajax('/conceitos/' + termo, {
        type: 'DELETE',
        success: function(data){
            console.log(data)
            if(data["success"]){
                window.location.href = data['redirect_url'];
            }
        },
        error: function(error){
            //adicionar mensagem
            console.log(error)
        }
    })
}


$(document).ready( function () {
    $('#myTable').DataTable({search: {
        regex: true
    }});
} );


