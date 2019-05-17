$(document).ready( async function() {
    const BASE_URL = "";
    const $picList = $("#pic_list");

    let cupcakes = await $.get(`${BASE_URL}/cupcakes`);

    for(cupcake of cupcakes.response){
        $picList.append(
            `<div>
                <img src="${ cupcake.image }">
                <p>Flavor: ${ cupcake.flavor }</p>
                <p>Size: ${ cupcake.size }</p>
                <p>Rating: ${ cupcake.rating }</p>
            </div>`);
    }

    $("#search_form").on("submit", async function(evt) {
        evt.preventDefault();

        let type = $("#type").val();
        let term = $("#search_term").val();

        let response = await $.get(`${BASE_URL}/cupcakes/search?type=${type}&term=${term}`);

        $picList.empty();

        for(cupcake of response.response){
            $picList.append(
                `<div>
                <img src="${ cupcake.image }">
                <p>Flavor: ${ cupcake.flavor }</p>
                <p>Size: ${ cupcake.size }</p>
                <p>Rating: ${ cupcake.rating }</p>
                </div>`);
        }

    });

    $("#new_cupcake_form").on("submit", async function(evt) {
        evt.preventDefault();

        let newCupcake = {
            flavor: $("#flavor").val(),
            size: $("#size").val(),
            rating: $("#rating").val(),
            image: $("#image").val() || null
        };

        let response = await $.ajax({
            method: "POST",
            url: `${BASE_URL}/cupcakes`,
            contentType: "application/json",
            data: JSON.stringify(newCupcake)
        });

        $picList.append(
        `<div>
            <img src="${ response.response.image }">
            <p>Flavor: ${ response.response.flavor }</p>
            <p>Size: ${ response.response.size }</p>
            <p>Rating: ${ response.response.rating }</p>
        </div>`);

    });

    $("#update_cupcake_form").on("submit", async function(evt) {
        evt.preventDefault();

        let updatedCupcake = {
            flavor: $("#flavor").val(),
            size: $("#size").val(),
            rating: $("#rating").val(),
            image: $("#image").val() || null
        };

        let cupcakeId = $("#id").val()

        await $.ajax({
            method: "PATCH",
            url: `${BASE_URL}/cupcakes/${cupcakeId}`,
            contentType: "application/json",
            data: JSON.stringify(updatedCupcake)
        });

        location.reload();

    });
});

