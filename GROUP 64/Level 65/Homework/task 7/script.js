function cubeNumber() {
    const num = Number(document.getElementById("numInput").value);
    const cubed = num ** 3;
    
    document.getElementById("numOut").textContent = cubed;
}