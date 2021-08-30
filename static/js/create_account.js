'use strict';

$('#create_account').on('submit', (event) => {
    if($('#username').val() == "" || $('#password').val() == "" || 
        $('#spotify_username').val() == "" || $('#token').val() == "") {
        alert("Please fill in all of the required fields.");
        event.preventDefault();
    }

    else {
        $('#create_account').submit();
    }
});