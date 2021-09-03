'use strict';


$('#login').on('submit', (event) => {
    event.preventDefault();

    if($('#username').val() == "" || $('#password').val() == "") {
        
        alert("Please enter both a username and password");
    }

    else {
        const data = {"username":$("#username").val(), "password": $("#password").val()}

        $.post("/login", data , (res) => {
            location.href = res["url"];
        });
    }
});