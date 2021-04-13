/*
Team Decidophobia -- Madelyn Mao, Dragos Lup 
SoftDev
K21 -- Get Scripty
2021-04-11
- You can write JavaScript code in chromes console 
- You cannot write JavaScript in firefox :(
- Node is helpful to have on your machine when it comes to installing third party 
applications 
- Use html file as host for your js code
- Use console.log('hello world'); to “print” in console
- Add <script src = “intro”.js></script> in your html file to reference your js file
- On Mac, open your html script with a live server for ease in debugging  
*/

//factI(n) returns factorial of n, computed iteratively.
function factI(n) {
    ans = 1;
    while (n > 0) {
        ans = n * ans;
        n = n - 1;
    }
    return ans;
}
console.log(factI(3));

//factR(n) returns factorial of n, computed recursively.
function factR(n) {
    if (n == 1) {
        return n;
    }
    else return n * factR(n - 1);
}
console.log(factR(3));

//fibI(n) returns the nth Fibonacci number, computed iteratively.
function fibI(n) {
    a = 1;
    b = 1;
    c = 0;
    if (n == 1) return 0;
    if (n == 2) return 1;
    while (n > 2) {
        c = a + b;
        a = b;
        b = c;
        n = n - 1;
    }
    return b;
}
console.log(fibI(7));

//fibR(n) returns the nth Fibonacci number, computed recursively.
function fibR(n) {
    if (n <= 1) return n;
    return fibR(n - 1) + fibR(n - 2);
}

console.log(fibR(7));