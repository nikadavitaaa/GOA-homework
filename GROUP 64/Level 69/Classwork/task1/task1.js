const dataBase = [];

const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const registerBtn = document.getElementById('registerBtn');

registerBtn.onclick = function() {
    const account = {
        name: nameInput.value,
        email: emailInput.value,
        password: passwordInput.value
    };

    dataBase.push(account);

    nameInput.value = '';
    emailInput.value = '';
    passwordInput.value = '';

};

printBtn.onclick = function() {
    console.log(dataBase);
};
