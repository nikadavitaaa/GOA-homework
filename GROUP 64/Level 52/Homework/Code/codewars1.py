"https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python"

"Rock Paper Scissors!"

def rps(p1, p2):
    rules = {
        "scissors": "paper",
        "paper": "rock",
        "rock": "scissors"
    }
    
    if p1 == p2:
        return "Draw!"
    
    if rules[p1] == p2:
        return "Player 1 won!"
    return "Player 2 won!"