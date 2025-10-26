const tablet = {
    brand: "Apple",
    model: "iPad Air",
    color: "Silver",

    playMusic() {
        console.log("Playing music...");
    }
};

const button = document.getElementById("musicBtn");

button.onclick = function() {
    tablet.playMusic();
};