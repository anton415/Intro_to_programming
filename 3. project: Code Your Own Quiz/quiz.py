# coding=utf-8
# Game data.
data = {
    'easy': {
        'phrase': ['Pythons a drop-in ___1___ for BASIC in the sense that Optimus Prime is a drop-in ___1___ for a '
            'truck. - Cory Dodt.', 'Perfection [in design] is achieved, not when there is ___1___ more to add'
            ', but when there is ___1___ left to take away. - Antoine de Saint-Exupéry'],
        'answers': [['replacement'], ['nothing']],
        'attempts': 5
    },
    'medium': {
        'phrase': ['Always ___1___ as if the guy who ends up maintaining your ___1___ will be a violent ___2___ who '
            'knows where you live. - Martin Golding.', 'I have always wished for my computer to be as easy to '
            'use as my ___1___; my wish has come true because I can no longer figure out how to use my ___1___'
            '. - Bjarne Stroustrup'],
        'answers': [['code', 'psychopath'], ['telephone']],
        'attempts': 3
    },
    'hard': {
        'phrase': ['Most good ___1___ do programming not because they expect to get ___2___ or get adulation by the '
            'public, but because it is ___3___ to program. - Linus Torvalds', 'Don’t worry if it doesn’t work '
            '___1___. If everything did, you’d be out of a job. - Mosher’s Law of Software Engineering'],
        'answers': [['programmers', 'paid', 'fun'], ['right']],
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
            break
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
