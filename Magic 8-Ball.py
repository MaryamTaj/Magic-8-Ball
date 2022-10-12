# Author: Maryam Taj
# Name of Program: Magic 8-Ball
# Description of Program: This program simulates a game of Magic 8-Ball, wherin the user poses a question, and the computer outputs an answer.

print('Welcome to the 21st century Magic 8-Ball.')                                                                                                     #Introduction
while True:
    Userchoice = str(input('What is your question today?'))                                                                                            #Computer asks user to type their question
                                                                                                                                                       #Computer discusses technology and mathematics's rin predicting the future
                                                                                                                                                       #Backslashes are equivalent to an 'Enter' and move code to a new line, so it fits on one screen. Remove them
                                                                                                                                                       #before running the code because they add uneccessary space to the code
    print("I see.. Well, you must realize that given our advances in technology, the future is entirely calculable,\
    as inevitable as mathematics. An advanced grasp of probability mapped onto a thorough apprehension of human \
    psychology and the known dispositions of any given individual can reduce the number of variables that influence \
    life's outcomes considerably. But, to answer your question..")
                                                                                                                                                       #Computer's possible answers (string values) coincide with keys (integers). Dictionaries are more helpful to
                                                                                                                                                       #store strings as integers than lists
                                                                                                                                                       #because lists rely on position. print(List[20]) prints the string in position 20. However, in dictionaries,
                                                                                                                                                       #it prints the string next to integer 20. This gives the coder more flexibility as they can refer to strings
                                                                                                                                                       #based on their keys (integer), rather than coutning their position every time
    Dictionary = {1: 'You may rely on it.', 2: 'It is certain.', 3: 'It is decidedly so.', 4: 'Yes', 5: 'Without a doubt.', \
                  11: 'My sources say no.', 12: "Don't count on it.", 13: 'Very doubtful.', 14: 'Outlook not so good.', \
                  15: 'My reply is no.', 6: 'As I see it, yes.', 7: 'Most likely.', 8: 'Yes, definitely.', 9: 'Outlook good.', \
                  10: 'Signs point to yes.', 16: 'Ask again later.', 17: 'Better not tell you now.', 18: 'Concentrate and ask again.', \
                  19: 'Cannot predict now.', 20: 'Reply hazy, ask again.'}
    import random                                                                                                                                      #Import random module which will randomly output a number from 1 to 20, with 1 and 20 included
    x = random.randint(1,20)                                                                                                                           #Assign x the value of the random integer output
    print(Dictionary[x])                                                                                                                               #Computer answers the user's question. It print the value assigned to x in the dictionary                  
    Replay = str(input('Would you like to play again?'))                                                                                               #Computer asks user if they would like to play again?
    if Replay == 'Yes':                                                                                                                                #If user replies 'Yes', the code underneath the while True statement begins again
        print("I see that you are beginning to understand the world's predictability. As they say, the universe is rarely so lazy so as to \
        indulge in coincidences. There is a pattern to everything. Find the pattern, and you have the world at your fingertips. But I digress...")
    if Replay == 'No':                                                                                                                                 #If user replies 'No', the computer responds and breaks out of the while True loop, concluding the code
        print('Very well.')
        break

