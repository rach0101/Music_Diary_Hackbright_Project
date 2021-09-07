'use strict';

$('#login').on('submit', (event) => {
    event.preventDefault();

    const data = {"username":$("#username").val(), "password": $("#password").val()}
// TODO hand reroute on the backend
    $.post("/login", data , (res) => {
        location.href = res["url"];
    });
    
});
