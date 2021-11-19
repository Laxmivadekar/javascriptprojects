asyncTask1=()=>{
    console.log("Mahanandha")
}
asyncTask2()=()=>{
    console.log("jyothi")
}
asyncTask3=()=>{
    console.log("jyotsna")
}
asyncTask4=()=>{
    console.log("Rajasri")
}
async function asyncPromAll() {
    const resultArray = await Promise.all([asyncTask1(), asyncTask2(), asyncTask3(), asyncTask4()]);
    for (let i = 0; i<resultArray.length; i++){
      console.log(resultArray[i]); 
    }
  }