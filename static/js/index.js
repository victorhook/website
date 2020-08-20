$(document).ready(function() {

    console.log();

    const NAVBAR = ['skills', 'projects', 'photography', 'about', 'website', 'contact'];
    var url = window.location.pathname;
    url = url.slice(1, url.length);

    if (url.length > 0) {
        for (var i = 0; i < NAVBAR.length; i++) {
            if (NAVBAR[i].startsWith(url)) {
                let currentURL = $("#" + NAVBAR[i]);
                currentURL.css("color", "rgba(255,255,255,.8)");
                currentURL.css("font-weight", "bold");
                break;
            }
        }
    }

 });
