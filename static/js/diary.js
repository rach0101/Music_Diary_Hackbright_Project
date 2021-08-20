'use strict';

// Can use JS to render API search results on the front end
// on submit do get request using ajax
// give form an id
$(document).ready( () => {
    $('#music_search').on('submit', (event) => {
        event.preventDefault();
        
        const data = {"name": $("#music_search_input").val()};

        $.post('/diary_api.json', data, (response) => {
            const update = "";
            
            for(const element in response) {
                update.concat("<div> ${element.name} </div>");
                $('#search_results').html(update);
            };  
        });
    });
});