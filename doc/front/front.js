
// set good width for the footer
window.onload = function(event) {
    headerFooterWidth();
}

window.onresize = function(event) {
    headerFooterWidth();
};

function headerFooterWidth(){
    var mainWidth = document.getElementsByClassName('main-div')[0].offsetWidth;
    document.getElementsByTagName('header')[0].style.width = mainWidth + "px";
    document.getElementsByTagName('footer')[0].style.width = mainWidth + "px";
    document.getElementById('papy').style.width = (mainWidth/6) + "px";
    var papyHeight = document.getElementById('papy').height
    document.getElementById('virgule-bulle').style.marginTop = (papyHeight / 3) + "px";

}
