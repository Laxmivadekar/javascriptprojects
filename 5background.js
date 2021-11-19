const button=document.getElementById("btn");
const body=document.body;
const colors=["red","green","yellow","meroon","pink","white","black","blue","purple","voilet","aqua"]
button.addEventListener('click',changeBackgroung)

function  changeBackgroung(){
    const colorIndex=Math.floor(Math.random()*colors.length)
    body.style.backgroundColor=colors[colorIndex]
}