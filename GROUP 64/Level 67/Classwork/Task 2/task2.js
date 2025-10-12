const choiceDiv = document.getElementById("userchoice");
const playerScoreP = document.getElementById("playerScoreP");
const compScoreP = document.getElementById("compScoreP");
const compChoiseP = document.getElementById("compChoiceP");
const resultDisplay = document.getElementById("gameRes")
const options = ["Rock", "Paper", "Scissors"]  

let playerScore = 0;
let computerScore = 0;

function gameLogic(clickEvent) {
    let randomIndex = Math.floor(Math.random() * 3)
    let computerChoice = options[randomIndex]

    let playerChoice = clickEvent.target.textContent

    compChoiseP.textContent = `Computer choice: ${computerChoice}`
    
    if ((computerChoice === "Rock" && playerChoice === "Scissors") || (computerChoice === "Paper" && playerChoice === "Rock") || computerChoice === 'Scissors' && playerChoice === "Paper") {
        console.log("Computer wins!")

    }
}

choiceDiv.onclick = gameLogic
