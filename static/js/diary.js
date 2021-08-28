'use strict';

$(document).ready(() => {
    // Create an empty dictionary to help handle 
    // song selection from search
    let song_data = {};
    
    // Event listener for submitting song search form in diary.html
    $('#music_search_form').on('submit', (event) => {
        
        event.preventDefault();
       
        // Empty DOM of any old search results and refresh with new search
        $('#list_of_search_results').empty(); 
        
        if($('#music_search_input').val() == ""){
            alert("Please search for a song.");
        };
        // Create key value pair for name: "song search input"
        const data = { "name": $("#music_search_input").val() };
        
        // Send data (key: value pair) to the server as a post request
        // and retrieve Spotify API response data from server
        $.post('/diary_api.json', data, (response) => {
          
            // Create empty song search dict for saving 
            // data about a song that will be used in posts
            song_data = {};
            
            // Loop through JSON response data from Spotify API
            // add each song to the song_data dictionary
            for (const element of response) {

                song_data[element.id] = {
                    'name': element.name,
                    'url': element.external_urls.spotify,
                    'img': element.album.images[2].url,
                    'id': element.id
                };
                // $('#list_of_search_results').style.display = "none";

                // Append the 5 songs with links and album art to the DOM
                // as clickable radio buttons
                $('#list_of_search_results').append(
                    // Set song ID to form input value            
                    `<div id="radio_selection">
                        <input type="radio" name="select_song" value="${element.id}">
                        <label id="${element.uri}" for="${element.name}"> 
                            <img src="${element.album.images[2].url}">
                            <a href="${element.external_urls.spotify}">${element.name} </a>
                        </label>            
                    </div>`);
            };
            
                $('#list_of_search_results').append(
                `<div>
                    <input type="submit" value="post song">
                </div>`);
        });
    });
    
    // Write post request that sends radio selection to server
    
     // -------------------------------------
    // ----------Testing code here----------
    // -------------------------------------
    // $('input[type=radio]').on('change', (event) => {

    // }) 
     
    $('#list_of_search_results').on('submit', (event) => {
       
       
        // Serialize form to an array to grab song id
        // array only displays one result which is the selected song
        let selected_song_id = $('#list_of_search_results').serializeArray()[0].value;
       
        event.preventDefault();
        
        // Alert user if no song is selected from search results
         if ($('input[name=default]:checked').length){
            // do nothing if radio is checked
            // {};
            alert("you DID NOT check a radio button");
        };
        //     else {
        //         console.log("NOOOOO")
        //         alert("you did not checked a radio button");
        // };
        
        // Remove list of radio buttons from search results
        $('#list_of_search_results').empty();

        // Remove submit button and search box from song search form
        $('#music_search_form').empty();

        
        // if($('#music_search_input').val() == ""){
        //     alert("Please search for a song.");

        // Lookup song info using song id from the serialized array
        let post_song_data = song_data[selected_song_id];

        // Populate a form at the top of the page so the user can make 
        // diary entry and send data to the server
        $('#song_data').append(
            `<div>
                <input type="hidden" name="posted_song" value="${post_song_data.id}">
                <label id="${post_song_data.id}" for="${post_song_data.name}"> 
                    <img src="${post_song_data.img}">
                    <a href="${post_song_data.url}">${post_song_data.name} </a>
                </label>            
            </div>`
        );
        // Update each hidden inputon on the save_song_to_databse form at the top of 
        // the diary page.
        // Each hidden input tag's "value" is updated using data from post_song_data dict 
        // then the server grabs this data and saves to the database 
        // at the @app.route /save_song_to_database
        $('#song_name').val(post_song_data.name);
        $('#song_url').val(post_song_data.url);
        $('#song_img').val(post_song_data.img);
        $('#song_id').val(post_song_data.id);
    });
});




