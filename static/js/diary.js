'use strict';

// Can use JS to render API search results on the front end
// on submit do get request using ajax
// give form an id
$(document).ready( () => {
    $('#music_search').on('submit', (event) => {
        event.preventDefault();
        
        const data = {"name": $("#music_search_input").val()};

        $.post('/diary_api.json', data, (response) => {
            console.log((response));
     
            console.log(response.name);
          
            $('#search_results').append(`<div> <a href="${response.external_urls.spotify}">${response.name} </a></div>`);
            
        });
    });
});