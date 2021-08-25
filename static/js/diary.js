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
            
            // empty song search dict
            song_data = {};

            for (const element of response) {
                console.log(element);

                song_data[element.id] = {
                    'name': element.name,
                    'url': element.external_urls.spotify,
                    'img': element.album.images[2].url,
                    'id': element.id
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
        // serialize form to an array to grab song id
        let selected_song_id = $('#search_results').serializeArray()[0].value;
        
        console.log(selected_song_id);

        event.preventDefault();

        // remove children of search results
        $('#search_results').empty();

        // grab id from serialzed array and lookup song info
        let post_song_data = song_data[selected_song_id];
        console.log(post_song_data);

        // populate a form at the top of the page so the user can make 
        // diary entry
        $('#song_data').append(
            `<div>
                <input type="hidden" name="posted_song" value="${post_song_data.id}">
                <label id="${post_song_data.id}" for="${post_song_data.name}"> 
                    <img src="${post_song_data.img}">
                    <a href="${post_song_data.url}">${post_song_data.name} </a>
                </label>            
            </div>`
        );
        // update hidden values on form to send to server
        $('#song_name').val(post_song_data.name);
        $('#song_url').val(post_song_data.url);
        $('#song_img').val(post_song_data.img);
        $('#song_id').val(post_song_data.id);
    }); 
});




