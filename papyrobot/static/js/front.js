
// set good width for the footer
window.onload = function(event) {
    resizeAll();
    // Hide loading page when windows is loaded
    document.getElementsByClassName("loading")[0].style.display = 'none';
}

window.onresize = function(event) {
    resizeAll();
};

function resizeAll(){
    var mainWidth = document.getElementsByClassName('main-div')[0].offsetWidth;
    // set good width to header and footer
    document.getElementsByTagName('header')[0].style.width = mainWidth + "px";
    document.getElementsByTagName('footer')[0].style.width = mainWidth + "px";
    // set 2/12 width to papy pic
    document.getElementById('papy').style.width = (mainWidth/6) + "px";
    var papyHeight = document.getElementById('papy').height
    // set vertical position of virgule-bulle according to papy pic size
    document.getElementById('virgule-bulle').style.top = (papyHeight * 0.4) + "px";
    // set height for papy pic div
    document.getElementById("papy-div").style.height = papyHeight + 30 + "px";;
    // set loading img in the center
    loadingHeight = document.querySelector(".loading img").height
    document.querySelector(".loading img").style.marginTop = (screen.height / 2 - loadingHeight) + "px";
}