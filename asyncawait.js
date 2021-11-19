myPromise=()=>{
    return " I am resolved now!"
}

async function asyncFuncExample(){
    let resolvedValue = await myPromise();
    console.log(resolvedValue);
  }
   
  asyncFuncExample(); // Prints: I am resolved now!
  