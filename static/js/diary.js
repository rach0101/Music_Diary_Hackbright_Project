'use strict';

// Can use JS to render API search results on the front end
// on submit do get request using ajax
// give form an id
$(document).ready( () => {
    $('#music_search').on('submit', (event) => {
        // Display results of song search on submit
        event.preventDefault();
        
        const data = {"name": $("#music_search_input").val()};

        $.post('/diary_api.json', data, (response) => {
            // Loop through JSON response data from Spotify API
            // Append 5 songs with links and album art to the DOM
            for (const element of response){
                console.log(element.name);
                $('#search_results').append(
                                `<div>
                                    <input type="radio" name="select_song">
                                    <label id="${element.uri}"> 
                                        <img src="${element.album.images[2].url}">
                                        <a href="${element.external_urls.spotify}">${element.name} </a>
                                    </label>
                                    
                                </div>`);
                                
            };  
            $('#search_results').append(
                `<div>
                    <input type="submit" value="post song">
                </div>`);  
        });
    });
});


