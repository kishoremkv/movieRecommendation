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
    dialog.showModal();

    $(".login-cover").show();

});


