// Team Raspberry Jam :: Dragos Lup, Saqif Abedin
// SoftDev pd1
// K23 -- Basic functions in JavaScript
// 2021-04-15r

//send diagnostic output to console
//(Ctrl-Shift-J in Chromium & Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
//An anonymous fxn is a function without the name, set to a variable (we think)
var f = function (x) {
    var j = 30;
    return j + x;
}; // semicolon at end too


//instantiate an object
var o = {
    'name': 'Thluffy',
    age: 15,
    items: [10, 20, 30, 40],
    morestuff: { a: 1, b: 'ayo' },
    func: function (x) {
        return x + 30;
    }
};


//Returns the factorial of n, computed iteratively.
var fact = function (n) {
    var prod = 1;
    for (; n > 1; n--) {
        prod = prod * n;
    }
    return prod;
};


//Returns the factorial of n, computed recursively.
var factR = function (n) {
    if (n <= 1) {
        return 1;
    }
    else {
        return n * factR(n - 1);
    }
};

//Adds an item to the list definited by the id "thelist"
var addItem = function (text) {
    var list = document.getElementById("thelist"); // This gets "the list"
    var newitem = document.createElement("li"); // This defines the variable as an li, or the part of the list
    newitem.innerHTML = text; // This definies the inside of the item as the text
    list.appendChild(newitem); // This adds the item to the list
};

//Removes an item on the document, not specifically "the list"
var removeItem = function (n) {
    var listitems = document.getElementsByTagName('li'); //Gets something with the tag li
    listitems[n].remove(); // Gets the nth item, removes it
};

//Adds the red class to all of the li's on the document
var red = function () {
    var items = document.getElementsByTagName("li"); //gets the li's
    for (var i = 0; i < items.length; i++) { //runs through them
        items[i].classList.add('red'); //Adds the red class
    }
};

//Adds either the blue or red class to all of the li's on the document, alternating
var stripe = function () {
    var items = document.getElementsByTagName("li"); //gets all the li's
    for (var i = 0; i < items.length; i++) {
        if (i % 2 == 0) { //if even
            items[i].classList.add('red'); //adds red class
        } else { //if odd
            items[i].classList.add('blue'); //adds blue class
        }
    }
};

// Returns information based on the click that happened
var buttonCallback = function (e) {
    console.log("\n\nhere comes e...");
    console.log(e); //information regarding the thing that clicked, usually the user's mouse
    console.log("\n\nhere comes 'this'...");
    console.log(this); //information regarding the thing being clicked.
}

//Gets the element b, or in this case the button
var b = document.getElementById('b');
//Adds an event listener, that waits for "click" to happen so it can run buttonCallback
b.addEventListener('click', buttonCallback);

//adds the red class to the specific list item (or thing clicked)
var redCallback = function (e) {
    console.log("\n\n---redCallback invoked---")
    console.log(this); //returns information about thing clicked
    this.classList.add('red'); //adds the red class to the thing clicked.
}

var thelist = document.getElementById("thelist"); //gets the list by id
var litems = thelist.children; //gets the items in the list
//Isn't a function, runs automatically
for (var i = 0; i < litems.length; i++) { //runs through the list
    litems[i].addEventListener('click', redCallback); //Whenever you click on an item in the list, add red to the number of classes
    litems[i].addEventListener('mouseover', function (e) { //Whenever you mouseover the item
        console.log("user has moved into this:" + this); //Sends message to the console about thing being hovered over
        this.classList.toggle('green'); //toggles the green class
    });
    litems[i].addEventListener('mouseout', function (e) { //whenever your mouse leaves the item.
        console.log("user has moved out of this:" + this);//Sends message to the console about thing no longer being hovered over
        this.classList.toggle('blue'); //toggles the blue class
    });
}