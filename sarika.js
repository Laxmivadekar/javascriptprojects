a=["hydrogen","helium","lithium","beryllium"]
// function gases(){
//     var l=[]
//     for (var i of a){
//         l.push(i.length)
//     }
//     return l
// }
// console.log(gases())

var b=(x)=>{
    var l=[]
    for (var i of x){
        l.push(i.length)
    }
    return l

}
console.log(b(a))