$(function(){
    $("#echo_get").click(function() {
        $.get( "/api/echo?msg=" + $("#txt_field").val(), function( data ) {
            $( "#ajax_get_response" ).html( data["text"] );
        });
    });

    $("#echo_post").click(function() {
        $.post( "/api/echo", { msg : $("#msg_field").val() }, function( data ) {
            $( "#ajax_post_response" ).html( data["text"] );
        });
    });

}); 

