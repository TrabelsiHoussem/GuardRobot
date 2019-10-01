/* MonImageP = new Array(6);
for (i = 0; i < 7; i++) {
    MonImageP[i] = new Image();
    MonImageP[i].src = "static/potard" + i + ".gif";
} */

/* 
function fpotard(x) {
    if (x == 'undefined')  { 
        return; 
    }
    //requete Http pour le serveur
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function()  { 
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)    {
            document.getElementById('potardgif').src = MonImageP[xmlhttp.responseText].src;   
        }
    }
    xmlhttp.open("POST", "/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("vitesse=" + x);
} */
function desactivee() {
    var x = document.getElementById("avance");
    var y = document.getElementById("mode");
    if (x.disabled === false) {
        x.disabled = true;
        document.getElementById("avancee").style.opacity = 0.6;
        y.innerHTML = "Mode automatique";
    } else {
        x.disabled = false;
        document.getElementById("avancee").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
    }
    var x = document.getElementById("gauche");
    if (x.disabled === false) {
        x.disabled = true;
        document.getElementById("gauchee").style.opacity = 0.6;
        y.innerHTML = "Mode automatique";
    } else {
        x.disabled = false;
        document.getElementById("gauchee").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
    }

    var x = document.getElementById("stop");
    if (x.disabled === false) {
        x.disabled = true;
        document.getElementById("stopp").style.opacity = 0.6;
        y.innerHTML = "Mode automatique";
    } else {
        x.disabled = false;
        document.getElementById("stopp").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
    }
    var x = document.getElementById("droite");
    if (x.disabled === false) {
        x.disabled = true;
        document.getElementById("droitee").style.opacity = 0.6;
        y.innerHTML = "Mode automatique";
    } else {
        x.disabled = false;
        document.getElementById("droitee").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
    }
    var x = document.getElementById("recule");
    if (x.disabled === false) {
        x.disabled = true;
        document.getElementById("reculee").style.opacity = 0.6;
        y.innerHTML = "Mode automatique";
        var mode = "auto"
        var xmlhttp = new XMLHttpRequest(); 
        xmlhttp.open("POST", "http://192.168.1.7:8080/", true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send("mode=" + mode);

    } else {
        x.disabled = false;
        document.getElementById("reculee").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
        var mode = "manuelle"
        var xmlhttp = new XMLHttpRequest(); 
        xmlhttp.open("POST", "http://192.168.1.7:8080/", true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send("mode=" + mode);
    }
}

function toggleSidebar(ref) {
    ref.classList.toggle('active');
    document.getElementById('sidebar').classList.toggle('active');
}

function move(direction) {
    if (direction == 'undefined')  { 
        return; 
    }
    //requete Http pour le serveur
    var xmlhttp = new XMLHttpRequest(); 
    xmlhttp.open("POST", "http://192.168.1.7:8080/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("direction=" + direction);
}





/* function rotate(orientation) {
    if (orientation == 'undefined')  { 
        return; 
    }
    //requete Http pour le serveur
    var xmlhttp = new XMLHttpRequest(); 
    xmlhttp.open("POST", "/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("orientation=" + orientation);
} */

/* function outputUpdate(vol) {
    if (vol == 'undefined')  { 
        return; 
    }
    var xmlhttp = new XMLHttpRequest(); 
    xmlhttp.open("POST", "/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("vol=" + vol);

    document.querySelector('#volume').value = vol * 1.8;

} */

/* function myFunction(event) {


    switch (event.keyCode) {
        case 122: // ←
            move('avant');

            break;
        case 100: // ↑
            move('droite');

        case 113: // →
            move('gauche');

        case 115: // ↓
            move('arriere')

            event.preventDefault();
            return false;
    }
} */

/*jQuery(document).ready(function() {
            function load() {

                jQuery.get("/se", function(result) {

                    jQuery("#text11").text(result);

                    



                    if (parseInt(result) == 0) {

                        jQuery("#monImage").attr("src", "static/green.png");

                    } else {

                        jQuery("#monImage").attr("src", "static/red.png");

                    }

                    setTimeout(load, 1000);

                    



                });

            }

            load();
 });*/