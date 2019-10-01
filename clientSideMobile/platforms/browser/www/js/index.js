function login() {
    var location = '';
    var user;
    var passwd;
    user = document.iAccInput.user.value
    passwd = document.iAccInput.passwd.value
    if (user == 'admin' && passwd == 'admin') {
        location = ("myrobot.html");

    } else alert('verifier votre login et  pass');

    this.location.href = location;

}