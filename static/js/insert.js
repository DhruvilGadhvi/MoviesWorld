$(document).ready(function () {
    $.post("/polls/", function (response) {
        // alert(response);
        console.log(response);
        // $("#img0").attr('src', 'https://image.tmdb.org/t/p/w500/' + (response.results[4].poster_path)).height(250).width(250)
        // $("#original_title0").append(response.results[4].original_title)
        // $("#popularity0").append(response.results[4].popularity)
        // $("#overview0").append(response.results[4].overview)

        //Appending
        $.each(response.movie_data, function (index, value) {
            // console.log(value.original_title);
            // console.log(value.popularity);
            // console.log(value.overview);

            // var img=$(this).attr('src', 'https://image.tmdb.org/t/p/w500/' + (response.results[index].poster_path));
            // console.log(img[0])
            // console.log(value.poster_path)
            $(".container").append(`<div class="card" style="width: 18rem;">
            <img class="card-img-top" id="img" src="https://image.tmdb.org/t/p/w500//${value.poster_path}" alt="Card image cap"></img>
            <div class="card-body">
                <h5 class="card-title" id="original_title">${value.title}</h5>
                <h6 class="card-title" id="popularity">popularity : ${value.popularity} </h6>
                <p class="card-text" id="overview">${value.overview}</p>
            </div>
        </div>`)
        });
    });

});