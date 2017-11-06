/**
 * The action can be 1 or 2. In order to determine which card is upside, first or second.
 * @type {number}
 */
var action = 1;
/**
 *
 */
var firstCardData;
/**
 *
 */
var secondCardData;
/**
 *
 */
var firstCard;
/**
 *
 */
var secondCard;
/**
 *
 * @type {number}
 */
var openCards = 0;
/**
 * Time spent on the game.
 * @type {number}
 */
var time = performance.now();
/**
 * Number of moves.
 * @type {number}
 */
var moveCount = 0;
/**
 * Number of moves. Used to reduce the number of stars.
 * @type {number}
 */
var moveCountForRemoveStars = 0;
/**
 * Number of stars. Initially equal to 3. The more moves, the fewer stars.
 * @type {number}
 */
var stars = 3;

/**
 * Click on card.
 */
$('.card').on("click", viewCard);

/**
 * Click on restart button.
 */
$('.restart').on("click", restart);

/**
 * Creation of an array of cards, for their shuffling.
 * @type {jQuery|HTMLElement}
 */
var arrayCards = $('.card');
// Shuffle cards.
arrayCards = shuffle(arrayCards);
// Add to page.
$(".deck").append(arrayCards);


/**
 * Function for shuffle cards.
 * @param array
 * @returns {*}
 */
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

/**
 * For restart button. Reload window.
 */
function restart() {
    window.location.reload();
}

/**
 * For click on card. Show this card.
 */
function viewCard() {
    /**
     * If this first card, wait when will be second action.
     */
    if (action === 1) {

        /**
         * The countdown begins with the first click on the card.
         */
        if(moveCount === 0) {
            var display = document.querySelector('#time');
            startTimer(display);
        }

        /**
         * Show image of card.
         */
        $(event.target).toggleClass('match');
        firstCardData = $(event.target);
        firstCard = event.target.childNodes.item(1);
        /**
         * Next, the second card will be opened.
         * @type {number}
         */
        action = 2;

        /**
         * Action for second card.
         */
    } else {
        /**
         * Increase in the number of moves. 1 move = 2 open cards.
         */
        moveCount++;
        moveCountForRemoveStars++;
        /**
         * Show image of card.
         */
        $(event.target).toggleClass('match');
        secondCardData = $(event.target);
        secondCard = event.target.childNodes.item(1);

        /**
         * If the cards match they remain upside.
         */
        if (firstCard.isEqualNode(secondCard)) {
            $(firstCardData).toggleClass('match');
            $(secondCardData).toggleClass('match');
            $(firstCardData).toggleClass('open show');
            $(secondCardData).toggleClass('open show');
            openCards = openCards + 2;
            /**
             * If all the cards are reversed, a congratulation will appear.
             */
            if (openCards === 16) {
                congratulation();
            }
            /**
             * If the cards do not match, wait for 2 seconds and flip them back.
             */
        } else {
            $('.card').off("click");
            setTimeout(wait, 2000);
        }
        /**
         * The user has to turn the first card.
         * @type {number}
         */
        action = 1;
        /**
         * Display the number of stars.
         */
        starRating();
        /**
         * Display the number of moves.
         */
        moveDisplay();
    }
}

/**
 * Display the number of stars.
 */
var starRating = function() {
    if (stars > 0) {
        if (moveCountForRemoveStars >= 16) {
            $('.stars').children("li").get(0).remove();
            stars--;
            moveCountForRemoveStars = 0;
        }
    }
};

/**
 * Display the number of moves.
 */
var moveDisplay = function () {
    $('.moves').text(moveCount)
}

/**
 * User Congratulations.
 */
var congratulation = function() {
    document.getElementById('win').removeAttribute('style');
    time = performance.now() - time;
    if (moveCount > 20) stars - 1;
    if (moveCount > 30) stars - 1;
    $('.allTime').html('You got: ' + moveCount + ' moves, ' + parseInt(time/1000) + ' seconds and ' + stars + ' stars.');
};

/**
 * Wait 2 seconds before turning the cards back. There is also a blocking of the opening of cards.
 */
var wait = function() {
    $(firstCardData).toggleClass('match');
    $(secondCardData).toggleClass('match');
    firstCardData = null;
    secondCardData = null;
    firstCard = null;
    secondCard = null;
    $('.card').on("click", viewCard);
};

/**
 * Reflection of time during the game of the user.
 * @param display
 */
function startTimer(display) {
    var start = Date.now(),
        diff,
        minutes,
        seconds;
    function timer() {
        // get the number of seconds that have elapsed since
        // startTimer() was called
        diff = (((Date.now() - start) / 1000) | 0);

        // does the same job as parseInt truncates the float
        minutes = (diff / 60) | 0;
        seconds = (diff % 60) | 0;

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;
    };
    // we don't want to wait a full second before the timer starts
    timer();
    setInterval(timer, 1000);
}