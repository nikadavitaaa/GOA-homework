function checkBirthYear() {
    const birthYear = Number(document.getElementById("yearInput").value);
    const currentYear = new Date().getFullYear();
    const age = currentYear - birthYear;

    const message = age < 18 ? "Minor" : "Adult";

    document.getElementById("ageMsg").textContent = message;
}