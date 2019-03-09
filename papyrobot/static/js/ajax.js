const questionInput =  document.getElementsByClassName("question")[0]
questionInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        document.getElementsByClassName("loading")[0].style.display = 'block';
        // setTimeout(console.log('wait'), 1000);
        // console.log('Appuie sur Enter');
        // console.log(questionInput.value);
        var req = new XMLHttpRequest();
        req.open("GET", "/ajax?question=".concat(questionInput.value));
        req.addEventListener("load", function () {

            console.log(req.responseText);
        });
        req.send(null);
        document.getElementsByClassName("loading")[0].style.display = 'none'
    }
});

questionInput.value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"