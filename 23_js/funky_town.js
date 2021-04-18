// Team Raspberry Jam :: Dragos Lup, Saqif Abedin
// SoftDev pd1
// K23 -- Basic functions in JavaScript
// 2021-04-15r
// --------------------------------------------------

//CARRY OVER YOUR BEST JS fxns here


// ~~~ NEXT STEPS  ~~~


//Develop, then implement gcd(a,b), which returns the greatest common divisor of a and b.

function gcd(a, b) {
    //While b is not 0
    while (b) {
        var c = b; //Save original value of b
        b = a % b; // Get new value of b by modding a and b
        a = c; // set a to original value of b
    }
    return a; // a will be the gcd
}

//Develop, then implement randomStudent(), which returns a randomly selected name from a list.

function randomStudent() {
    var students = ["Joshua", "Jim", "James"]; //list of names
    var num = Math.floor(Math.random() * students.length);//get random index, where max number is length of students
    return students[num]; //return random name
}
//You may want to create helper functions or external list variables here.
// No thanks
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
