
const openBtn = document.getElementById("addE");

openBtn.addEventListener("click", ()=> {
    modal.classList.add("open");
    let newdiv = document.createElement("div");
    
    newdiv.style.width = "350px";
    newdiv.style.height= "500px";
    newdiv.style.backgroundColor = "#e35ffd70";
    newdiv.style.borderRadius ="8px";
    newdiv.style.display = "flex";
    newdiv.style.flexDirection = "column";

    let title = document.createElement("h2");
    title.textContent ="new event";
    title.style.textAlign = "center";
    title.style.marginTop = "20px";
    title.style.color = "white"

    let tasks = document.createElement("ul");
    tasks.style.color= "white";
    tasks.style.marginLeft = "30px";
    tasks.style.marginTop = "20px";


    let addtask = document.createElement("button");
    addtask.style.width = "125px";
    addtask.style.height = "50px";
    addtask.textContent = "add task";
    addtask.style.marginTop = "auto";
    
    theTitle = title;

    //selection logit
    newdiv.addEventListener("click", () => {
        if (selectedDiv !== newdiv) {
            if (selectedDiv) {
                selectedDiv.style.border = ''; 
            }
            selectedDiv = newdiv;
            selectedDiv.style.border = '1px solid purple';  
        }
    });
    

    addtask.addEventListener("click", () => {
        
        modal2.classList.add("open2");
    });

    //selection logic

    newdiv.appendChild(title);
    newdiv.appendChild(tasks);
    newdiv.appendChild(addtask);

    document.getElementById("main-screen").appendChild(newdiv);    
});