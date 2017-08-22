# coding=utf-8
# Game data.
data = {
    'easy': {
        'phrase': ['Pythons a drop-in ___1___ for BASIC in the sense that Optimus Prime is a drop-in ___1___ for a '
            'truck. - Cory Dodt.', 'Perfection [in design] is achieved, not when there is ___1___ more to add, but when'
            'there is ___1___ left to take away. - Antoine de Saint-Exupéry', 'The trouble with programmers is that you'
            'can never tell what a ___1___ is doing until it’s too late. - Seymour Cray', 'First learn computer science'
            'and all the theory. Next develop a programming style. Then forget all that and just ___1___ . - George '
            'Carrette'],
        'answers': [['replacement'], ['nothing'], ['programmer'], ['hack']],
        'attempts': 5
    },
    'medium': {
        'phrase': ['Always ___1___ as if the guy who ends up maintaining your ___1___ will be a violent ___2___ who '
            'knows where you live. - Martin Golding.', 'I have always wished for my computer to be as easy to '
            'use as my ___1___ ; my wish has come true because I can no longer figure out how to use my ___1___'
            ' . - Bjarne Stroustrup', 'People think that ___1___ is the art of geniuses but the actual reality'
            ' is the opposite, just many people doing things that build on each other, like a wall of mini stones. - '
            'Donald Knuth', 'Debugging is twice as hard as writing the ___1___ in the first place. Therefore, if you '
            'write the ___1___ as cleverly as possible, you are, by definition, not smart enough to debug it. - Brian W'
            '. Kernighan.'],
        'answers': [['code', 'psychopath'], ['telephone'], ['computer science'], ['code']],
        'attempts': 3
    },
    'hard': {
        'phrase': ['Most good ___1___ do programming not because they expect to get ___2___ or get adulation by the '
            'public, but because it is ___3___ to program. - Linus Torvalds', 'Don’t worry if it doesn’t work '
            '___1___ . If everything did, you’d be out of a job. - Mosher’s Law of Software Engineering', 'Measuring '
            'programming ___1___ by lines of code is like measuring aircraft building ___1___ by weight. - Bill Gates',
            'Beware of ___1___ in the above code; I have only proved it correct, not tried it. - Donald E. Knuth.'],
        'answers': [['programmers', 'paid', 'fun'], ['right'], ['progress'], ['bugs']],
        'attempts': 1
    }
}

def insert_answer(phrase, answers, answers_number):
    """
    Behavior: This method insert answer in phrase.
    :param phrase: Phrase with space(___1___) words.
    :param answers: Answer for this space word.
    :param answers_number: Index of answer in data.
    :return: None.
    """
    print phrase
    print answers
    print answers_number
    for index, string in enumerate(phrase):
        empty_string = "___" + str(answers_number) + "___"
        if (string == empty_string):
            phrase[index] = answers[answers_number - 1]

def game(phrases, answers, attempts):
    """
    Behavior: This main method. You sould answer in all words.
    :param phrases: Array with phrases.
    :param answers: Array with answers.
    :param failures: Count of failures.
    :return: None.
    """
    answers_number = 0
    phrase_number = 0
    failure_number = 0
    while len(phrases) > phrase_number and attempts > failure_number:
        failure_number = mini_game(phrases[phrase_number], answers[answers_number], attempts, failure_number)
        phrase_number += 1
        answers_number += 1

def mini_game(phrase, answers, attempts, failure_number):
    """
    Behavior: This method for help main method. You wirk only with one phrase.
    :param phrase: Phrase with empty words.
    :param answers: Words you must answer.
    :param failures: Count of failures.
    :return: None.
    """
    answers_number = 1
    phrase = phrase.split()
    while len(answers) + 1 > answers_number and attempts > failure_number:
        print " ".join(phrase)
        word = raw_input("Type " + str(answers_number) + " word: ")
        if word in answers:
            print "correct :)"
            insert_answer(phrase, answers, answers_number)
            answers_number += 1
        else:
            print "try again :("
            failure_number += 1
            print "You have " + str(attempts - failure_number) + " attempts."
    print " ".join(phrase)
    return failure_number

def choose_level():
    """
    Behavior: This method for choose user level.
    :param: None.
    :return: Level.
    """
    while True:
        level = raw_input('Choose a level (easy / medium / hard): ').lower()
        if level in data:
                return level
        print 'Incorrect level! Try again!'

level = choose_level()
game(data[level]['phrase'], data[level]['answers'], data[level]['attempts'])
