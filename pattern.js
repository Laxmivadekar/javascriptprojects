/*
1 2 3 4
9 10 11 12
13 14 15 16
5 6 7 8
n=4*/
var r=require("readline-sync")
const n=r.questionInt("enter the number");
str=''
j=1
m=n+(n+1)
for(var i=0;i<n;i++){
    if (i%(n-1)==0){
        for(var k=0;k<n;k++){
            str+=j+k+" "
        }
    console.log(str)
    j+=4
    str=""
    }
    else{
        for(var k=0;k<n;k++){
            str+=m+k+" "
        }
    console.log(str)
    m+=4
    str="" 
    }
}


// 1 2 3 4 5                                  1  2  3  4  5
// 9 10 11 12 13                             11  12 13 14 15 
// 13 14 15 16 17                            21  22 23 24 25
// 5 6 7 8 9                                 16  17 18 19 20
// 17 18 19 20 21                             6  7  8  9  10

// enter the number4
// 1 2 3 4 
// 9 10 11 12 
// 13 14 15 16 
// 5 6 7 8 
