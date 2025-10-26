function checkLength() {
    const word = document.getElementById("wordInput").value;
    document.getElementById("wordOut").textContent = "Number of characters: " + word.length;
}