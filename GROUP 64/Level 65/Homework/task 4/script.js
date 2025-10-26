const teacher = {
    name: "Anna",
    subject: "Mathematics",
    experience: 5,

    greet() {
        alert("Hello, I teach " + this.subject);
    }
};

const button = document.getElementById("greetBtn");

button.onclick = function() {
    teacher.greet();
};