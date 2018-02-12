# -*- coding: utf-8 -*-
""" Trivia quiz.. """
from __future__ import print_function
import math
import string
import random

GAME_STATE_TRIVIA = "TRIVIA"
GAME_STATE_START = "START"
GAME_STATE_HELP = "HELP"

GAME_QUESTIONS_KEY = "gameQuestions"
ANSWERTEXT_KEY = "correctAnswerText"
SCORE = "score"
CORRECTANSWERINDEX = "correctAnswerIndex"
SPEECHOUTPUT_KEY = "speechOutput"
REPROMPT_KEY = "repromptText"
CURRENTQUESTION_KEY = "currentQuestionIndex"
STATE_KEY = "state"
LOCALE = "locale"

COUNTER = 0
QUIZSCORE = 0
GAME_LENGTH = 5
ANSWER_COUNT = 4

game_state = GAME_STATE_START

"""
 * When editing your questions pay attention to your punctuation. Make sure you use question marks or periods.
 * Make sure the first answer is the correct one. Set at least ANSWER_COUNT answers, any extras will be shuffled in.
"""

languageSupport = {
    "en-US": {
        "translation": {
            "QUESTIONS": [
        {
            "Reindeer have very thick coats, how many hairs per square inch do they have?":
            ["13,000", "1,200", "5,000", "700", "1,000", "120,000" ]},
        {
            "The 1964 classic Rudolph The Red Nosed Reindeer was filmed in. ":
            ["Japan", "United States", "Finland", "Germany", "Canada", "Norway", "France"]
        },
        {
            "Santas reindeer are cared for by one of the Christmas elves, what is his name?":
            ["Wunorse Openslae", "Alabaster Snowball", "Bushy Evergreen", "Pepper Minstix"]
        },
        {
            "If all of Santas reindeer had antlers while pulling his Christmas sleigh, they would all be. ":
            ["Girls", "Boys", "Girls and boys", "No way to tell"]
        },
        {
            "What do Reindeer eat?":
            ["Lichen", "Grasses", "Leaves" ,"Berries"]
        },
        {
            "What of the following is not true?": 
            ["Caribou live on all continents",
            "Both reindeer and Caribou are the same species",
            "Caribou are bigger than reindeer",
            "Reindeer live in Scandinavia and Russia"]
        },
        {
            "In what year did Rudolph make his television debut?": 
            ["1964", "1979", "2000", "1956"]
        },
        {
            "Who was the voice of Rudolph in the 1964 classic?":
            ["Billie Mae Richards", "Burl Ives", "Paul Soles", "Lady Gaga"]
        },
        {
            "In 1939 what retailer used the story of Rudolph the Red Nose Reindeer?":
            ["Montgomery Ward", "Sears", "Macys", "Kmart"]
        },
        {
            "Santa's reindeer named Donner was originally named what?":
            ["Dunder", "Donny", "Dweedle", "Dreamy"]
        },
        {
            "Who invented the story of Rudolph?":
            ["Robert May", "Johnny Marks", "Santa", "J.K. Rowling"]
        },
        {
            "In what location will you not find reindeer?":
            ["North Pole", "Lapland", "Korvatunturi mountain", "Finland"]
        },
        {
            "What Makes Santa's Reindeer Fly?":
            ["Magical Reindeer Dust", "Fusion", "Amanita muscaria", "Elves"]
        },
        {
            "Including Rudolph, how many reindeer hooves are there?":
            ["36", "24", "16", "8"]
        },
        {
            "Santa only has one female reindeer. Which one is it?": [
            "Vixen", "Clarice", "Cupid", "Comet"]
        },
        {
            "In the 1964 classic Rudolph The Red Nosed Reindeer, what was the snowman narrators name?": [
            "Sam", "Frosty", "Burl", "Snowy"]
        },
        {
            "What was Rudolph's father's name?": [
            "Donner", "Dasher", "Blixen", "Comet"]
        },
        {
            "In the 1964 movie, What was the name of the coach of the Reindeer Games?": [
             "Comet", "Blixen", "Donner", "Dasher"]
        },
        {
            "In the 1964 movie, what is the name of the deer that Rudolph befriends at the reindeer games?": [ 
            "Fireball", "Clarice", "Jumper", "Vixen"]
        },
        {
            "In the 1964 movie, How did Donner, Rudolph's father, try to hide Rudolph's nose?": [ 
            "Black mud", "Bag", "Pillow case", "Sock"]
        },
        {
            "In the 1964 movie, what does the Misfit Elf want to be instead of a Santa Elf?": [
            "Dentist", "Reindeer", "Toy maker", "Candlestick maker"]
        },
        {
            "In the 1964 movie,what was the Bumble's one weakness?": [
            "Could not swim", "Always hungry", "Candy canes", "Cross eyed"]
        },
        {
            "In the 1964 movie, what is Yukon Cornelius really in search of?": [
            "Peppermint", "Gold", "India", "Polar Bears"]
        },
        {
            "In the 1964 movie, why is the train on the Island of Misfit Toys?": [
            "Square wheels", "No Engine", "Paint does not match", "It does not toot"]
        },
        {
            "In the 1964 movie, what is the name of the Jack in the Box?": [
            "Charlie", "Sam", "Billy", "Jack"]
        },
        {
            "In the 1964 movie, why did Santa Claus almost cancel Christmas?": [
            "Storm", "No snow", "No toys", "The Reindeer were sick"]
        },
        {
            "In the 1964 movie, what animal noise did the elf make to distract the Bumble?": [
            "Oink", "Growl", "Bark", "Meow"]
        },
        {
            "In the 1964 movie, what is the name of the prospector?": [
            "Yukon Cornelius", "Slider Sam", "Bumble", "Jack"]
        },
        {
            "How far do reindeer travel when they migrate?": [
            "3000 miles", "700 miles", "500 miles", "0 miles"]
        },
        {
            "How fast can a reindeer run?": [
            "48 miles per hour", "17 miles per hour", "19 miles per hour", "14 miles per hour", "52 miles per hour", "41 miles per hour"]
        }
    ],
            "GAME_NAME" : "American Reindeer Trivia", # Be sure to change this for your skill.
            "HELP_MESSAGE": "I will ask you {0} multiple choice questions. Respond with the number of the answer. " +
            "For example, say one, two, three, or four. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": " What would you like to do? ",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "CANCEL_MESSAGE": "Ok, let's play again soon.",
            "NO_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to {0}. ",
            "WELCOME_MESSAGE": "I will ask you {0} questions, try to get as many right as you can. Just say the number of the answer. Let's begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is {0}: {1}. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question {0}. {1} ",
            "GAME_OVER_MESSAGE": "You got {0} out of {1} questions correct. Thank you for playing!",
            "SCORE_IS_MESSAGE": "Your score is {0}. "
     },
    },
    "en-GB": {
        "translation": {
            "QUESTIONS": [
        {
            "Reindeer have very thick coats, how many hairs per square inch do they have?":
            ["13,000", "1,200", "5,000", "700", "1,000", "120,000" ]},
        {
            "The 1964 classic Rudolph The Red Nosed Reindeer was filmed in. ":
            ["Japan", "United States", "Finland", "Germany", "Canada", "Norway", "France"]
        },
        {
            "Santas reindeer are cared for by one of the Christmas elves, what is his name?":
            ["Wunorse Openslae", "Alabaster Snowball", "Bushy Evergreen", "Pepper Minstix"]
        },
        {
            "If all of Santas reindeer had antlers while pulling his Christmas sleigh, they would all be. ":
            ["Girls", "Boys", "Girls and boys", "No way to tell"]
        },
        {
            "What do Reindeer eat?":
            ["Lichen", "Grasses", "Leaves" ,"Berries"]
        },
        {
            "What of the following is not true?": 
            ["Caribou live on all continents",
            "Both reindeer and Caribou are the same species",
            "Caribou are bigger than reindeer",
            "Reindeer live in Scandinavia and Russia"]
        },
        {
            "In what year did Rudolph make his television debut?": 
            ["1964", "1979", "2000", "1956"]
        },
        {
            "Who was the voice of Rudolph in the 1964 classic?":
            ["Billie Mae Richards", "Burl Ives", "Paul Soles", "Lady Gaga"]
        },
        {
            "In 1939 what retailer used the story of Rudolph the Red Nose Reindeer?":
            ["Montgomery Ward", "Sears", "Macys", "Kmart"]
        },
        {
            "Santa's reindeer named Donner was originally named what?":
            ["Dunder", "Donny", "Dweedle", "Dreamy"]
        },
        {
            "Who invented the story of Rudolph?":
            ["Robert May", "Johnny Marks", "Santa", "J.K. Rowling"]
        },
        {
            "In what location will you not find reindeer?":
            ["North Pole", "Lapland", "Korvatunturi mountain", "Finland"]
        },
        {
            "What Makes Santa's Reindeer Fly?":
            ["Magical Reindeer Dust", "Fusion", "Amanita muscaria", "Elves"]
        },
        {
            "Including Rudolph, how many reindeer hooves are there?":
            ["36", "24", "16", "8"]
        },
        {
            "Santa only has one female reindeer. Which one is it?": [
            "Vixen", "Clarice", "Cupid", "Comet"]
        },
        {
            "In the 1964 classic Rudolph The Red Nosed Reindeer, what was the snowman narrators name?": [
            "Sam", "Frosty", "Burl", "Snowy"]
        },
        {
            "What was Rudolph's father's name?": [
            "Donner", "Dasher", "Blixen", "Comet"]
        },
        {
            "In the 1964 movie, What was the name of the coach of the Reindeer Games?": [
             "Comet", "Blixen", "Donner", "Dasher"]
        },
        {
            "In the 1964 movie, what is the name of the deer that Rudolph befriends at the reindeer games?": [ 
            "Fireball", "Clarice", "Jumper", "Vixen"]
        },
        {
            "In the 1964 movie, How did Donner, Rudolph's father, try to hide Rudolph's nose?": [ 
            "Black mud", "Bag", "Pillow case", "Sock"]
        },
        {
            "In the 1964 movie, what does the Misfit Elf want to be instead of a Santa Elf?": [
            "Dentist", "Reindeer", "Toy maker", "Candlestick maker"]
        },
        {
            "In the 1964 movie,what was the Bumble's one weakness?": [
            "Could not swim", "Always hungry", "Candy canes", "Cross eyed"]
        },
        {
            "In the 1964 movie, what is Yukon Cornelius really in search of?": [
            "Peppermint", "Gold", "India", "Polar Bears"]
        },
        {
            "In the 1964 movie, why is the train on the Island of Misfit Toys?": [
            "Square wheels", "No Engine", "Paint does not match", "It does not toot"]
        },
        {
            "In the 1964 movie, what is the name of the Jack in the Box?": [
            "Charlie", "Sam", "Billy", "Jack"]
        },
        {
            "In the 1964 movie, why did Santa Claus almost cancel Christmas?": [
            "Storm", "No snow", "No toys", "The Reindeer were sick"]
        },
        {
            "In the 1964 movie, what animal noise did the elf make to distract the Bumble?": [
            "Oink", "Growl", "Bark", "Meow"]
        },
        {
            "In the 1964 movie, what is the name of the prospector?": [
            "Yukon Cornelius", "Slider Sam", "Bumble", "Jack"]
        },
        {
            "How far do reindeer travel when they migrate?": [
            "3000 miles", "700 miles", "500 miles", "0 miles"]
        },
        {
            "How fast can a reindeer run?": [
            "48 miles per hour", "17 miles per hour", "19 miles per hour", "14 miles per hour", "52 miles per hour", "41 miles per hour"]
        }
    ],
            "GAME_NAME" : "British Reindeer Trivia", # Be sure to change this for your skill.
            "HELP_MESSAGE": "I will ask you {0} multiple choice questions. Respond with the number of the answer. " +
            "For example, say one, two, three, or four. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": " What would you like to do? ",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "CANCEL_MESSAGE": "Ok, let's play again soon.",
            "NO_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to {0}. ",
            "WELCOME_MESSAGE": "I will ask you {0} questions, try to get as many right as you can. Just say the number of the answer. Let's begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is {0}: {1}. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question {0}. {1} ",
            "GAME_OVER_MESSAGE": "You got {0} out of {1} questions correct. Thank you for playing!",
            "SCORE_IS_MESSAGE": "Your score is {0}. "
     },
    },
    "de-DE": {
        "translation": {
            "QUESTIONS" : [
        {
            "Rentiere haben ein sehr dickes Fell. Wie viele Haare pro Quadratzentimeter haben sie?": [
             "13,000", "1,200", "5,000", "700", "1,000", "120,000"]
        },
        {
            "Der Klassiker aus dem Jahr 1964, Rudolph mit der roten Nase, wurde gedreht in. ": [
            "Japan", "USA", "Finnland", "Deutschland", "Kanada", "Norwegen", "Frankreich"]
        },
        {
            "Um die Rentiere des Weihnachtsmanns kümmert sich eine der Weihnachtselfen. Wie heißt sie?": [
            "Wunorse Openslae", "Alabaster Snowball", "Bushy Evergreen", "Pfeffer Minstix"]
        },
        {
            "Wenn alle Rentiere des Weihnachtsmanns Geweihe hätten, während sie seinen Weihnachtsschlitten ziehen, wären sie alle. ": [
            "Weiblich", "Männlich", "Weiblich und männlich", "Kann man nicht sagen"]
        },
        {
            "Was essen Rentiere?": [
            "Flechten", "Gras", "Blätter", "Beeren"]
        },
        {
            "Welche Aussage ist nicht richtig?": [
            "Karibus leben auf allen Kontinenten", "Karibus und Rentiere gehören derselben Gattung an ",
            "Karibus sind größer als Rentiere", "Rentiere leben in Skandinavien und Russland"]
        },
        {
            "In welchem Jahr kam Rudolph ins Fernsehen?": [
            "1964", "1979", "2000", "1956"]
        },
        {
            "Wer war der Sprecher für Rudolph im klassischen Film aus dem Jahr 1964?": [
            "Billie Mae Richards", "Burl Ives", "Paul Soles", "Lady Gaga"]
        },
        {
            "Welche Handelskette verwendete 1939 die Geschichte von Rudolph mit der roten Nase?": [
            "Montgomery Ward", "Sears", "Macys", "Kmart"]
        },
        {
            "Wie hieß das Rentier des Weihnachtsmanns namens Donner ursprünglich?": [
            "Dunder", "Donny", "Dweedle", "Dreamy"]
        },
        {
            "Wer hat die Geschichte von Rudolph erfunden?": [
            "Robert May", "Johnny Marks", "Santa", "J.K. Rowling"]
        },
        {
            "Wo findest du keine Rentiere?": [
            "Nordpol", "Lappland", "Korvatunturi-Berge", "Finnland"]
        },
        {
            "Warum können die Rentiere des Weihnachtsmanns fliegen?": [
            "Magischer Staub der Rentiere", "Fusion", "Amanita muscaria", "Elfen"]
        },
        {
            "Wieviele Rentierhufe gibt es hier einschließlich Rudolph?": [
            "36", "24", "16", "8"]
        },
        {
            "Der Weihnachtsmann hat nur ein weibliches Rentier. Wie heißt es?": [
            "Blitzen", "Clarice", "Cupid", "Comet"]
        },
        {
            "Wie war der Name des erzählenden Schneemanns im klassischen Film Rudolph mit der roten Nase aus dem Jahr 1964?": [
            "Sam", "Frosty", "Burl", "Snowy"]
        },
        {
            "Wie hieß der Vater von Rudolph?": [
            "Donner", "Dasher", "Blixen", "Comet"]
        },
        {
            "Wie war der Name des Trainers der Rentierspiele im klassischen Film aus dem Jahr 1964?": [
            "Comet", "Blixen", "Donner", "Dasher"]
        },
        {
            "Wie war im klassichen Film aus 1964 der Name des Hirsches, mit dem sich Rudolph befreundete?": [
            "Fireball", "Clarice", "Jumper", "Vixen"]
        },
        {
            "Wie hat der Vater von Rudolph, Donner, im Film aus dem Jahr 1964 versucht, die Nase von Rudolph zu verbergen?": [
            "Schwarzer Schlamm", "Sack", "Kissenbezug", "Socke"]
        },
        {
            "Was möchte die Misfit-Elfe im Film aus dem Jahr 1964 werden anstatt eine Elfe für den Weihnachtsmann?": [
            "Zahnarzt", "Rentier", "Spielzeugmacher", "Kerzenmacher"]
        },
        {
            "Was war die einzige Schwäche von Bumble im Film aus dem Jahr 1964?": [
            "Konnte nicht schwimmen", "War immer hungrig", "Zuckerstangen", "Schielte"]
        },
        {
            "Was sucht Yukon Cornelius in Wirklichkeit im Film aus dem Jahr 1964?": [
            "Pfefferminz", "Gold", "Indien", "Polarbären"]
        },
        {
            "Warum befindet sich der Zug im Film aus dem Jahr 1964 auf der Insel des fehlerhaften Spielzeugs?": [
            "Viereckige Räder", "Keine Dampfmaschine", "Farbe stimmt nicht", "Pfeift nicht"]
        },
        {
            "Wie lautet der Name des Schachtelmännchens im Film aus dem Jahr 1964?": [
            "Charlie", "Sam", "Billy", "Jack"]
        },
        {
            "Warum hat der Weihnachtsmann im Film aus dem Jahr 1964 Weihnachten beinahe abgesagt?": [
            "Sturm", "Kein Schnee", "Kein Spielzeug", "Die Rentiere waren krank"]
        },
        {
            "Welches tierische Geräusch machte die Elfe im Film aus dem Jahr 1964, um den Bumble abzulenken?": [
            "Oink", "Knurr", "Wauwau", "Miau"]
        },
        {
            "Wie lautet der Name des Goldsuchers im Film aus dem Jahr 1964?": [
            "Yukon Cornelius", "Slider Sam", "Bumble", "Jack"]
        },
        {
            "Wie weit ziehen Rentiere auf ihren Wanderungen?": [
            "4800 km", "1100 km", "800 km", "0 km"]
        },
        {
            "Wie schnell läuft ein Rentier?": [
            "77 km pro Stunde", "27 km pro Stunde", "30 km pro Stunde", "22 km pro Stunde", "83 km pro Stunde", "65 km pro Stunde"]
        }
      ],
            "GAME_NAME" : "Wissenswertes über Rentiere in Deutsch", # Be sure to change this for your skill.
            "HELP_MESSAGE": "Ich stelle dir {0} Multiple-Choice-Fragen. Antworte mit der Zahl, die zur richtigen Antwort gehört. " +
            "Sage beispielsweise eins, zwei, drei oder vier. Du kannst jederzeit ein neues Spiel beginnen, sage einfach „Spiel starten“. ",
            "REPEAT_QUESTION_MESSAGE": "Wenn die letzte Frage wiederholt werden soll, sage „Wiederholen“ ",
            "ASK_MESSAGE_START": "Möchten Sie beginnen?",
            "HELP_REPROMPT": "Wenn du eine Frage beantworten willst, antworte mit der Zahl, die zur richtigen Antwort gehört. ",
            "STOP_MESSAGE": "OK, spielen wir ein andermal. Auf Wiedersehen!",
            "CANCEL_MESSAGE": "OK, dann lass uns bald mal wieder spielen.",
            "NO_MESSAGE": "OK, spielen wir ein andermal. Auf Wiedersehen!",
            "TRIVIA_UNHANDLED": "Sagt eine Zahl beispielsweise zwischen 1 und %s",
            "HELP_UNHANDLED": "Sage ja, um fortzufahren, oder nein, um das Spiel zu beenden.",
            "START_UNHANDLED": "Du kannst jederzeit ein neues Spiel beginnen, sage einfach „Spiel starten“.",
            "NEW_GAME_MESSAGE": "Willkommen bei {0}. ",
            "WELCOME_MESSAGE": "Ich stelle dir {0} Fragen und du versuchst, so viele wie möglich richtig zu beantworten. "
            "Sage einfach die Zahl, die zur richtigen Antwort passt. Fangen wir an. ",
            "ANSWER_CORRECT_MESSAGE": "Richtig. ",
            "ANSWER_WRONG_MESSAGE": "Falsch. ",
            "CORRECT_ANSWER_MESSAGE": "Die richtige Antwort ist {0}: {1}. ",
            "ANSWER_IS_MESSAGE": "Diese Antwort ist ",
            "TELL_QUESTION_MESSAGE": "Frage {0}. {1} ",
            "GAME_OVER_MESSAGE": "Du hast {0} von {1} richtig beantwortet. Danke fürs Mitspielen!",
            "SCORE_IS_MESSAGE": "Dein Ergebnis ist {0}. "
        }
     }
}

# --------------- entry point -----------------

def lambda_handler(event, context):
    """ App entry point  """
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended()

# --------------- response handlers -----------------

def on_intent(request, session):
    """ called on Intent """
    intent = request['intent']
    intent_name = request['intent']['name']
    #print("on_intent " +intent_name)
    #print(request)

    getstate(session)
    locale = getlocale(request, session)

    if get_game_state() == GAME_STATE_TRIVIA:        
        return rungame(request, session, locale, intent, session)
        
    return help_handler(False, request, locale, session)

def rungame(request, newgame, locale, intent, session):
    """ process the game questions and user response """
    intent_name = request['intent']['name']
    resource = getresource(locale)

    if 'dialogState' in request:
        #delegate to Alexa until dialog sequence is complete
        if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
            attributes = {"locale":locale}
            return dialog_response(attributes, False)
    
    if intent_name == "AMAZON.StartOverIntent":
        return start_game(request, True, locale)
    elif intent_name == "AMAZON.RepeatIntent":
        reprompt = session['attributes'][REPROMPT_KEY]
        return rebuild_response(request, locale, session, reprompt )
    elif intent_name == "AMAZON.CancelIntent":
        return cancel_response(locale)
    elif intent_name == "AMAZON.StopIntent":
        return cancel_response(locale)
    elif intent_name == "AMAZON.HelpIntent":
        return dohelp(request, False, locale)
    elif intent_name == "AnswerIntent":
        return processuserguess(False, request, session, intent, locale)
    elif intent_name == "DontKnowIntent":
        return processuserguess(True, request, session, intent, locale) 
    return dohelp(request, False, locale)

def processuserguess(usergaveup, request, session, intent, locale):
    """ process the users response, builf next question if required """
   
    resource = getresource(locale)
    speech_output = ""

    game_questions = session['attributes'][GAME_QUESTIONS_KEY]
    correct_answer_index_previous_question = int(session['attributes'][CORRECTANSWERINDEX])
    current_score = int(session['attributes'][SCORE])
    current_question_index_previous_question = int(session['attributes'][CURRENTQUESTION_KEY])
    correct_answer = session['attributes'][ANSWERTEXT_KEY]

    if match_guess_with_answer(intent, correct_answer_index_previous_question):    
       current_score += 1
       speech_output = resource["ANSWER_CORRECT_MESSAGE"]
    else:
        if usergaveup == False:            
           speech_output = resource["ANSWER_WRONG_MESSAGE"]
                          
        speech_output += resource["CORRECT_ANSWER_MESSAGE"].format(correct_answer_index_previous_question, correct_answer)

    if current_question_index_previous_question >= (GAME_LENGTH - 1):
        speech_message = ""
        if usergaveup == False:
           speech_message = resource["ANSWER_IS_MESSAGE"]
        
        speech_message += speech_output + resource["GAME_OVER_MESSAGE"].format(str(current_score), str(GAME_LENGTH))
        return response("", response_plain_text(speech_message, True))   
    
    current_question_index_next_question = current_question_index_previous_question + 1    
    correct_answer_index_next_question = random.randrange(0, ANSWER_COUNT-1, 1)    
        
    new_questions = game_questions[current_question_index_next_question]
            
    round_answers = populate_round_answers(new_questions, 
                    current_question_index_next_question, correct_answer_index_next_question)
         
    correct_answer_text_next_question = round_answers[correct_answer_index_next_question]    
          
    reprompt = get_answers_text(game_questions[current_question_index_next_question], round_answers,
               current_question_index_next_question, locale)
            
    if usergaveup == False:
       speech_message  = resource["ANSWER_IS_MESSAGE"]
    else:
        speech_message = ""   
    speech_message += speech_output + " " + resource["SCORE_IS_MESSAGE"].format(str(current_score)) + " " + reprompt

    correct_answer_index_next_question += 1    
    set_game_state(GAME_STATE_TRIVIA)

    attributes = { SPEECHOUTPUT_KEY: reprompt,
                      REPROMPT_KEY: reprompt,
                      CURRENTQUESTION_KEY: str(current_question_index_next_question),
                      CORRECTANSWERINDEX: str(correct_answer_index_next_question),
                      GAME_QUESTIONS_KEY: game_questions,
                      SCORE: str(current_score),
                      ANSWERTEXT_KEY: correct_answer_text_next_question,
                      STATE_KEY: get_game_state(),
                      LOCALE: locale
                 }
    
    return response(attributes, speech_response_prompt_card(resource["GAME_NAME"],speech_message, reprompt, False))

  
def match_guess_with_answer(intent, correctAnswerIndex):
    """ check if answer matches """  
    if 'slots' in intent:
        slots = intent['slots']
        for key, val in slots.items():            
            if val.get('value'):
                if (val.get('value')).isdigit():
                    lval = int(val['value'].lower())
                    if lval == correctAnswerIndex and lval <= ANSWER_COUNT and lval > 0:
                        #print("user answered " + str(lval) + " correct answer number is: " + str(correctAnswerIndex))
                        return True
    return False
       
   
def cancel_response(locale):
    """ """
    resource = getresource(locale)
    speechmessage = resource["CANCEL_MESSAGE"] 
    return response("", response_plain_text(speechmessage, True))

def rebuild_response(request, locale, session, speech_message):
    """ """
  
    speech_output = session['attributes'][SPEECHOUTPUT_KEY]
    reprompt = session['attributes'][REPROMPT_KEY]
    game_questions = session['attributes'][GAME_QUESTIONS_KEY]
    correct_answer_index = session['attributes'][CORRECTANSWERINDEX]
    current_score = session['attributes'][SCORE]
    current_question_index = session['attributes'][CURRENTQUESTION_KEY]
    correct_answer_text = session['attributes'][ANSWERTEXT_KEY]
    set_game_state(GAME_STATE_TRIVIA)
 
    attributes = { SPEECHOUTPUT_KEY: reprompt,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: current_question_index,
                  CORRECTANSWERINDEX: correct_answer_index,
                  GAME_QUESTIONS_KEY: game_questions,
                  SCORE: current_score,
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
                  LOCALE: locale
                 }

    return response(attributes, response_plain_text_promt(speech_message, speech_message, False))
 
def dohelp(request, newgame, locale):
    """ display help for selected locale """
    
    resource = getresource(locale)
    askmessage =  resource["REPEAT_QUESTION_MESSAGE"] +" " +resource["ASK_MESSAGE_START"] 
    speech_message = resource["HELP_MESSAGE"].format(resource["GAME_NAME"]) + askmessage

    set_game_state(GAME_STATE_HELP)
    attributes = {
                 STATE_KEY: get_game_state()                  
                 }
    return response(attributes, response_plain_text_promt(speech_message, speech_message, False))

def help_handler(newgame, request, locale, session):
    """ help handler """
  
    intent_name = request['intent']['name']
    resource = getresource(locale)
    if newgame == True:
         askmessage = resource["ASK_MESSAGE_START"] 
    else:
         askmessage = resource["REPEAT_QUESTION_MESSAGE"] + resource["ASK_MESSAGE_START"]
     
    if intent_name == "AMAZON.StartOverIntent":
        print("help state: startover intent")
        set_game_state(GAME_STATE_START)
        return start_game(request, False, locale)

    elif intent_name == "AMAZON.RepeatIntent":
        print("help state: repeat intent")
        if SPEECHOUTPUT_KEY in session['attributes']:
            if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
                return dohelp(False, request, session, locale)
        return dohelp(request, True, locale)

    elif intent_name == "AMAZON.CancelIntent":
        return cancel_response(locale)

    elif intent_name == "AMAZON.StopIntent":
        return cancel_response(locale)

    elif intent_name == "AMAZON.HelpIntent":
        if SPEECHOUTPUT_KEY in session['attributes']:
            if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
                return dohelp(request, False, locale)
        return dohelp(request, True, locale)    
     
    speechmessage = resource["HELP_MESSAGE"].format(GAME_LENGTH) + askmessage
    set_game_state(GAME_STATE_HELP)    
    attributes = {
                  STATE_KEY: get_game_state()                  
                 }
    return response(attributes, response_plain_text(speechmessage, False))    
     
def on_launch(request, session):
    """ start """
    #print("launch")
    set_game_state(GAME_STATE_TRIVIA)
    return start_game(request, True, getlocale(request, session))

def start_game(request, newgame, locale):
    """ start a new game """
    
    resource = getresource(locale)

    speechOutput = "" 
    if newgame == True:
       speechOutput = resource["NEW_GAME_MESSAGE"].format(resource["GAME_NAME"]) + resource["WELCOME_MESSAGE"].format(str(GAME_LENGTH)) 
        
    current_question_index = 0
    
    questions = get_question_list(locale)
    correct_answer_index = random.randrange(0, ANSWER_COUNT - 1, 1)
        
    round_answers = populate_round_answers(questions[current_question_index], 
        current_question_index, correct_answer_index)
    correct_answer_text = round_answers[correct_answer_index]
    
    reprompt = get_answers_text(questions[current_question_index], round_answers, current_question_index, locale)
    speech_message = speechOutput + reprompt
    
    correct_answer_index += 1    
    set_game_state(GAME_STATE_TRIVIA)
    
    attributes = { SPEECHOUTPUT_KEY: speech_message,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: str(current_question_index),
                  CORRECTANSWERINDEX: str(correct_answer_index),
                  GAME_QUESTIONS_KEY: questions,
                  SCORE: "0",
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
                  LOCALE: locale
                 }

    return response(attributes, speech_response_prompt_card(resource["GAME_NAME"],speech_message, reprompt, False))     

def populate_round_answers(question, correct_question_index, correct_answer_index):
    """ get answers for a given question, place correct answer at the spot marked by the/
        correctAnswerIndex. 
    """
    for theanswers in question.values():        
        tmp_answer = theanswers[0]        
        theanswers.remove(tmp_answer)
        theanswers_randomised = random.sample(theanswers, len(theanswers) )
        theanswers_randomised.insert(correct_answer_index, tmp_answer)
        theanswers.insert(correct_question_index, tmp_answer)
        return theanswers_randomised

def getstate(session):
    """ get and set the current state  """
 
    if STATE_KEY in session['attributes']:
        set_game_state(session['attributes'][STATE_KEY])
    else:
        set_game_state(GAME_STATE_START)

def get_answers_text(question, reorderedquestion, current_question_index, locale):
    """ get text for the answer """
    number = current_question_index + 1
    resource = getresource(locale)
    k = list(question.keys())
    questiontext = k[0]
    outtext = resource["TELL_QUESTION_MESSAGE"].format(str(number), questiontext) + " "
    
    index = 0
    for qtext in reorderedquestion:
        outtext += str(index + 1) + ". " + qtext +". "
        index += 1        
        if index == ANSWER_COUNT:
            break

    return outtext[:-1]   

def get_game_state():
    """ """
    global game_state
    return game_state

def set_game_state(state):
    """ """
    global game_state
    game_state = state

def getresource(locale):
    """ """
    return languageSupport[locale]["translation"]

def getlocale(request,session):
    """ """
    locale = request['locale']
    if locale == "":
       attributes = session['attributes']
       attributes['locale']
 
    if locale == "":
        locale = "en-US" 
    
    return locale

def on_session_ended():
    """ called on session end  """
    #print(on_session_ended)


def get_question_list(locale):
    """ """
    global GAME_LENGTH
    questions  = []
    res = getresource(locale)
    ilen = len(res["QUESTIONS"])
    questionsample = random.sample(range(0, ilen), GAME_LENGTH)
    for index in questionsample:
        questions.append(res["QUESTIONS"][index])
    return questions
 
# --------------- speech response handlers -----------------
# build the json responses

def response_plain_text(output, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },     
        'shouldEndSession': endsession
    }

def response_plain_text_promt(output, reprompt_text, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
            'type': 'PlainText',
            'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }

def response_ssml_text(output, endsession):
    """ create a simple json plain text response  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_card_image(title, output, endsession, cardtext, smallimage, largeimage):
    """ create a simple json plain text response  """
    return {
        'card': {
            'type': 'Standard',
            'title': title,
            'text': cardtext,
            'image':{
                'smallimageurl':smallimage,
                'largeimageurl':largeimage
            },
        },
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def response_ssml_text_card(title, output, endsession):
    """ create a simple json plain text response  """
    return {
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'shouldEndSession': endsession
    }

def speech_response_prompt_card(title, output, reprompt_text, endsession):
    """  create a simple json response with a card  """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
         'card': {
            'type': 'Simple',
            'title': title,
            'content': reprompt_text
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': endsession
    }


def response_ssml_text_reprompt(title, output, endsession, repromt_text):
    """  create a simple json response with a card  """
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" +output +"</speak>"
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" +repromt_text +"</speak>"
            }
        },
        'shouldEndSession': endsession
    }

def dialog_response(attributes, endsession):
    """  create a simple json response with card """
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response':{
            'directives': [
                {
                    'type': 'Dialog.Delegate'
                }
            ],
            'shouldEndSession': endsession
        }
    }

def response(attributes, speech_response):
    """ create a simple json response """
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speech_response
    }
