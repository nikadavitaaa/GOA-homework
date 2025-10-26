let numbers = [10, 20, 30, 40, 50, 60];

// Pop - შლის მასივის ბოლო ელემენტს და აბრუნებს მას
let last = numbers.pop();
console.log(last);
console.log(numbers);

// Shift - შლის პირველ ელემენტს და აბრუნებს მას
let first = numbers.shift();
console.log(first);
console.log(numbers);

// Unshift - ამატებს ახალ ელემენტებს მასივის დასაწყისში და აბრუნებს მასივს
let newLength = numbers.unshift(5);
console.log(newLength);
console.log(numbers);

// Slice - ქმნის მასივის ასლს და არ ცვლის ორიგინალს
let sliced = numbers.slice(1, 3);
console.log(sliced);
console.log(numbers);

// Splice - შლის ან ამატებს ელემენტებს მასივში ადგილზევე
numbers.splice(2, 1, 99);
console.log(numbers);

// indexOf - ეძებს მითითებული ელემენტის ინდექსს, თუ ვერ იპოვა, აბრუნებს -1
let index = numbers.indexOf(99);
console.log(index);

// lastIndexOf - პოულობს ელემენტის გამეორების ინდექსს
numbers.push(20);
console.log(numbers);
let lastIndex = numbers.lastIndexOf(20);
console.log(lastIndex);

// includes - ამოწმებს არის თუ არა ელემენტი მასივში, თუ არის, აბრუნებს true-ს ხოლო თუ არა, false
console.log(numbers.includes(40));
console.log(numbers.includes(100));

// find - პოულობს პირველ ელემენტს, რომელიც აკმაყოფილებს პირობას
let found = numbers.find(num => num > 30);
console.log(found);

// findIndex - პოულობს პირველ ელემენტს, რომელიც აკმაყოფილებს პირობას და აბრუნებს მის ინდექსს.
let foundIndex = numbers.findIndex(num => num > 30);
console.log(foundIndex);
