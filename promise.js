/*// these example only for resolve
const prom = new Promise((resolve, reject) => {
    resolve('Yay!');
  });   
  const handleSuccess = (resolvedValue) => {
    console.log(resolvedValue);
  }; 
  prom.then(handleSuccess); // Prints: 'Yay!'*/



/*let prom = new Promise((resolve, reject) => {
let num = 0.2//Math.random();
// console.log(num)
if (num < .5 ){
    resolve('Yay!');
} else {
    reject('Ohhh noooo!');
}
});


const c = (d) => {
  console.log(d);
  console.log("succeful or resolved one")
};
const a = (b) => {
    console.log(b)
    console.log("rejected one");
};*/




/*let prom = new Promise((resolve, reject) => {
  let num = 6//Math.random();
  // console.log(num)
if (num < .5 ){
    resolve('Yay!');
} else {
    reject('Ohhh noooo!');
}
  });
prom
  .then((resolvedValue) => {
    console.log(resolvedValue);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });*/



