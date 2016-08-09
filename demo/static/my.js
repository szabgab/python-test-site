$(function(){
    $("#echo_get").click(function() {
        $.get( "/api/echo?msg=" + $("#txt_field").val(), function( data ) {
            $( "#response" ).html( data["text"] );
        });
    });
}); 

