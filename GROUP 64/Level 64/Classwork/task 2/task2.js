const button = document.getElementById("sub")

button.onclick = function () {
    
    const answer = confirm("Are you sure?")

    console.log(answer)
}