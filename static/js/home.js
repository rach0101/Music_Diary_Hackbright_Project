'use strict';

$('#login').on('submit', (event) => {
    event.preventDefault();

    const data = {"username":$("#username").val(), "password": $("#password").val()}

    $.post("/login", data , (res) => {
        location.href = res["url"];
    });
});
