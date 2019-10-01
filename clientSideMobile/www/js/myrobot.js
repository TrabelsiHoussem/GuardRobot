function move(direction) {
    if (direction == 'undefined') 
        return; 

    //requete Http pour le serveur
    var xmlhttp = new XMLHttpRequest(); 
    xmlhttp.open("POST", ipadress + "/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("direction=" + direction);
}