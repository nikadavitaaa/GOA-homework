const laptop = {
    brand: "Dell",
    RAM: "16GB",
    price: 1200,

    turnOn() {
        console.log("Laptop is on");
    }
};

const button = document.getElementById("laptopBtn");

button.onclick = function () {
    laptop.turnOn();
};

/* 
    Property: ობიექტის მახასიათებელი, მაგალითად brand, RAM, price
    Method: ობიექტის ფუნქცია, ამ შემთხვევაში - turnOn()
    ობიექტი HTML ელემენტზე მოქმედებს method-ის გამოძახებით
*/