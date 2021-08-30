'use strict';

$('#login').on('submit', (event) => {
    

    if($('#username').val() == "" || $('#password').val() == "") {
        alert("Please enter both username and password.");
        event.preventDefault();
    }
    else {
        $('#login').submit();
    }
});