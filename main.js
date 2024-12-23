const desk = {
    item1: "book",
    item2: "glass bottle",
    item3: "wallet"
};


const len = Object.len(desk);

for (let i = 0; i < len.length; i++) {
    let len = len[i]
    console.log(len);
    console.log(desk[len]);
}

