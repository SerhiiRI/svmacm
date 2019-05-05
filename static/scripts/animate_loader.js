
var pos = 0;
var opacity = 1.0;
var finish = 0;

function StartLoading() {
    var elem = document.getElementById("animate-loading-line");
    var id = setInterval(frame, 5);

    function frame() {
        if (finish == 1 || pos >= document.documentElement.clientWidth - 100) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.width = pos + "px";
        }
    }
}

function KillLoading() {
    var elem = document.getElementById("animate-loading-line");
    finish = 0;
    var ddd = setInterval(hides, 40);

    function hides() {
        if ((pos * 100 / (document.documentElement.clientWidth)) > 80) {
            if (opacity == 0.1) {
                clearInterval(ddd);
                elem.style.opacity = 1;
                elem.style.width = "0px";
                pos = 0;
                opacity = 1.0;
            } else {
                opacity -= 0.1;
                elem.style.opacity = opacity;
            }
        }
    }

    var fff = setInterval(fish, 1);
    function fish() {
        if (pos >= document.documentElement.clientWidth) {
            clearInterval(fff);
            clearInterval(ddd);
            elem.style.opacity = 1;
            elem.style.width = "0px";
            pos = 0;
            opacity = 1.0;
        } else {
            pos += 2;
            elem.style.width = pos + "px";
        }
    }
}