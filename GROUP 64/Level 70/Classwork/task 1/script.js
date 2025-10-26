// ობიექტი — ეს არის მონაცემთა სტრუქტურა, რომელიც აერთიანებს მონაცემებს

// ობიექტის კონსტრუქტორი — ფუნქცია, რომლის დახმარებითაც შეგვიძლია შევქმნათ მრავალი მსგავსი ობიექტი.
function Task(title, desc, state, deadline) {
    this.title = title;
    this.desc = desc;
    this.state = state;
    this.deadline = deadline;
    
    this.complete = function () {
        this.state = "completed";
        console.log(` Task "${this.title}" is now completed!`);
    };
}
