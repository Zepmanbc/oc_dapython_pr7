var mapNumber = 0;

function putDataInTextArea(data){
    document.getElementById('textArea').innerHTML = '';
    if (data['keywords']){
        mapNumber++;
        // var question = "Tu cherches où se trouve " + data['keywords'] + "?";
        var answer = "Bien sur mon poussin, voici l'adresse : " + data['formatted_address'];
        var story = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " + data['story']
        
        // document.getElementById('textArea').innerHTML += '<p>' + question + '</p>';
        document.getElementById('textArea').innerHTML += '<p>' + answer + '</p>';
        document.getElementById('textArea').innerHTML += '<div class="map_container"><div id="map'+mapNumber+'" class="map"></div></div>'
        document.getElementById('textArea').innerHTML += '<p>' + story + '</p>';

        // initMap
        var lat_lng = {lat: data['location'][0], lng: data['location'][1]};
        var map = new google.maps.Map(document.getElementById('map'+mapNumber), {
            center: lat_lng,
            zoom: 14
        });
        var marker = new google.maps.Marker({position: lat_lng, map: map});
    } else {
        document.getElementById('textArea').innerHTML += "<p>Je n'ai pas bien compris ta question ou alors je ne connais pas ce lieu, essaie encore !</p>";
    }
    
}

function putInHistory(speaker, data){
    if(speaker == "userSpeak"){classText = " text-right";}else{classText="";};
    dataFormated = '<div class="col-12'+classText+'"><div class="' + speaker + '">' + data + '</div></div>'
    document.getElementById("history").innerHTML += dataFormated;
    window.scrollTo(0,document.body.scrollHeight);
}

const questionInput =  document.getElementsByClassName("question")[0]
questionInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter" && questionInput.value) {
        // show loading div
        document.getElementsByClassName("loading")[0].style.display = 'block';
        var req = new XMLHttpRequest();
        req.open("GET", "/ajax?question=".concat(questionInput.value));
        req.addEventListener("load", function () {
            var data = JSON.parse(req.responseText);
            console.log(req.responseText);
            papyText = document.getElementById('textArea').innerHTML
            putDataInTextArea(data);
            console.log("loaded...");
            // hide loading div
            document.getElementsByClassName("loading")[0].style.display = 'none';
            
            // put previous papy speech (TextArea innerHTML) in history div
            putInHistory('papySpeak', papyText);
            // put user speech (input value) in history div
            putInHistory('userSpeak', questionInput.value);
            // clear input
            questionInput.value = '';
        });
        req.send(null);
        console.log("loading...");
        
    }
});


