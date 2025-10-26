function NumberInfo(number) {
    this.number = number;
    this.even = number % 2 === 0;
}

let numbers = [];

for (let i = 1; i <= 10; i++) {
    let numObj = new NumberInfo(i);
    numbers.push(numObj);
}

console.log(numbers);
