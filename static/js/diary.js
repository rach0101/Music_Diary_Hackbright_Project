'use strict';

// Can use JS to render API search results on the front end
// on submit do get request using ajax
// give form an id
$(document).ready(() => {

    let song_data = {};

    $('#music_search').on('submit', (event) => {
        // Display results of song search on submit
        event.preventDefault();

        const data = { "name": $("#music_search_input").val() };

        $.post('/diary_api.json', data, (response) => {
            // Loop through JSON response data from Spotify API
            // Append 5 songs with links and album art to the DOM
            // use ajax to 
            // use type = hidden and .serialize the form to get the correct data
            
            // empty song search dict
            song_data = {};

            for (const element of response) {
                console.log(element);

                song_data[element.id] = {
                    'name': element.name,
                    'url': element.external_urls.spotify,
                    'img': element.album.images[2].url
                };

                $('#search_results').append(
                    // make id the value            
                                `<div>
                                    <input type="radio" name="select_song" value="${element.id}">
                                    <label id="${element.uri}" for="${element.name}"> 
                                        <img src="${element.album.images[2].url}">
                                        <a href="${element.external_urls.spotify}">${element.name} </a>
                                    </label>            
                                </div>`);
            };
            $('#search_results').append(
                `<div>
                    <input type="submit" value="post song">
                </div>`);
            console.log(song_data);
        });
    });

    // Write post request that sends radio selection to server
    $('#search_results').on('submit', (event) => {
        // serialize form to an array to grab results
        console.log($('#search_results').serializeArray());

        event.preventDefault();

        // remove children of search results
        $('#search_results').empty();

        // grab id from serialzed array and lookup song info
        // populate a form at the top of the page so the user can make 
        // diary entry

        // this form will then post to the server
    }); 
});




