'use strict';

$('#create_account').on('submit', (event) => {
    if($('#username').val() == "" || $('#password').val() == "") {
        alert("Please fill in all of the required fields.");
        event.preventDefault();
    }

    else {
        $('#create_account').submit();
    }
});