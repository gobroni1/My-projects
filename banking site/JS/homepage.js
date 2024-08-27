// homepage.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-auth.js";
import { getFirestore, getDoc, doc } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDx8olgefMrRcmsFmjAcK0TkcX3apwhjOU",
    authDomain: "internet-bank-d3531.firebaseapp.com",
    projectId: "internet-bank-d3531",
    storageBucket: "internet-bank-d3531.appspot.com",
    messagingSenderId: "924873151396",
    appId: "1:924873151396:web:9817d5d7814ce919802731"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const auth = getAuth();
const db = getFirestore();

onAuthStateChanged(auth, (user) => {
    if (user) {
        const docRef = doc(db, "users", user.uid);
        getDoc(docRef)
            .then((docSpan) => {
                if (docSpan.exists()) {
                    const userData = docSpan.data();
                    document.getElementById('loggedUserFName').innerText = userData.firstName;
                    document.getElementById('loggedUserLName').innerText = userData.lastName;
                    document.getElementById('loggedUserEmail').innerText = userData.email;
                    document.getElementById('card').innerText = userData.cardNumber;
                    document.getElementById('Balance').innerText = userData.Balance;
                } else {
                    console.log('No document found matching ID');
                }
            })
            .catch((error) => {
                console.log("Error getting document:", error);
            });
    } else {
        console.log("User not found");
    }
});

const logoutButton = document.getElementById('logout');
logoutButton.addEventListener('click', () => {
    signOut(auth)
        .then(() => {
            localStorage.removeItem('loggedInUserId');
            window.location.href = 'index.html';
        })
        .catch((error) => {
            console.error('Error signing out:', error);
        });
});
