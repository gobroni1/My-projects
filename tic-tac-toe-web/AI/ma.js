// Select all the squares in the game
const squares = document.querySelectorAll('.square');

// URLs for the X and O images
const xImage = 'Picture1.png'; // Replace with the actual path to the X image
const oImage = 'Picture2.png'; // Replace with the actual path to the O image

// Loop through each square to add event listeners
squares.forEach(square => {
    let content = '';  // Track the current content of the square

    // Left-click event to place O
    square.addEventListener('click', () => {
        if (content === 'O') {
            content = '';
            square.querySelector('.symbol').src="Picture3.png";  // Clear the image
        } else {
            content = 'O';
            square.querySelector('.symbol').src = oImage;  // Set O image
        }
    });

    // Right-click event to place X
    square.addEventListener('contextmenu', (event) => {
        event.preventDefault(); // Prevent the context menu from appearing

        if (content === 'X') {
            content = '';
            square.querySelector('.symbol').src="Picture3.png";  // Clear the image
        } else {
            content = 'X';
            square.querySelector('.symbol').src = xImage;  // Set X image
        }
    });
});
