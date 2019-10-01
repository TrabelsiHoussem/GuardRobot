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
        xmlhttp.open("POST", ipadress + "/", true);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.send("mode=" + mode);

    } else {
        x.disabled = false;
        document.getElementById("reculee").style.opacity = 1;
        y.innerHTML = "Mode manuelle";
        var mode = "manuelle"
        var xmlhttp = new XMLHttpRequest(); 
        xmlhttp.open("POST", ipadress + "/", true);
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
    xmlhttp.open("POST", ipadress + "/", true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send("direction=" + direction);
}