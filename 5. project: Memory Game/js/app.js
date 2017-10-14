function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}


/*
 * set up the event listener for a card. If a card is clicked:
 *  - display the card's symbol (put this functionality in another function that you call from this one)
 *  - add the card to a *list* of "open" cards (put this functionality in another function that you call from this one)
 *  - if the list already has another card, check to see if the two cards match
 *    + if the cards do match, lock the cards in the open position (put this functionality in another function that you call from this one)
 *    + if the cards do not match, remove the cards from the list and hide the card's symbol (put this functionality in another function that you call from this one)
 *    + increment the move counter and display it on the page (put this functionality in another function that you call from this one)
 *    + if all cards have matched, display a message with the final score (put this functionality in another function that you call from this one)
 */

var action = 1;
var firstCardData;
var secondCardData;
var firstCard;
var secondCard;
var openCards = 0;

$('.card').on("click", viewCard);

function viewCard() {
    if (action === 1) {
        $(event.target).toggleClass('match');
        firstCardData = $(event.target);
        firstCard = event.target.childNodes.item(1);
        action = 2;
    } else {
        $(event.target).toggleClass('match');
        secondCardData = $(event.target);
        secondCard = event.target.childNodes.item(1);
        if (firstCard.isEqualNode(secondCard)) {
            $(firstCardData).toggleClass('match');
            $(secondCardData).toggleClass('match');
            $(firstCardData).toggleClass('open show');
            $(secondCardData).toggleClass('open show');
            openCards = openCards + 2;
            console.log("You open: " + openCards);
            if (openCards === 16) {
                console.log("You win!");
            }
        } else {
            setTimeout(wait, 2000);
        }
        action = 1;
    }
}

console.log("Hello World! 1");

var wait = function() {
    $(firstCardData).toggleClass('match');
    $(secondCardData).toggleClass('match');
    firstCardData = null;
    secondCardData = null;
    firstCard = null;
    secondCard = null;
};

var arrayCards = $('.card');
console.log(arrayCards.length);
// Shuffle cards.
arrayCards = shuffle(arrayCards);
// Add to page.
$(".deck").append(arrayCards);


/*
Object.keys(arrayCards).forEach(function(element) {
    console.log(element.outerHTML);
});
alert(arrayCards[0].outerHTML);
 */