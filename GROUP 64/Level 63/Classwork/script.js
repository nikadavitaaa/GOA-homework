
const title = document.getElementById("h1");
const nameInput = document.getElementById("nameInput");

function updateTitle() {
    const name = nameInput.value;
    title.textContent = "Hello " + name;
}
