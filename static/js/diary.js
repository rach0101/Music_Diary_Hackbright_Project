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
            
            for (const element of response){
                console.log(element.name);
                $('#search_results').append(
                                `<div> 
                                    <img src="${element.album.images[2].url}">
                                    <a href="${element.external_urls.spotify}">${element.name} </a>
                                </div>`);
            }; 
        });
    });
});