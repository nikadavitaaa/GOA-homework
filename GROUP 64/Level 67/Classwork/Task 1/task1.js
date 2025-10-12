function calculateGrade() {
    let examPoints = prompt("შეიყვანე გამოცდის ქულა (0-100): ");
    let activityPoints = prompt("შეიყვანე აქტიურობის ქულა (0-100): ");

    examPoints = Number(examPoints);
    activityPoints = parseInt(activityPoints);

    let totalPoints = examPoints + activityPoints;

    let finalGrade;
    if (totalPoints >= 90 && totalPoints <= 100) {
        finalGrade = "A";
    } else if (totalPoints >= 80 && totalPoints < 90) {
        finalGrade = "B";
    } else if (totalPoints >= 70 && totalPoints < 80) {
        finalGrade = "C";
    } if (totalPoints >= 50 && totalPoints < 70) {
        finalGrade = "D";
    } if (totalPoints >= 30 && totalPoints < 50) {
        finalGrade = "E";
    } else {
        finalGrade = "F";
    }
    alert("თქვენი ჯამური ქულაა: " + totalPoints + " → შეფასება: " + finalGrade);
}
