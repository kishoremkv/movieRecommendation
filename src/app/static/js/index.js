$(document).ready(function () {

    $("#signout_button").click(function() {
       console.log("signer out");
       window.location.href = '/logout';
   });

   $("#recalib_button").click(function() {
    console.log("signer out");
    window.location.href = '/calibrate';
});

});


