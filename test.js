var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(xmlHttp.responseText);
}

httpGet('https://www.orce.uni.edu.pe/fotosuni/006020180125F.jpg');