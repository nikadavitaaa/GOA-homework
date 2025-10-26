// stack
let a = 10;
let b = a;
b = 20;
console.log(a);

// heap
let user1 = { name: "Givi" };
let user2 = user1;
user2.name = "Luka";
console.log(user1.name);

// Memory leak - როდესაც ვერ იძებნება საკმარისი მეხსიერება, მეხსიერება იტვირთება და გადაივსება
function toDO() {
    toDO()

}