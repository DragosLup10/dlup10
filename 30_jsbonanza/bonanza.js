// Team Candian Owls: Karl Hernandez, Dragos, Arib
// SoftDev
// K30 -- JSorcery
// 2021-05-15

// Setup inital variables to make life eaiser
var c = document.getElementById("board");
var scoreboard = document.getElementById("score");
var wd = c.width;
var ht = c.height;
var ctx = c.getContext("2d");

var requestID;
// the body of the snake with it being located roughtly around the center of the canvas
var snek = [[wd/2, ht/2], [(wd/2)-(wd/50), ht/2], [(wd/2)-2*(wd/50), ht/2], [(wd/2)-3*(wd/50), ht/2]];
// the fruit which the snek eats
var fruit = null;
// direction
var v = [0,0];
var score = 0;

/// Drawing the snek
for (x = 0; x < snek.length; x++) ctx.fillRect(snek[x][0], snek[x][1], wd/50, ht/50);

// Basically the game -> reset the board -> redraw snek -> check if fruit is not collide -> play snak
function drawBoard() {
    setTimeout(function OnTick(){
    clearTimeout();
    ctx.clearRect(0,0,wd,ht);
    DrawFruit();
    ctx.fillStyle = "green";
    for (x = 0; x < snek.length; x++) ctx.fillRect(snek[x][0],snek[x][1], wd/50, ht/50); //Redraw Snek
    if (v[0] != 0 | v[1] != 0) {
        snek.unshift([snek[0][0] + v[0], snek[0][1] + v[1]]);
        if (!fruitCollide()){
            snek.pop();
        }
        //console.log(v[0] + ' ' + v[1]);
        // console.log(requestID);
        if (snekCollide()) gameEnd();
        else requestID = window.requestAnimationFrame(drawBoard); //Next Frame
    }}, 500)
}

// Check for self death
function snekCollide() {
    for (x = 1; x < snek.length; x++) { //Check if snek ran into itself
        if (snek[x][0] == snek[0][0] & snek[x][1] == snek[0][1]) {
            return true;
        }
    }
    return (snek[0][0] < 0 | snek[0][1] < 0 | snek[0][0] > wd | snek[0][1] > ht); //Check if snake hit wall
}

// check for prey death
function fruitCollide() {
    if (fruit[0] == snek[0][0] & fruit[1] == snek[0][1]){
        fruit = null;
        score += 1;
        scoreboard.innerHTML = score;
        return true;
    }
    return false;
}

// draws a random fruit
function DrawFruit(){
    if (fruit == null) {
        FruitTesting();
    }
    ctx.fillStyle = "red";
    ctx.fillRect(fruit[0],fruit[1], wd/50, ht/50);
}

//The snake has very specific prefrences
function FruitTesting() {
    fruit = [Math.floor(Math.random()*51)*(wd/50),Math.floor(Math.random()*51)*(ht/50)];
    for (x = 1; x < snek.length; x++) {
        if (snek[x][0] == fruit[0] & snek[x][1] == fruit[1]) {
            FruitTesting();
            break;
        }
    }
}

// ends the game
function gameEnd() {
    window.cancelAnimationFrame(requestID); //End Animation
    requestID = null;
    snek = [[wd/2, ht/2], [(wd/2)-(wd/50), ht/2], [(wd/2)-2*(wd/50), ht/2], [(wd/2)-3*(wd/50), ht/2]]; //Reset Snek
    v = [0,0];
    score = 0;
    // clears timeout
    clearTimeout();
    // update the score
    scoreboard.innerHTML = score;
    fruit = null;
    ctx.clearRect(0,0,wd,ht);
    for (x = 0; x < snek.length; x++) ctx.fillRect(snek[x][0],snek[x][1], wd/50, ht/50); //Redraw Starting Snek

}

// Changes direction on press
document.onkeypress = function turn(event) { //Check key presses for turning
    if (event.keyCode == 97 & v[0] != wd/50) v = [-wd/50,0]; //Left, A
    if (event.keyCode == 100 & v[0] != -wd/50) v = [wd/50,0]; //Right, D
    if (event.keyCode == 119 & v[1] != ht/50) v = [0,-ht/50]; //Up, W
    if (event.keyCode == 115 & v[1] != -ht/50) v = [0,ht/50]; //Down, S
    if (requestID == null & [100, 119, 115].includes(event.keyCode)) drawBoard(); //Start game upon picking direction
}

// init game
drawBoard()