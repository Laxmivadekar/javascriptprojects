/*const brainstormDinner = require('./asyncandawaitlibrary.js');


// Native promise version:
function nativePromiseDinner() {
  brainstormDinner().then((meal) => {
	  console.log(`I'm going to make ${meal} for dinner.`);
  });
}


// async/await version:
async function announceDinner() {
  // Write your code below:
  let meal = await brainstormDinner();
  console.log(`I'm going to make ${meal} for dinner.`);
}

announceDinner();*/

let myPromise = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('Yay, I resolved!')
      }, 1000);
    });
  }
async function noAwait() {
let value = myPromise();
console.log(value);
}

async function yesAwait() {
let value = await myPromise();
console.log(value);
}

noAwait(); // Prints: Promise { <pending> }
yesAwait(); // Prints: Yay, I resolved!~