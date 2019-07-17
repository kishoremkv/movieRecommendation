var docId;
var bal;
var bal;
/* UTIL */


function showSnackbar(message) {
    var snackbarContainer = document.querySelector("#snackbar");
    var data = {
        message: message,
        timeout: 2000
    };
    snackbarContainer.MaterialSnackbar.showSnackbar(data);
}


function isEmpty(str) {
    return (!str || 0 === str.length);
}
/* UTIL */

$(document).ready(function () {

    var dialog = document.querySelector('#login_dialog');
    if (!dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }
    // Now dialog acts like a native <dialog>.
    //dialog.showModal();

    $(".login-cover").hide();

    var gridItem = '<div class="mdl-cell mdl-cell--4-col"> <style> .demo-card-square.mdl-card { width: 320px; height: 320px; } .demo-card-square>.mdl-card__title { color: #fff; background: url("../assets/demos/dog.png") bottom right 15% no-repeat #46B6AC; } </style> <div class="demo-card-square mdl-card mdl-shadow--2dp"> <div class="mdl-card__title mdl-card--expand"> <h2 class="mdl-card__title-text">Update</h2> </div> <div class="mdl-card__supporting-text"> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenan convallis. </div> <div class="mdl-card__actions mdl-card--border"> <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect"> View Updates </a> </div> </div>';

    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);
    $("#movie_grid").append(gridItem);

});


