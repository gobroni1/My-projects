let squares = document.querySelectorAll("p");

squares.forEach((sq) => {
    let content = "";

    sq.addEventListener("contextmenu", (event) => {
        event.preventDefault(); 

        if (content === "X") {
            content = "";
        } else {
            content = "X";
        }
        
        sq.textContent = content; 
    });
   
    sq.addEventListener("click", (event) => {
        event.preventDefault(); 
        if (content === "O") {
            content = "";
        } else {
            content = "O";
        }

        sq.textContent = content;
    });
});






