ANALYSIS:
=========

RESEARCH:
---------

  ------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Source              Link                                                                                                                                                                                     Access Date   Summary
  Article             [*https://en.wikipedia.org/wiki/Poker\_probability\_(Texas\_hold\_%27em)*](https://en.wikipedia.org/wiki/Poker_probability_(Texas_hold_%27em))                                           17/09/16      Lots of formulas and probability calculations that can be used in the AI for making decisions about what card to play next, how much to bet, what cards other players have.
  Web page            [*http://pokerpredictor.com/headsup*](http://pokerpredictor.com/headsup)                                                                                                                 17/09/16      Reads your two inputted cards and calculates various probabilities such as win rates, and what it is strongest and weakest against. Also has other Texas Hold ‘em tools.
  Article             [*http://www.codeproject.com/Articles/19091/More-Texas-Holdem-Analysis-in-C-Part*](http://www.codeproject.com/Articles/19091/More-Texas-Holdem-Analysis-in-C-Part)                       17/09/16      An article discussing a program that will calculate and analyse certain aspects of the game using several algorithms.
  Article             [*https://en.wikipedia.org/wiki/Monte\_Carlo\_method*](https://en.wikipedia.org/wiki/Monte_Carlo_method)                                                                                 17/09/16      A method of calculating probabilities using randomness to solve problems. This method is used lots in poker to analyse and determine probabilities. Also see the Monte Carlo Algorithm. This algorithm is always fast, probably correct.
  Article             [*https://en.wikipedia.org/wiki/Las\_Vegas\_algorithm*](https://en.wikipedia.org/wiki/Las_Vegas_algorithm)                                                                               17/09/16      Another randomised algorithm that calculate various probabilities within poker, this algorithm is probably fast, always correct.
  Article             [*http://www.codeproject.com/Articles/19092/More-Texas-Holdem-Analysis-in-C-Part*](http://www.codeproject.com/Articles/19092/More-Texas-Holdem-Analysis-in-C-Part)                       18/09/16      The second half of More Texas Hold ‘em Analysis in C\# contains algorithms like the Monte Carlo algorithm and the code and analysis of them.
  Article             [*http://pokercoder.blogspot.co.uk/2006/07/towards-meaningful-ordering-of-hands.html*](http://pokercoder.blogspot.co.uk/2006/07/towards-meaningful-ordering-of-hands.html)               18/09/16      An explanation of a poker AI going in depth with certain methods and such.
  Rules set           [*https://en.wikipedia.org/wiki/Texas\_hold\_%27em\#Rules*](https://en.wikipedia.org/wiki/Texas_hold_%27em#Rules)                                                                        18/09/16      The rules for Texas Hold ‘em as explanations for them.
  Article             [*https://www.partypoker.com/how-to-play/texas-holdem.html*](https://www.partypoker.com/how-to-play/texas-holdem.html)                                                                   18/09/16      A basic and comprehensive tutorial on how to play Texas Hold ‘em.
  Article             [*https://www.partypoker.com/how-to-play/hand-rankings.html*](https://www.partypoker.com/how-to-play/hand-rankings.html)                                                                 18/09/16      A list of the hands in any game of poker ordered by their ranks.
  Glossary            [*https://www.partypoker.com/how-to-play/school/basics/glossary.html*](https://www.partypoker.com/how-to-play/school/basics/glossary.html)                                               18/09/16      A list of all poker terms and explanations of them.
  Article             [*https://en.wikipedia.org/wiki/Poker\_Effective\_Hand\_Strength\_(EHS)\_algorithm*](https://en.wikipedia.org/wiki/Poker_Effective_Hand_Strength_(EHS)_algorithm)                        18/09/16      An algorithm that calculates the strength of a poker hand compared to all other hands.
  Existing Solution   [*https://code.google.com/archive/p/openholdembot/*](https://code.google.com/archive/p/openholdembot/)                                                                                   18/09/19      An existing open source Texas Hold ‘em AI that can be used to get ideas and inspiration from.
  Existing Solution   [*http://poker.srv.ualberta.ca/*](http://poker.srv.ualberta.ca/)                                                                                                                         18/09/16      Another Hold ‘em AI coded by students of the University of Alberta, there are several programs on the webpage which shows the AI’s strategy. These will come in useful when looking for strategies for my AI to see which one is the best.
  Existing Solution   [*https://code.google.com/archive/p/specialkpokereval/*](https://code.google.com/archive/p/specialkpokereval/)                                                                           18/09/16      A lightweight Hold ‘em hand evaluator AI.
  Article             [*https://en.wikipedia.org/wiki/Artificial\_neural\_network*](https://en.wikipedia.org/wiki/Artificial_neural_network)                                                                   18/09/16      An article all about neural networks.
  Article             [*http://www.codeproject.com/Articles/1028339/Basis-of-Neural-Networks-in-Visual-Basic-NET*](http://www.codeproject.com/Articles/1028339/Basis-of-Neural-Networks-in-Visual-Basic-NET)   18/09/16      An article which talks about neural networks, how they work and how to implement them into visual basic.
  Book                [*https://www.amazon.com/dp/1880685000/?tag=stackoverfl08-20*](https://www.amazon.com/dp/1880685000/?tag=stackoverfl08-20)                                                               18/09/16      Chapters discuss the value of deception, bluffing, raising, the slow-play, the value of position, psychology, heads-up play, game theory, implied odds, the free card, and semibluffing. These are all tactics that the AI could employ.
  Journal             [*https://www.doc.ic.ac.uk/\~nd/surprise\_96/journal/vol4/cs11/report.html*](https://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol4/cs11/report.html)                                     18/06/16      Different types of neural networks are explained, demonstrated and applications are given.
  Video               [*https://youtu.be/h3l4qz76JhQ*](https://youtu.be/h3l4qz76JhQ)                                                                                                                           18/06/16      A short video explaining how to create a simple neural network.
  ------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SELF-DISSCUSSION:
-----------------

The aim of this project is to see if it possible to make an AI that will
play Texas Hold ‘em and beat a player. I will achieve this by first of
all making the game itself, which is an easy task, I will then implement
an AI to play against a player.

Texas Hold ‘em is a variation of poker where all players are dealt two
random cards, “Hole Cards” by the “Dealer”. The two players to the left
of the dealer are the “Small Blind” and the “Big Blind” respectively.
The “Small Blind” is required to bet a fixed starting bet and the “Big
Blind” is required to bet double the “Small Blind”. Then the player to
the left of the “Big Blind” will then start the first round of betting.
The first player will assess their hand and if they think it is good
enough for them to win they will “Call”, which means they will match the
previous player's bet or they will “Raise”, which means they will bet
more than the minimum bet to raise the minimum bet for other players.
The player can also choose to go “All In” if they are certain they will
win this round, which means they will bet all their money. If the player
decides their cards are not worth playing with and they will probably
lose, they will “Fold”, which means not betting and returning your cards
to the dealer and skipping the round. Then each player will repeat this
until one round of betting is over (no one else “Raises” or goes “All
In” for a round). This is known as the “Pre-Flop”. Once all the betting
has finished the three shared cards are dealt so that everyone can see
(face up). This is called the “Flop”. Then another round of betting
occurs and a fourth shared card, “The Turn”, is dealt. Another round of
betting occurs and then the fifth and final shared card, “The River”, is
dealt. A final round of betting then occurs. The hand can then end in
one of two ways; the players turn over their “Hole Cards” and whoever
has the best hand wins or someone will bet enough that all the other
players fold and they win. The ultimate end goal is to turn a profit and
to do that you don’t necessarily need to win every hand.

There are several ways in which I can make the game of poker for the AI
to play on. I can use a GUI application or a console application. Since
the program is not meant for an end user but is for investigation
purposes I can use either method, a console application will be easier
and less time consuming to develop yet the GUI application will be much
easier to use and test the AI on. As it is not that hard to switch
between the two I can always choose which one I want to use later down
the road.

The game will be made in Python as I already have prior knowledge of the
program and it has several abilities that will be useful to making an AI
as well as math libraries like NumPy which will help me manage arrays in
more powerful ways. Also if I do decide to make it into a GUI
application it is easy to do so, with libraries like tkinter, which make
it easy to make a GUI application. I will also use libraries like random
which has several randomisation options. I can use this to select a
random card from an array. This ensures the game is always fair.

There is also several ways in which I can get the AI to interact with
the game. I could build the AI directly into the game so they both
operate in the same program but this could make it harder to
troubleshoot when the program is not working to see if it is the AI or
the game itself that is causing the program not to work. I could also
make the game and the AI different programs and get them to communicate
via text file or database, this however would be very time consuming and
would not contribute much towards the investigation on the AI. If I were
to store information about the game in a database this is what it would
look like:

  -------- -------- -------- ---------- ----------- ------ ------
  Flop 1   Flop 2   Flop 3   The Turn   The River   AI 1   AI 2
  JS       KD       8S       8C         3H          7C     6D
  -------- -------- -------- ---------- ----------- ------ ------

This database can then be shared between the game and the AI allowing
the AI to access its cards and the shared cards as they are revealed.

There are two main methods that I could use for the AI:

-   I could make a general algorithm which will calculate the odds of my
    hand winning compared to all the other possible hands. This would be
    fast and efficient but predictable, meaning that the human player
    could easily figure out the AI’s strategy and easily combat it. It
    would also only win if it had been repeatedly dealt good hands as if
    it is dealt a bad hand it would not be able to choose when or when
    not to bluff (out bet the other players so they all fold and you
    win).

-   I could make a neural network that would learn the best ways to play
    > over trial and error, each time becoming more and more effective
    > at playing the game. A general algorithm would then control the
    > weighting of the neural network according to their success. This
    > method will not be as fast as I will have to run the AI with
    > thousands of AI players, who do not know how to play the game. I
    > will then use the general algorithm to determine which AI player
    > was the best and then weight the ability of the players. A new
    > generation of players would be made with the determined weighting
    > and knowledge of the previous player that they were selected to
    > be. This process happens over and over again through lots of hands
    > and generations until the best individual AI players play really
    > well. This process can be endless as there will always be small
    > improvements but there will be diminishing return up until the
    > point where the improvements are unnoticeable and don’t make a
    > difference. Once trained the best player is selected and put up
    > against a human player. This method can be very good at playing
    > Texas Hold ‘em as there are no detectable patterns in the AIs
    > logic and if trained correctly, with the right kind of dataset, it
    > can bluff and win hands which the first algorithm would just fold
    > on to save money. However this methods bluffing ability also has
    > the chance to lose money if the bluff is unsuccessful.

The best method is clearly the neural network as it is the method used
in most successful AI created for Texas Hold ‘em. But if I need to
change method later on, due to the complexity of neural networks, it is
possible to do so.

Finally to test if the AI is better than a human player I will play the
AI myself for a number of hands and judge who made a profit, NOT who won
the most games as you can still lose the majority of games but make lots
of profit on a few, thus winning overall as you made money and the other
player(s) lost money (or gained less than you did). If the AI is

successful then I know that it is possible to create an AI that is
better than a human if not then I can try to improve the AI until it
wins or cannot be improved anymore, in that case I will know that it is
not possible to create an AI with the resources I have that is better
than a human but know that other AIs have been created that are far more
successful than a human player.

### TIMELINE:

  --------------------------------------------------------------------------------- -------------
  Activity                                                                          Finish Date
  Research                                                                          22/09/16
  Analysis                                                                          06/10/16
  Requirements                                                                      20/10/16
  Design                                                                            17/11/16
  > Write Pseudocode for the Hold ‘em game                                          
  Make Decision on whether it’s a console program or forms program.                 
  Technical Solution                                                                26/01/17
  Make the Hold ‘em game.                                                           
  Make a basic AI using a general algorithm to test the game.                       
  Plan the neural network and make a basic version of it.                           
  Test the basic neural network and make improvements.                              
  Make final neural network.                                                        
  Testing                                                                           23/02/17
  Start the neural network playing so it can learn the game to an advanced level.   
  Make improvements to neural network and game where needs be.                      
  Evaluation and Final Progress Check                                               16/03/17
  Final Hand-in                                                                     30/03/17
  --------------------------------------------------------------------------------- -------------

**\
**

### THE GAME:

I will make a poker game that will create two players (the human player
and the AI) it will then assign two random cards (card1 and card2) from
a deck of cards to each player. It will then also assign five more
random cards from the deck to the table cards (flop1, flop2, flop3,
turn, and river). I could assign each player big blind and small blind
but since this is only a two player game of poker big blind and small
blind are not relevant so I shall miss this out. The game will then play
through a game of poker, deducting betting money as it goes along and
displaying the visible table cards after every betting round when they
are meant to be shown. Once the game of poker is finished it will then
determine the winner by first checking if anyone has folded and if not
it will use a card ranking algorithm to decide the winner. Once the
winner is decided the game will then distribute money to the correct
player and start a new game of poker, all the while keeping track of
scores. To help me truly understand how the game is going to work I
created an IPSO, dataflow diagram and flowchart for the game.

The following is the IPSO diagram for the game:

  ------------------------- ---------------------------------------------------------------------------------------------
  **IN**                    **PROCESS**

  Call                      Compare hand with rankings to determine who wins.
                            
  Raise                     Money processing and transactions.
                            
  Bet amount (and All in)   Randomisation of cards.
                            
  Fold                      Determine whether the round of betting is over and whether the next card needs to be dealt.
                            
                            Determine who won the game when one player runs out of money.

  **STORE**                 **OUT**

  Pot                       A representation of the cards on the game board.
                            
  Players Money             The player’s current amount of money.
                            
  AIs Money                 The users hand.
                            
  Flop1                     A representation of who won and with what hand in the hand rankings.
                            
  Flop2                     
                            
  Flop3                     
                            
  Turn                      
                            
  River                     
                            
  AIs Card 1                
                            
  AIs Card 2                
                            
  Players Card 1            
                            
  Players Card 2            
                            
  Big Blind                 
                            
  Small Blind               
                            
  Hand Rankings             
                            
  Round                     
  ------------------------- ---------------------------------------------------------------------------------------------

Dataflow diagram for the game:

![\\\\godalming.ac.uk\\dfs\\UserAreas\\Students\\154146\\download.png](media/image1.png){width="6.260416666666667in"
height="5.645833333333333in"}

![](media/image2.png){width="6.267716535433071in"
height="8.902777777777779in"}Flowchart for the game:

This data dictionary that declares the classes and variables that could
be used in the game:

  --------------------- ---------------- -------------------------------------
  **Data Dictionary**
  Name
  Pot
  Player Money
  AI Money
  Card
  Betting stage
  Turn
  Winner
  --------------------- ---------------- -------------------------------------

From this analysis I have formed a good idea of how a Texas Hold ‘em
game works and how I can make one. Since the main focus of the project
is on the AI there are no notable changes or features of this game from
the original other than the fact there is not big or small blind.

### 

### THE AI:

I plan to create a neural network for the AI. The neural network will
train itself off a pre-existing database and then play the game, so that
it has the highest chance of turning a profit as my research suggests.

The following is the IPSO diagram for the AI:

  ------------------------------------- ----------------------------------------------------------
  **IN**                                **PROCESS**

  AI Card 1                             Money processing and transactions.
                                        
  AI Card 2                             Train network on dataset and adjust weights accordingly.
                                        
  Flop 1                                Run current cards through weights to determine move.
                                        
  Flop 2                                
                                        
  Flop 3                                
                                        
  Turn                                  
                                        
  River                                 

  **STORE**                             **OUT**

  Weighting of neural network           Call
                                        
  Number of players in neural network   Raise
                                        
  Move                                  Bet amount (and All in)
                                        
                                        Fold
  ------------------------------------- ----------------------------------------------------------

Dataflow diagram for the AI:

![\\\\godalming.ac.uk\\dfs\\UserAreas\\Students\\154146\\ddfdf.png](media/image3.png){width="6.270833333333333in"
height="4.489583333333333in"}

The data dictionary that declares the classes and variables that could
be used in the AI:

  --------------------- ----------- -------------------
  **Data Dictionary**
  Name
  Pot
  AI Money
  Weightings
  Player in network
  --------------------- ----------- -------------------

REQUIREMENTS:
-------------

1.  The game interface easily readable and useable.

    1.  The player should be able to easily read their cards and choose
        what action to make.

    2.  The player must easily be able to see how much money is in the
        pot, their wallet and the AI’s wallet.

2.  The game must be able to store the card deck.

    1.  The game program must be able to access it easily

    2.  The game will have to be able to draw random cards from it and
        ensure the same ones are not drawn twice.

3.  The game must be able to send and receive data with the AI.

    1.  The AI’s hand and the shared cards must be given to the AI
        program.

    2.  The AI must be able to tell the game what action it wants to
        make.

    3.  The game must be able to send and receive money with the AI

4.  The game must be able to correctly handle all money and distribute
    it.

    1.  The game must receive betting money and place it into a pot.

    2.  The game must give all winnings to the winner.

5.  The game must be able to determine the winner.

    1.  It must be able to determine the winner by rating each player’s
        hands then comparing them with each other.

6.  The game must be able to determine whether a round of betting is
    over.

7.  The AI must be able to receive various data inputs for processing.

    1.  The AI needs to be able to receive all data from the game that
        is required.

        1.  AI cards.

        2.  Shared cards.

    2.  The AI must be able to receive data from its wallet.

8.  The AI must be able to use the data it has received and create a
    decision on what action it should make.

    1.  The AI must be able to determine whether it should Fold, Call or
        Raise.

        1.  It will need a dataset to train itself on.

        2.  It will need to judge its move based on what the neural
            network returns when the AI current cards are put in.

    2.  The AI must determine how much it wants to bet.

DESIGN:
=======

### FILES, DATA STRUCTURES, METHODS OF ACCESS:

What files I will need:

-   A text file for moves to train the neural network against

-   A text file for correct outcomes of moves needed to train the
    network.

Methods of access:

-   I will use the dependency csv to manipulate my dataset.

### PROCESSES:

*The game:*

There are multiple algorithms involved in the functioning of the game,
below are some pseudo code examples of them.

Card assignment algorithm:

*class CardPile:*

*deck = (array of all card combinations)*

*usedCards = \[ \]*

*def getCard():*

*while True:*

*randCard = deck\[randint(0,51)\]*

*if randCard not in usedCards:*

*usedCards.append(randCard)*

*return randCard*

*break*

This algorithm seems to be the most efficient out of all the ways I
found to do it. It would also be possible to compare to the randomly
drawn cards to the other cards assigned to the plays and tables
variables not a used cards variable. This way would be slower however
and mean that the program is less secure.

Hand comparison algorithm:

*class Compare:*

*Hcards = (list of human and table cards)*

*Acards = (list of AI and table cards)*

*def cardCompare(hc,ac,tblc):*

> *if evaluateCard(Hcards) &gt; evaluateCard(Acards):*
>
> *return 'human'*
>
> *elif evaluateCard(Acards) &gt; evaluateCard(Hcards):*
>
> *return 'ai'*

*else: *

> *return "no-one"*

*def evaluateCard(hand):*

*groups = group(\['--23456789TJQKA'.index(r) for r, s in hand\])*

*counts, ranks = zip(\*groups)*

*print groups*

*if ranks == (14, 5, 4, 3, 2):*

*ranks = (5, 4, 3, 2, 1)*

*straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4*

*flush = len(set(\[s for r, s in hand\])) == 1*

*return (*

*9 if (5, ) == counts else*

*8 if straight and flush else*

*7 if (4, 1) == counts else*

*6 if (3, 2) == counts else*

*5 if flush else*

*4 if straight else*

*3 if (3, 1, 1) == counts else*

*2 if (2, 2, 1) == counts else*

*1 if (2, 1, 1, 1) == counts else*

*0), ranks*

*def group(self,items):*

*groups = \[(items.count(x), x) for x in set(items)\]*

*return sorted(groups, reverse = True)*

Since there are few ways to make this algorithm and my investigation is
on the AI I decided to use the card sorting algorithm from Udacity’s
“Design of Computer Programs” course. This way I can focus my time on
making the neural network work instead of using it to create a card
sorting algorithm.

Winner Calculator Algorithm:

def *CalcWinner*

*If Showdown = True*

*Return CompareCards*

*If AI.LastTurn = Fold*

*Return Player*

*If Player.LastTurn = Fold*

*Return AI*

*If AI.Bank = 0 and Player.Bank &gt; 0*

*Return Player*

*If Player.Bank = 0 and AI.Bank &gt; 0*

*Return AI*

This algorithm finds who won the current game by using a series of
simple if statements.

*The AI:*

There are multiple algorithms involved in the functioning of the AI,
below are some pseudo code examples of them.

Neural Network:

*x =handstrained.csv*

*y = correctpredtrained.csv*

*w = 2\* random((3,1)) - 1*

*for t in xrange(100000):*

*l0 = x*

*l1 = 1/(1+exponential(-dotproduct(l0, w)))*

*l1\_error = y - l1*

*l1\_change = l1\_error\* l1\*(1-l1)*

*w += dotproduct(l0.T,l1\_change)*

This method would allow the AI to be unpredictable as well as play more
human like, given the right dataset.

I could also make the AI by using simple probabilities found online. I
could then use these probabilities and combine them with the AIs current
cards to reach an outcome.

### USER INTERFACE DESIGN:

Since this is an investigation on whether AI is able to beat a human at
poker a UI element is not necessary. In order to use the program I shall
use a command line interface and as the program runs it will print out
necessary information along the way.

### PACKAGES AND FRAMEWORK: 

[]{#_e1fp5vnq1r1q .anchor}I will plan on using a scientific computing
package such as NumPy ([*http://www.numpy.org/*](http://www.numpy.org/))
to help with sigmoid function and matrices. I will also need to use the
built in csv library in order to import and manipulate the datasets to
train the neural network with. On top of this I will need the random
([*https://docs.python.org/2/library/random.html*](https://docs.python.org/2/library/random.html))
dependency so I can generate random numbers where necessary.
[[]{#_emwz1magnd62 .anchor}]{#_91eu46eers0w .anchor}

### DESIGN OF TESTING:

[]{#_l2b23ncnifi .anchor}I will test several aspects of my program:

1.  []{#_of9tlbyjdwwr .anchor}I will test the basic functionality of the
    game, to make sure it correctly carried out betting rounds and
    handles the end of the game correctly.

    1.  []{#_bow0cqieabln .anchor}To do this I will use test data to
        test each section of the game. My project is not focused on the
        game however so I will not test this in depth. The following is
        some example test data:[]{#_jpkf9ttwtbg1 .anchor}

  ------ --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- -----------------------------------------------------
  N^o^   Purpose                                                                                                         Test Data                                                                                                Expected result
  1      To see if the game launches and prints the welcome screen.                                                      Run the program.                                                                                         Welcome to texas hold’em, please enter your name:
  2      To see if a new player object is created when requested                                                         Enter a name in the “Please enter your name” field.                                                      You are now on round 1 of the game.
  3      To see if the game is able to process a move given by the player.                                               Type “fold” in the “Please enter move” field.                                                            You folded, AI wins. The score is AI - 1 Human - 0.
  4      To see if the game is able to correctly determine the winner of the game using the card comparison algorithm.   Play the game until both you and the AI check during the final round of betting to enter the showdown.   \[someone\] wins with the cards \[C1,C2\]
  ------ --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- -----------------------------------------------------

1.  []{#_izhp3x3kq2e7 .anchor}At the end of each test I will screenshot
    the outcome and assess if it passes or not.

    []{#_8x4zimg5pdbd .anchor}

<!-- -->

1.  I will test that the AI is able to correctly interface with the
    game.

    1.  To do this I will play through several games each time playing
        in different styles and I will assess how the AI copes with
        this. Here is an example of some testing data:

  ------ ------------------------------------------------------- ------------------------------------------------------------------------------------- -------------------------------------
  N^o^   Purpose                                                 Test Data                                                                             Expected result

  1      To see if the AI can handle the human player folding.   Run the program and fold on the first turn. Then see if the AI functions next game.   Human folds, AI wins.
                                                                                                                                                       
                                                                                                                                                       You are now on round 2 of the game.
                                                                                                                                                       
                                                                                                                                                       AI plays as normal.
  ------ ------------------------------------------------------- ------------------------------------------------------------------------------------- -------------------------------------

1.  I will screen shot the outcome of the test and assess if it passes
    or not.

    []{#_q3zwlfabnhnx .anchor}

<!-- -->

1.  I will test that the AI correctly reads and trains itself off the
    dataset.

    1.  To do this I will isolate the AI and see if it performs the
        correct move according to the dataset I give it.

    2.  Here is some example testing data:

  ------ ------------------------------------------------------------------------- ---------------------------------------------------------------------- -----------------
  N^o^   Purpose                                                                   Test Data                                                              Expected result
  1      To see if the AI makes the correct move according to the dataset given.   Give the AI cards that you would expect it to bet on e.g. AH and AC.   AI raises.
  ------ ------------------------------------------------------------------------- ---------------------------------------------------------------------- -----------------

[]{#_8zni8um17ufd .anchor}

1.  I will test that the ability of the AI and see if it is able to gain
    more money than a human over a period of 10 games.

    1.  To do this I will play normally against the AI over 10 games
        with the aim for me to win. This gives the AI the toughest
        environment possible.

    2.  I will keep a log of all turns I make, the outcome of each game
        and the cards each player had, along with the table cards, and
        finally how much money each player has at the end of each round.

[[]{#_n7ttakbvijof .anchor}]{#_o3wxygkhab8r .anchor}

TECHNICAL SOLUTION:
===================

I started off my technical solution by exploring the different types of
neural networks and decide what I would use to create my AI.

I first created a simple neural network that could play the game higher
or lower by learning off a small dataset (the complete code is found at
appendix A):

11. *\#define datasets*

12. x = np.array((\[\[0\],\[12\],\[4\],\[7\]\]), dtype=float)

13. y = np.array(\[\[1\],\[0\],\[1\],\[0\]\])

14.  

15. *\#normalise*

16. x = x/12

17.  

18. *\#weights*

19. w0 = 2\*np.random.random((1,4))-1

20. w1 = 2\*np.random.random((4,4))-1

21. w2 = 2\*np.random.random((4,4))-1

22. w3 = 2\*np.random.random((4,1))-1

23.  

24. *\#train*

25. **for** t **in** xrange(100000):

26.    

27.     *\#forward propagation*

28.     l0 = x

29.     l1 = sigma(np.dot(l0, w0))

30.     l2 = sigma(np.dot(l1, w1))

31.     l3 = sigma(np.dot(l2, w2))

32.     l4 = sigma(np.dot(l3, w3))

33.    

34.     *\#error + change calc*

35.     l4\_error = y - l4    

36.     l4\_change = l4\_error\*sigma\_deriv(l4)

37.     l3\_error = l4\_change.dot(w3.T)

38.     l3\_change = l3\_error \* sigma\_deriv(l3)

39.     l2\_error = l3\_change.dot(w2.T)

40.     l2\_change = l2\_error \* sigma\_deriv(l2)

41.     l1\_error= l2\_change.dot(w1.T)

42.     l1\_change = l1\_error \* sigma\_deriv(l1)

43.    

44.     *\#update weights*

45.     w3 += np.dot(l3.T, l4\_change)

46.     w2 += np.dot(l2.T, l3\_change)

47.     w1 += np.dot(l1.T, l2\_change)

48.     w0 += np.dot(l0.T, l1\_change)

It used a neural network that used gradient descent to learn. Gradient
descent is where each weight in the network is assigned a random weight.
The learning dataset (x) is then put through the weights and the outcome
is recorded. The difference between this and the actual outcome store in
dataset (y) is then calculated, this is the error. To find how much it
needs to adjust the weights by, the change, it multiplies the error by
the gradient of the point on the sigma function on which each layer
lies. It then adjusts the weights by the dot product of the layer and
the layer change needed. This whole process is repeated 100,000 times to
achieve maximum accuracy. The user may then enter their own card, this
then gets put through the weights and returns whether the next card is
likely to be higher or lower.

This method worked well but only for small datasets. The dataset I will
be using will be significantly bigger as it will store the move that
should be made for each possible combination of the players hand cards.

I then found a neural network type that is able to handle large data
sets. Using a method called “Stochastic gradient descent” the neural
network is able to be trained quickly on a large dataset.

I then set about creating an AI that would learn what move to make in
poker when given its two hand cards. First I had to create a dataset for
the AI to learn off. I did this by writing a program that compared every
possible hand combination with every possible hand combination it could
go up against multiple times, each time with different table cards. I
then assigned each card combination points based on how many times it
won. From this I created a dataset. There are two files that make up the
dataset, correctpredtrained.csv and handstrained.csv. The headers of
each dataset look like the following:

correctpredtrained.csv:

  ----------------------------- ----------------------------- ------------------------------------
  Card1 float value (rank/14)   Card2 float value (rank/14)   Suited (1= suited, 0 = not suited)
  ----------------------------- ----------------------------- ------------------------------------

handstrained.csv:

  ------------------------------------------
  Correct prediction (1 = raise, 0 = fold)
  ------------------------------------------

The program took roughly eight hours to create the dataset which I am
going to use for my AI. The code for this program can be found in
appendix B. The dataset can be found in appendix C. After I had created
this dataset I then moved on to create the Stochastic Gradient Descent
neural network that would play AI:

8.      *\#define datasets*

9.      \_\_x = np.genfromtxt('handstrained.csv', delimiter=',')

10.    
    \_\_y = np.genfromtxt('correctpredtrained.csv', delimiter=',')\[np.newaxis\]

11.     \_\_y = \_\_y.T

12.     *\#seed*

13.     np.random.seed(1)

14.     *\#weights*

15.     \_\_w0 = 2\*np.random.random((3,4))-1

16.     \_\_w1 = 2\*np.random.random((4,4))-1

17.     \_\_w2 = 2\*np.random.random((4,4))-1

18.     \_\_w3 = 2\*np.random.random((4,1))-1

<!-- -->

36.        **for** i **in** xrange(10):

37.             self.epoch()

<!-- -->

50.    **def** epoch(self):

51.         \_\_z=0

52.         *\#train*

53.         **for** t **in** xrange(len(self.\_\_y)/4):

54.             *\#forward propagation*

55.             \_\_l0 = self.\_\_x\[\_\_z:(\_\_z+5)\]

56.             \_\_l1 = self.sigma(np.dot(\_\_l0, self.\_\_w0))

57.             \_\_l2 = self.sigma(np.dot(\_\_l1, self.\_\_w1))

58.             \_\_l3 = self.sigma(np.dot(\_\_l2, self.\_\_w2))

59.             \_\_l4 = self.sigma(np.dot(\_\_l3, self.\_\_w3))

60.             *\#error + change calc*

61.             \_\_l4\_error = self.\_\_y\[\_\_z:(\_\_z+5)\] - \_\_l4  
     

62.             \_\_l4\_change = \_\_l4\_error\*self.sigmaDeriv(\_\_l4)

63.             \_\_l3\_error = \_\_l4\_change.dot(self.\_\_w3.T)

64.             \_\_l3\_change = \_\_l3\_error
    \* self.sigmaDeriv(\_\_l3)

65.             \_\_l2\_error = \_\_l3\_change.dot(self.\_\_w2.T)

66.             \_\_l2\_change = \_\_l2\_error
    \* self.sigmaDeriv(\_\_l2)

67.             \_\_l1\_error= \_\_l2\_change.dot(self.\_\_w1.T)

68.             \_\_l1\_change = \_\_l1\_error
    \* self.sigmaDeriv(\_\_l1)

69.             *\#update weights*

70.             self.\_\_w3 += np.dot(\_\_l3.T, \_\_l4\_change)

71.             self.\_\_w2 += np.dot(\_\_l2.T, \_\_l3\_change)

72.             self.\_\_w1 += np.dot(\_\_l1.T, \_\_l2\_change)

73.             self.\_\_w0 += np.dot(\_\_l0.T, \_\_l1\_change)

74.             \_\_z += 5

(The full code can be found in appendix B)

Unlike the standard gradient descent neural network this method trains
itself off chunks of the dataset at a time.

After I had solved the AI element I then needed to create a poker game
for the AI to play against someone on. The following are some of the
major algorithms in the game.

The playGame() function calls betting rounds in the right order, reveals
table cards as they are needed, calls on the card comparison to
determine the winner and returns the winner once run through.

1.      **def** playGame(self):

2.          self.\_\_human.setMoney(-self.\_\_table.getEntryMoney())

3.          self.\_\_ai.setMoney(-self.\_\_table.getEntryMoney())

4.          self.\_\_table.setPot(2\*self.\_\_table.getEntryMoney())

5.          self.\_\_table.setNextPlayer('r')

This is the preflop betting round.

1.          **if** self.bettingRound() == False:

2.              **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2))

3.              self.\_\_human.setAction('-')

4.              self.\_\_ai.setAction('-')

This is the flop betting round.

1.              **if** self.bettingRound() == False:

2.                  **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2)+",
    "+self.\_\_table.getCards(3))

3.                  self.\_\_human.setAction('-')

4.                  self.\_\_ai.setAction('-')

This is the turn betting round.

1.                  **if** self.bettingRound() == False:

2.                      **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2)+",
    "+self.\_\_table.getCards(3)+", "+self.\_\_table.getCards(4))

3.                      self.\_\_human.setAction('-')

4.                      self.\_\_ai.setAction('-')

This is the river betting round.

1.                      **if** self.bettingRound() == False:

If neither player folds nor runs out of money during any of the betting
rounds then the card comparison function is called to determine the
winner.

1.                       
      self.\_\_table.setWinner(Compare().cardCompare(self.\_\_human.getCard(), self.\_\_ai.getCard(),\[self.\_\_table.getCards(0),self.\_\_table.getCards(1),self.\_\_table.getCards(2),self.\_\_table.getCards(3),self.\_\_table.getCards(4)\]))

2.                       
      **if** self.\_\_table.getWinner() == 'Human':

3.                           
      self.\_\_human.setMoney(self.\_\_table.getPot())

4.                              self.\_\_table.setPot(0)

5.                              self.\_\_human.setScore(1)

6.                           
      self.\_\_table.setWinnersCards(str(self.\_\_human.getCard()))

7.                              **return** str(self.\_\_human.getName())

8.                          **elif** self.\_\_table.getWinner() == 'AI':

9.                           
      self.\_\_ai.setMoney(self.\_\_table.getPot())

10.                             self.\_\_table.setPot(0)

11.                             self.\_\_ai.setScore(1)

12.                          
      self.\_\_table.setWinnersCards(str(self.\_\_ai.getCard()))

13.                             **return** 'AI'

14.                         **else**:

15.                          
      self.\_\_human.setMoney(self.\_\_table.getPot()/2)

16.                          
      self.\_\_ai.setMoney(self.\_\_table.getPot()/2)

17.                             self.\_\_table.setPot(0)

18.                             self.\_\_table.setWinnersCards('')

19.                             **return** 'no-one'

If a player runs out of money or folds a winner will be chosen in this
section.

1.          **else**:

2.              **if** self.\_\_gameOver == 'ai':

3.                  **return** str(self.\_\_human.getName())

4.              **if** self.\_\_gameOver == 'human':

5.                  **return** 'AI'

6.              **elif** self.\_\_table.getWinner() == 'Human':

7.               
      self.\_\_table.setWinnersCards(str(self.\_\_human.getCard()))

8.                  **return** str(self.\_\_human.getName())

9.              **elif** self.\_\_table.getWinner() == 'AI':

10.              
      self.\_\_table.setWinnersCards(str(self.\_\_ai.getCard()))

11.                 **return** 'AI'

12.             **else**:

13.                 self.\_\_table.setWinnersCards('')

14.                 **return** 'no-one'

This function checks that both players still have money to play with
else it will end the game.

1.      **def** checkMoney(self,flag):

2.       
      **if** int(self.\_\_human.getMoney()) &lt; 0 **and** flag == False:

3.                      self.\_\_gameOver = 'human'

4.                      self.\_\_table.setWinner('AI')

5.                      self.\_\_table.setWon('t')

6.                      self.\_\_ai.setScore(1)

7.                      **return** True

8.       
      **elif** int(self.\_\_ai.getMoney()) &lt; 0 **and** flag == False:

9.                      self.\_\_gameOver = 'ai'

10.                     self.\_\_table.setWinner('Human')

11.                     self.\_\_table.setWon('t')

12.                     self.\_\_human.setScore(1)

13.                     **return** True

14.         **elif** flag == True: **return** True

15.         **else**: **return** False

This function is the base level of the betting rounds, it displays each
players money, checks that no one has folded and calls the checkMoney()
algorithm as well as call each players individual betting round in the
correct order.

1.  **def** bettingRound(self):

2.          self.\_\_table.setWon('f')

3.          \_\_flag = False

4.          **if** self.\_\_table.getNextPlayer() == 1:

5.              **while** \_\_flag == False:

6.                  \_\_flag = self.checkMoney(\_\_flag)

7.                  **print** "Your money:
    " + str(self.\_\_human.getMoney())

8.                  **print** "AI money: " + str(self.\_\_ai.getMoney())

9.                  **print** "Pot: " + str(self.\_\_table.getPot())

10.                 **if** \_\_flag == False:

11.                  
      **if** self.bettingRoundHuman()== True **and** \_\_flag == False:

12.                         self.\_\_table.setNextPlayer('a')

13.                         \_\_flag = True

14.                 \_\_flag = self.checkMoney(\_\_flag)

15.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

16.                 **print** "AI money: " + str(self.\_\_ai.getMoney())

17.                 **print** "Pot: " + str(self.\_\_table.getPot())

18.                 **if** \_\_flag == False:

19.                  
      **if** self.bettingRoundAi() == True **and** \_\_flag == False:

20.                         self.\_\_table.setNextPlayer('h')

21.                         \_\_flag = True

22.         **elif** self.\_\_table.getNextPlayer() == 2:

23.             **while** \_\_flag == False:

24.                 \_\_flag = self.checkMoney(\_\_flag)

25.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

26.                 **print** "AI money: " + str(self.\_\_ai.getMoney())

27.                 **print** "Pot: " + str(self.\_\_table.getPot())

28.                 **if** \_\_flag == False:

29.                  
      **if** self.bettingRoundAi()== True **and** \_\_flag == False:

30.                         self.\_\_table.setNextPlayer('h')

31.                         \_\_flag = True

32.                 \_\_flag = self.checkMoney(\_\_flag)

33.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

34.                 **print** "AI money: " + str(self.\_\_ai.getMoney())

35.                 **print** "Pot: " + str(self.\_\_table.getPot())

36.                 **if** \_\_flag == False:

37.                  
      **if** self.bettingRoundHuman() == True **and** \_\_flag == False:

38.                         self.\_\_table.setNextPlayer('a')

39.                         \_\_flag = True

40.         **if** self.\_\_table.getWon() == True:

41.             **return** True

42.         **else**:

43.             **return** False

This is the AI betting round, it requests moves from the AI object and
deals with the movement of money between players.

1.      **def** bettingRoundAi(self):

2.          self.\_\_ai.setAction('x')

3.          **if** self.\_\_ai.getAction() == 'f':

4.              **print** "AI folds with the cards:
    " + str(self.\_\_ai.getCard())

5.              self.\_\_human.setMoney(self.\_\_table.getPot())

6.              self.\_\_table.setPot(0)

7.              self.\_\_human.setScore(1)

8.              self.\_\_table.setWinner('Human')

9.              self.\_\_table.setWon('t')

10.             **return** True

11.         **elif** self.\_\_ai.getAction() == 'r':

12.             self.\_\_ai.setRaiseAmount()

13.             self.\_\_ai.setMoney(-self.\_\_ai.getRaiseAmount())

14.             self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

15.             **print** "AI raises by
    " + str(self.\_\_ai.getRaiseAmount())

16.             **if** self.\_\_human.getAction() == 'r':

17.              
      self.\_\_ai.setMoney(-self.\_\_human.getRaiseAmount())

18.              
      self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

19.                 self.\_\_table.setWon('f')

20.                 **return** False

21.             **elif** self.\_\_human.getAction() == 'c':

22.                 self.\_\_table.setWon('f')

23.                 **return** False

24.             **else**:

25.                 self.\_\_table.setWon('f')

26.                 **return** False

27.         **elif** self.\_\_ai.getAction() == 'c':

28.             **print** "AI calls"

29.             **if** self.\_\_human.getAction() ==  'r':

30.              
      self.\_\_ai.setMoney(-self.\_\_human.getRaiseAmount())

31.              
      self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

32.                 self.\_\_table.setWon('f')

33.                 **return** False

34.             **elif** self.\_\_human.getAction() == 'c':

35.                 self.\_\_table.setWon('f')

36.                 **return** True

37.             **else**:

38.                 self.\_\_table.setWon('f')

39.                 **return** False

This is the human betting round, it requests moves from the user and
deals with the movement of money between players.

1.      **def** bettingRoundHuman(self):

2.          **print** str(self.\_\_human.getName())+", your cards are:
    " + str(self.\_\_human.getCard())

3.          self.\_\_human.setAction(raw\_input("What is your move?
    (r/c/f): "))

4.          **if** self.\_\_human.getAction() == 'f':

5.              self.\_\_ai.setMoney(self.\_\_table.getPot())

6.              self.\_\_table.setPot(0)

7.              self.\_\_ai.setScore(1)

8.              self.\_\_table.setWinner('AI')

9.              self.\_\_table.setWon('t')

10.             **return** True

11.         **elif** self.\_\_human.getAction() == 'r':

12.             self.\_\_human.setRaiseAmount(input("Raise by: "))

13.          
      self.\_\_human.setMoney(-self.\_\_human.getRaiseAmount())

14.             self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

15.             **if** self.\_\_ai.getAction() == 'r':

16.              
      self.\_\_human.setMoney(-self.\_\_ai.getRaiseAmount())

17.                 self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

18.                 self.\_\_table.setWon('f')

19.                 **return** False

20.             **elif** self.\_\_ai.getAction() == 'c':

21.                 self.\_\_table.setWon('f')

22.                 **return** False

23.             **else**:

24.                 self.\_\_table.setWon('f')

25.                 **return** False

26.         **elif** self.\_\_human.getAction() == 'c':

27.             **if** self.\_\_ai.getAction() == 'c':

28.                 self.\_\_table.setWon('f')

29.                 **return** True

30.             **elif** self.\_\_ai.getAction() ==  'r':

31.              
      self.\_\_human.setMoney(-self.\_\_ai.getRaiseAmount())

32.                 self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

33.                 self.\_\_table.setWon('f')

34.                 **return** False

35.             **else**:

36.                 self.\_\_table.setWon('f')

37.                 **return** False

This is the card comparison function that decides which players hand was
stronger.

1.  **class** Compare:

2.      \_\_allHcards = \[\]

3.      \_\_allAcards = \[\]

First it creates two arrays; one for the humans and table cards and one
for the AI and table cards.

1.      **def** cardCompare(self,hc,ac,tblc):

2.       
      self.\_\_allHcards = \[hc\[0\], hc\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

3.       
      self.\_\_allAcards = \[ac\[0\], ac\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

Here it decides which player had the highest rated hand by comparing
tuples.

1.       
      **if** self.evaluateCard(self.\_\_allHcards) &gt; self.evaluateCard(self.\_\_allAcards): **return** 'Human'

2.       
      **elif** self.evaluateCard(self.\_\_allAcards) &gt; self.evaluateCard(self.\_\_allHcards): **return** 'AI'

3.          **else**: **return** "no-one"

4.  

This function creates a tuple that represents the players hand strength.

1.      **def** evaluateCard(self,hand):

2.         
    \_\_groups = self.group(\['--23456789TJQKA'.index(r) **for** r, s **in** hand\])

3.          \_\_counts, \_\_ranks = zip(\*\_\_groups)

4.          **if** \_\_ranks == (14, 5, 4, 3, 2):

5.              \_\_ranks = (5, 4, 3, 2, 1)

6.         
    \_\_straight = len(\_\_ranks) == 5 **and** max(\_\_ranks)-min(\_\_ranks) == 4

7.          \_\_flush = len(set(\[s **for** r, s **in** hand\])) == 1

8.          **return** (

9.              9 **if** (5, ) == \_\_counts **else**

10.             8 **if** \_\_straight **and** \_\_flush **else**

11.             7 **if** (4, 1) == \_\_counts **else**

12.             6 **if** (3, 2) == \_\_counts **else**

13.             5 **if** \_\_flush **else**

14.             4 **if** \_\_straight **else**

15.             3 **if** (3, 1, 1) == \_\_counts **else**

16.             2 **if** (2, 2, 1) == \_\_counts **else**

17.             1 **if** (2, 1, 1, 1) == \_\_counts **else**

18.             0), \_\_ranks

19.  

20.     **def** group(self,items):

21.        
    \_\_groups = \[(items.count(x), x) **for** x **in** set(items)\]

22.         **return** sorted(\_\_groups, reverse = True)

Since the card comparison algorithm is a difficult one to code and there
are only a few certain ways to perform it I made use of a card
comparison algorithm found on Udacity’s “Design of Computer Programs”
course.

This is the card pile class that contains the deck array and distributes
cards to players and the table.

1.  **class** CardPile:

2.     
    \_\_deck = \[r+s **for** r **in** '23456789TJQKA' **for** s **in** 'SHDC'\]

3.      \_\_usedCards  = \[\]

4.      **def** getCard(self):

5.          **while** True:

6.              \_\_randCard = self.\_\_deck\[randint(0,51)\]

7.              **if** \_\_randCard **not** **in** self.\_\_usedCards:

8.                  self.\_\_usedCards.append(\_\_randCard)

9.                  **return** \_\_randCard

10.                 **break**

11.     **def** reset(self):

12.         self.\_\_usedCards = \[\]

13.  

14. game = Game('One')

15. game.menu()

After I had finished coding each separate algorithm I combined them all
into one python file, added linking pieces of code and converted it into
OOP style programming. The final result can be found in appendix E.

Here is an overview guide of the program:

![](media/image4.png){width="6.261805555555555in"
height="2.285416666666667in"}

TESTING:
========

I then moved onto the testing where I could verify that all the
algorithms were working correctly and where I could start to investigate
if it is possible for a poker AI to beat a human player. I started with
testing the actual functionality of the game, to ensure that it was
correctly dealing with inputs and playing through the game of poker
correctly.

### Game Functionality testing:

  -------------------------- ------------------------------------------------------------------ ------------------------------------------------- -------------------------------------------------------------------------------------------- -------------------------------------
  []{#_gjdgxs .anchor}N^o^   Purpose                                                            Test Data                                         Expected result                                                                              Actual Result (evidence appendix F)

  1.1                        The game launches without errors.                                  N/A.                                              Games launches and prints welcome text.                                                      Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.1)

  1.2                        The game successfully creates a new player object.                 Enter “Player name” in the name field.            Game starts the first round of betting.                                                      Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.2)

  1.3a                       The game is able to interpret a player’s move.                     Enter:                                            a.  Game recognises you wanted to fold and ends the round, declaring the AI as the winner.   a.  Pass. (1.3a)
                                                                                                                                                                                                                                               
  1.3b                                                                                          “f”                                               b.  Game asks how much you want to raise by.                                                 b.  Pass. (1.3b)
                                                                                                                                                                                                                                               
  1.3c                                                                                          “r”                                               c.  Game proceeds with the betting round                                                     c.  Pass. (1.3c)
                                                                                                                                                                                                                                               
                                                                                                “c”                                                                                                                                            
                                                                                                                                                                                                                                               
                                                                                                In the move field.                                                                                                                             

  1.4                        To see if the game correctly handles money.                        Enter “1000” in the raise field.                  The game deducts 1000 from the player’s wallet when raising.                                 Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.4)

  1.5                        To see if the card comparison algorithm works correctly.           Play until the end of a round.                    The player who had the better set of cards wins.                                             Pass, the human won with two pairs.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.5)

  1.6                        To see if the game is able to reset itself.                        Enter “y” in the reset field.                     The game resets each player’s money, score and game round.                                   Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.6)

  1.7                        To see if the game quits successfully.                             Enter “y” in the quit field.                      The game exits.                                                                              Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.7)

  1.8                        To see if the game displays relevant information about the game.   N/A                                               a.  It displays information about the money.                                                 a.  Pass. (1.8a)
                                                                                                                                                                                                                                               
                                                                                                                                                  b.  It displays information about the game score and round.                                  b.  Pass. (1.8b)
                                                                                                                                                                                                                                               
                                                                                                                                                  c.  The game displays information about player’s cards and the table cards.                  c.  Pass. (1.8c)
                                                                                                                                                                                                                                               
                                                                                                                                                  d.  The game shows information about the winner.                                             d.  Pass. (1.8d)
                                                                                                                                                                                                                                               

  1.9                        The game is able to correctly carry out an entire betting round    Play normally until the end of a betting round.   The game displays relevant information and doesn’t run into any errors as I play.            Pass.
                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                               (1.9)
  -------------------------- ------------------------------------------------------------------ ------------------------------------------------- -------------------------------------------------------------------------------------------- -------------------------------------

Then I moved on to test the integration of the AI within the poker game
to ensure that both algorithms were able to communicate successfully and
effectively.

### AI-Game communication testing:

  ------ --------------------------------------------------------- ------------------------------------------------------------------------------------- ------------------------------------- -------------------------------------
  N^o^   Purpose                                                   Test Data                                                                             Expected result                       Actual Result (evidence appendix F)

  2.1    To see if the AI can make a move within the game.         N/A                                                                                   AI calls / folds / raises.            Pass.
                                                                                                                                                                                               
                                                                                                                                                                                               (2.1)

  2.2    To see if the AI can handle the human player folding.     Run the program and fold on the first turn. Then see if the AI functions next game.   Human folds, AI wins.                 Pass.
                                                                                                                                                                                               
                                                                                                                                                         You are now on round 2 of the game.   (2.2)
                                                                                                                                                                                               
                                                                                                                                                         AI plays as normal.                   

  2.3    To see if the AI is able to play after multiple resets.   Fold several times over and reset the game multiple times.                            AI plays as normal.                   Pass.
                                                                                                                                                                                               
                                                                                                                                                                                               (2.3)
  ------ --------------------------------------------------------- ------------------------------------------------------------------------------------- ------------------------------------- -------------------------------------

Afterwards I then tested that the dataset was being read correctly by
the AI and to see if the AI was learning off of it.

### Tests to see if the AI is reading the dataset correctly.

  ------ ------------------------------------------------------------------------- ------------------------------------------------------- ----------------- -------------------------------------
  N^o^   Purpose                                                                   Test Data                                               Expected result   Actual Result (evidence appendix F)

  3.1a   To see if the AI makes the correct move according to the dataset given.   Give the AI cards that you would expect it to bet on:   a.  AI raises.    a.  Pass. (3.1a)
                                                                                                                                                             
  3.1b                                                                             a.  8D, QH                                              b.  AI folds.     b.  Pass. (3.1b)
                                                                                                                                                             
                                                                                   b.  3H, 2H                                                                
                                                                                                                                                             
  ------ ------------------------------------------------------------------------- ------------------------------------------------------- ----------------- -------------------------------------

Finally I tested whether it is possible for a poker AI to beat a human
player in order to get a conclusion for my investigation.

### Tests to see if the AI can outperform a human:

  ------------ --------------------------- ------------------- ---------------- ------------------------------------
  Round N^o^   Cards                       Method of winning   Players money    Game results (evidence appendix F)

  1            AI: QH, 2D                  Fold.               AI: 1,000,100    AI wins.
                                                                                
               Human: 2H, 2C                                   Human: 999,900   (4.1)
                                                                                
               Table: ?                                                         

  2            AI: JD, 5D                  Showdown.           AI: 995,168      Human wins.
                                                                                
               Human: JS, TS                                   Human: 994,958   (4.2)
                                                                                
               Table: KH, 2S, KD, 5H, 5C                                        

  3            AI: 8S, KC                  Showdown.           AI: 1,000,131    AI wins.
                                                                                
               Human: 9S, JH                                   Human: 999,869   (4.3)
                                                                                
               Table: 6H, 3C, TH, QC, 4D                                        

  4            AI: JC, QD                  Showdown.           AI: 1,050,523    AI wins.
                                                                                
               Human: QS, 8D                                   Human: 944,807   (4.4)
                                                                                
               Table: 4S, 9C, TC, 7C, 8C                                        

  5            AI: 9D, 6D                  Showdown.           AI: 1,058,863    AI wins.
                                                                                
               Human: 3S, KS                                   Human: 940,037   (4.5)
                                                                                
               Table: TD, 9H, 7D, 6S, 7H                                        

  6            AI: JS, 2D                  Showdown.           AI: 1,039,868    Human wins.
                                                                                
               Human: KH, 7C                                   Human: 953,821   (4.6)
                                                                                
               Table: 4C, 4H, 3D, QH, 3S                                        

  7            AI: 4C, 7H                  Showdown.           AI: 1,055,066    AI wins.
                                                                                
               Human: 9H, 8S                                   Human: 938,623   (4.7)
                                                                                
               Table: 6H, AD, QC, 5S, 8H                                        

  8            AI: 2S, JH                  Fold.               AI: 1,055,166    AI wins.
                                                                                
               Human: 3D, 7D                                   Human: 938,523   (4.8)
                                                                                
               Table: ?                                                         

  9            AI: 9S, 6S                  Showdown.           AI: 1,054,066    Human wins.
                                                                                
               Human: KS, JC                                   Human: 939,623   (4.9)
                                                                                
               Table: 2C, TS, QS, 7C, TD                                        

  10           AI: 5H, 6C                  Showdown.           AI: 1,048,775    Human wins.
                                                                                
               Human: 7S, 5D                                   Human: 951,225   (4.10)
                                                                                
               Table: KH, KC, 5C, AC, 2D                                        
  ------------ --------------------------- ------------------- ---------------- ------------------------------------

EVALUATION:
===========

To evaluate and assess how well I carried out this investigation I must
see if my solution meets the requirements.

I feel that my solution meets most, if not all, requirements I set out
to complete. The testing shows that the following requirements were met.

  Requirement   Met?   Explanation
  ------------- ------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1             ✓      As evidenced in the screenshot the user was clearly able to see their cards and the table cards as well as input there desired action.
  2             ✓      The program was successfully able to deal cards to all positions and not draw duplicates.
  3             ✓      The second stage of testing showed that the AI was successfully able to communicate with the game.
  4             ✓      As it was demonstrated all throughout my testing that the game was able to constantly transfer money between the players and the pot, rewarding the winner with all the money acquired in the pot at the end of a game.
  5             ✓      The game was successfully able to determine a winner, as shown in the final stage of testing, if a player folded, if a player’s money ran out or if it came to the showdown, a winner was picked.
  6             ✓      It was shown that in the last stage of testing as the game was clearly able to determine when a round of betting was over.
  7             ✓      The testing in stage 2 and 4 shows that the AI could make moves within the game and receive its cards and money.
  8             ✓      In the 3^rd^ stage of testing where I tested if the AI was able to access a dataset and make a correct move when asked.

Since all of my requirements were met this provides a fair platform to
put my investigation to test. However if I were to revisit this
investigation I would have introduced more validation into the poker
game to insure no foul input could be made. I would also create my own
hand evaluation algorithm that would be more tailored to my game of
poker. In addition to this I would have created a better dataset that
does not just work off probabilities. Finally if I had extra time I
would make the AI self-learning, so that after each game it played it
would update the dataset appropriately according to what happened during
that previous game.

To conclude, my investigation was to find out if it is possible to
produce an AI that will earn more money from playing Texas hold’em than
a human in 10 games. To test this I played my best against the AI for
the duration of 10 games of poker and measured the amount of money each
player had at the end of it. The final testing stage showed that AI is
capable of playing poker better than an average human poker player as it
beat me by making a profit of 48,775 over the duration of 10 games.

APPENDICIES:
============

### A: Higher lower standard gradient descent neural network.

1.  **import** numpy **as** np

2.   

3.  *\#make sigma*

4.  **def** sigma(x):  

5.      **return** 1/(1+np.exp(-x))

6.   

7.  *\#sigma gradient*

8.  **def** sigma\_deriv(x):

9.      **return** x\*(1-x)

10.  

11. *\#define datasets*

12. x = np.array((\[\[0\],\[12\],\[4\],\[7\]\]), dtype=float)

13. y = np.array(\[\[1\],\[0\],\[1\],\[0\]\])

14.  

15. *\#normalise*

16. x = x/12

17.  

18. *\#weights*

19. w0 = 2\*np.random.random((1,4))-1

20. w1 = 2\*np.random.random((4,4))-1

21. w2 = 2\*np.random.random((4,4))-1

22. w3 = 2\*np.random.random((4,1))-1

23.  

24. *\#train*

25. **for** t **in** xrange(100000):

26.    

27.     *\#forward propagation*

28.     l0 = x

29.     l1 = sigma(np.dot(l0, w0))

30.     l2 = sigma(np.dot(l1, w1))

31.     l3 = sigma(np.dot(l2, w2))

32.     l4 = sigma(np.dot(l3, w3))

33.    

34.     *\#error + change calc*

35.     l4\_error = y - l4    

36.     l4\_change = l4\_error\*sigma\_deriv(l4)

37.     l3\_error = l4\_change.dot(w3.T)

38.     l3\_change = l3\_error \* sigma\_deriv(l3)

39.     l2\_error = l3\_change.dot(w2.T)

40.     l2\_change = l2\_error \* sigma\_deriv(l2)

41.     l1\_error= l2\_change.dot(w1.T)

42.     l1\_change = l1\_error \* sigma\_deriv(l1)

43.    

44.     *\#update weights*

45.     w3 += np.dot(l3.T, l4\_change)

46.     w2 += np.dot(l2.T, l3\_change)

47.     w1 += np.dot(l1.T, l2\_change)

48.     w0 += np.dot(l0.T, l1\_change)

49.  

50. **print** "Output after training"

51. **print** l4

52.  

53. *\#user entry*

54. c = raw\_input("Card: ")

55. C = np.array((\[\[c\]\]), dtype=float)

56.  

57. *\#normalise*

58. C = C/12

59.  

60. **print** sigma(np.dot(sigma(np.dot(sigma(np.dot(sigma(np.dot(C, w0)), w1)), w2)), w3))

### B: datatrain.py – dataset creation.

1.  **import** itertools, random, sys, math, time, csv

2.  **from** random **import** randint

3.  **from** time **import** sleep

4.  **import** numpy **as** np

5.   

6.  **def** main():

7.      setup()

8.      train()

9.      DataSet().csvList()

10.  

11. **def** setup():

12.     CardPile().reset()

13.     CardPile().setList()

14.  

15. **def** train():

16.     **for** x **in** xrange(0,52):

17.         **for** y **in** xrange(0,52):

18.             **if** x!=y:

19.                 tp = TrainPlayer((x,y))

20.                
    tp.setCards((CardPile().getSpecCard(tp.getCardNo()\[0\]),CardPile().getSpecCard(tp.getCardNo()\[1\])))

21.                 **for** i **in** xrange(0,52):

22.                     **for** j **in** xrange(0,52):

23.                      
      **if** i!=j **and** i!=x **and** i!=y **and** j!=x **and** j!=y **and** x!=y:

24.                             op = OppPlayer((i,j))

25.                            
    op.setCards((CardPile().getSpecCard(op.getCardNo()\[0\]),CardPile().getSpecCard(op.getCardNo()\[1\])))

26.                             **for** epoch **in** xrange(0,100):

27.                                
    tbl = Table(\[CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard(),CardPile().getRandCard()\])

28.                                
    tp.setPoints(int(Compare().cardCompare(tp.getCards(),op.getCards(),tbl.getCards())))

29.                                 CardPile().reset()

30.                                
    CardPile().usedCardAdd(tp.getCards()\[0\])

31.                                
    CardPile().usedCardAdd(tp.getCards()\[1\])

32.                                
    CardPile().usedCardAdd(op.getCards()\[0\])

33.                                
    CardPile().usedCardAdd(op.getCards()\[1\])

34.                             **del** op

35.                
    DataSet().setPoint(tp.getCards()\[0\],tp.getCards()\[1\],tp.getPoints())

36.                 **print** tp.getCards()

37.                 **del** tp

38.                        

39.                

40. **class** Compare:

41.     \_\_allTcards = \[\]

42.     \_\_all0cards = \[\]

43.     **def** cardCompare(self,tpc,opc,tblc):

44.      
      self.\_\_allTcards = \[tpc\[0\], tpc\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

45.      
      self.\_\_allOcards = \[opc\[0\], opc\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

46.      
      **if** self.evaluateCard(self.\_\_allTcards) &gt; self.evaluateCard(self.\_\_allOcards):

47.             **return** 1

48.      
      **elif** self.evaluateCard(self.\_\_allOcards) &gt; self.evaluateCard(self.\_\_allTcards):

49.             **return** 0

50.         **else**:

51.             **return** 0

52.  

53.     **def** evaluateCard(self,hand):

54.        
    groups = self.group(\['--23456789TJQKA'.index(r) **for** r, s **in** hand\])

55.         counts, ranks = zip(\*groups)

56.         **if** ranks == (14, 5, 4, 3, 2):

57.             ranks = (5, 4, 3, 2, 1)

58.        
    straight = len(ranks) == 5 **and** max(ranks)-min(ranks) == 4

59.         flush = len(set(\[s **for** r, s **in** hand\])) == 1

60.         **return** (

61.             9 **if** (5, ) == counts **else**

62.             8 **if** straight **and** flush **else**

63.             7 **if** (4, 1) == counts **else**

64.             6 **if** (3, 2) == counts **else**

65.             5 **if** flush **else**

66.             4 **if** straight **else**

67.             3 **if** (3, 1, 1) == counts **else**

68.             2 **if** (2, 2, 1) == counts **else**

69.             1 **if** (2, 1, 1, 1) == counts **else**

70.             0), ranks

71.  

72.     **def** group(self,items):

73.         groups = \[(items.count(x), x) **for** x **in** set(items)\]

74.         **return** sorted(groups, reverse = True)

75.  

76. **class** Table:

77.     \_\_flop1 = \[\]

78.     \_\_flop2 = \[\]

79.     \_\_flop3 = \[\]

80.     \_\_turn = \[\]

81.     \_\_river = \[\]

82.     **def** \_\_init\_\_(self,cards):

83.         self.\_\_flop1 = cards\[0\]

84.         self.\_\_flop2 = cards\[1\]

85.         self.\_\_flop3 = cards\[2\]

86.         self.\_\_turn = cards\[3\]

87.         self.\_\_river = cards\[4\]

88.     **def** getCards(self):

89.      
      **return** \[self.\_\_flop1, self.\_\_flop2, self.\_\_flop3, self.\_\_turn, self.\_\_river\]

90.  

91. **class** Player:

92.     \_\_cardNo = \[\]

93.     \_\_cards = \[\]

94.     **def** \_\_init\_\_(self, cardNo):

95.         self.\_\_cardNo = cardNo

96.     **def** getCardNo(self):

97.         **return** self.\_\_cardNo

98.     **def** setCards(self,cards):

99.         self.\_\_cards = cards

100.     **def** getCards(self):

101.         **return** self.\_\_cards

102.  

103. **class** TrainPlayer(Player):

104.     \_\_points = 0

105.     **def** \_\_init\_\_(self, cardNo):

106.         Player.\_\_init\_\_(self, cardNo)

107.     **def** getCardNo(self):

108.         **return** Player.getCardNo(self)

109.     **def** setCards(self,cards):

110.         Player.setCards(self,cards)

111.     **def** getCards(self):

112.         **return** Player.getCards(self)

113.     **def** setPoints(self, points):

114.         self.\_\_points += points

115.     **def** getPoints(self):

116.         **return** self.\_\_points

117.  

118. **class** OppPlayer(Player):

119.     **def** \_\_init\_\_(self, cardNo):

120.         Player.\_\_init\_\_(self, cardNo)

121.     **def** getCardNo(self):

122.         **return** Player.getCardNo(self)

123.     **def** setCards(self,cards):

124.         Player.setCards(self, cards)

125.     **def** getCards(self):

126.         **return** Player.getCards(self)

127.  

128. **class** CardPile:

129.    
    \_\_deck = \[r+s **for** r **in** '23456789TJQKA' **for** s **in** 'SHDC'\]

130.     \_\_usedCards  = \[\]

131.     \_\_list = \[\]

132.     **def** getSpecCard(self,cardneeded):

133.         \_\_specCard = self.\_\_deck\[cardneeded\]

134.         self.\_\_usedCards.append(\_\_specCard)

135.         **return** \_\_specCard

136.     **def** getRandCard(self):

137.         **while** True:

138.             \_\_randCard = self.\_\_deck\[randint(0,51)\]

139.             **if** \_\_randCard **not** **in** self.\_\_usedCards:

140.                 self.\_\_usedCards.append(\_\_randCard)

141.                 **return** \_\_randCard

142.                 **break**

143.     **def** setList(self):

144.         **for** x **in** xrange(0,52):

145.             **for** y **in** xrange(0,52):

146.                 **if** y != x:

147.                     self.\_\_list.append((x,y))

148.     **def** getList(self):

149.         **return** self.\_\_list

150.     **def** reset(self):

151.         **del** self.\_\_usedCards\[:\]

152.     **def** usedCardAdd(self, card):

153.         self.\_\_usedCards.append(card)

154.        

155. **class** DataSet:

156.     \_\_cardList = \[\]

157.     \_\_pointList = \[\]

158.     \_\_floatList = \[\]

159.     \_\_predList = \[\]

160.     **def** setPoint(self,card1,card2,point):

161.         self.\_\_cardList.append(self.processCards(card1,card2))

162.         self.\_\_pointList.append(\[point\])

163.     **def** getPoint(self,pos):

164.      
      **return** (self.\_\_cardList\[pos\], self.\_\_pointList\[pos\])

165.     **def** processCards(self,card1,card2):

166.         **if** card1\[:1\] == 'T': c1 = 10

167.         **elif** card1\[:1\] == 'J': c1 = 11

168.         **elif** card1\[:1\] == 'Q': c1 = 12

169.         **elif** card1\[:1\] == 'K': c1 = 13

170.         **elif** card1\[:1\] == 'A': c1 = 14

171.         **else**: c1 = int(card1\[:1\])

172.         **if** card2\[:1\] == 'T': c2 = 10

173.         **elif** card2\[:1\] == 'J': c2 = 11

174.         **elif** card2\[:1\] == 'Q': c2 = 12

175.         **elif** card2\[:1\] == 'K': c2 = 13

176.         **elif** card2\[:1\] == 'A': c2 = 14

177.         **else**: c2 = int(card2\[:1\])

178.         **if** card1\[-1:\]==card2\[-1:\]: s = 1

179.         **else**: s = 0

180.         c1 = float(c1)/14

181.         c2 = float(c2)/14

182.         **return** \[c1,c2,s\]

183.     **def** pointFloat(self):

184.         maxPoint = max(self.\_\_pointList)\[0\]

185.      
      self.\_\_floatList = \[\[float(j)/maxPoint **for** j **in** i\] **for** i **in** self.\_\_pointList\]

186.     **def** makePred(self, x):

187.         **return**(

188.             1 **if** x &gt;= 0.6 **else**

189.             0)

190.     **def** makePredList(self):

191.      
      self.\_\_predList = \[\[self.makePred(x) **for** x **in** z\] **for** z **in** self.\_\_floatList\]

192.     **def** csvList(self):

193.         **with** open('handstrained.csv', 'wb') **as** myfile:

194.             wr = csv.writer(myfile, delimiter=',')

195.             **for** z **in** xrange(0,len(self.\_\_cardList)):

196.                 wr.writerow(self.\_\_cardList\[z\])

197.      
      **with** open('correctpredtrainedUN.csv', 'wb') **as** myfile:

198.             wr = csv.writer(myfile, delimiter=',')

199.             **for** z **in** xrange(0,len(self.\_\_pointList)):

200.                 wr.writerow(self.\_\_pointList\[z\])

201.         self.pointFloat()

202.         self.makePredList()

203.      
      **with** open('correctpredtrainedfloat.csv', 'wb') **as** myfile:

204.             wr = csv.writer(myfile, delimiter=',')

205.             **for** z **in** xrange(0,len(self.\_\_floatList)):

206.                 wr.writerow(self.\_\_floatList\[z\])

207.      
      **with** open('correctpredtrained.csv', 'wb') **as** myfile:

208.             wr = csv.writer(myfile, delimiter=',')

209.             **for** z **in** xrange(0,len(self.\_\_predList)):

210.                 wr.writerow(self.\_\_predList\[z\])

211.  

212. main()

### C: Dataset

correctpredtrained.csv:

  Card1 float value (rank/14)   Card2 float value (rank/14)   Suited (1= suited, 0 = not suited)
  ----------------------------- ----------------------------- ------------------------------------
  0.1428571429                  0.1428571429                  0
  0.1428571429                  0.1428571429                  0
  0.1428571429                  0.1428571429                  0
  0.1428571429                  0.2142857143                  1
  0.1428571429                  0.2142857143                  0
  0.1428571429                  0.2142857143                  0

(Continued)

handstrained.csv:

  Correct prediction (1 = raise, 0 = fold)
  ------------------------------------------
  0
  0
  0
  0
  0
  0

(Continued)

### D: Higher lower stochastic gradient descent neural network.

1.  **import** numpy **as** np

2.  **import** csv, random, itertools

3.  **from** random **import** randint

4.   

5.  **class** sdg\_nn:

6.      \_\_action = ''

7.   

8.          *\#define datasets*

9.      \_\_x = np.genfromtxt('handstrained.csv', delimiter=',')

10.    
    \_\_y = np.genfromtxt('correctpredtrained.csv', delimiter=',')\[np.newaxis\]

11.     \_\_y = \_\_y.T

12.     *\#seed*

13.     np.random.seed(1)

14.     *\#weights*

15.     \_\_w0 = 2\*np.random.random((3,4))-1

16.     \_\_w1 = 2\*np.random.random((4,4))-1

17.     \_\_w2 = 2\*np.random.random((4,4))-1

18.     \_\_w3 = 2\*np.random.random((4,1))-1

19.     *\#raise check*

20.     \_\_allReadyRaise = False

21.    

22.     \_\_move = 0

23.    

24.     **def** setAction(self,card1,card2):

25.         self.\_\_action = self.predict(card1,card2)

26.     **def** getAction(self):

27.         **return** self.\_\_action

28.  

29.     **def** sigma(self,x):

30.         **return** 1/(1+np.exp(-x))

31.     *\#sigma gradient*

32.     **def** sigmaDeriv(self,x):

33.         **return** x\*(1-x)

34.     **def** predict(self,c01,c02):

35.         \_\_carray = self.processCards(c01,c02)

36.         **for** i **in** xrange(10):

37.             self.epoch()

38.         *\#predict*

39.         \_\_c1 = \_\_carray\[0\]

40.         \_\_c2 = \_\_carray\[1\]

41.         \_\_s = \_\_carray\[2\]

42.         \_\_C = np.array(\[\[\_\_c1,\_\_c2,\_\_s\]\])

43.      
      self.\_\_move = self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(\_\_C, self.\_\_w0)), self.\_\_w1)), self.\_\_w2)),self.\_\_w3))

44.        

45.      
      **if** self.\_\_move &gt;= 0.7 **and** self.\_\_allReadyRaise == False:

46.             self.\_\_allReadyRaise = True

47.             **return** 'r'

48.         **elif** self.\_\_move &gt;=0.5: **return** 'c'

49.         **else**: **return** 'f'

50.     **def** epoch(self):

51.         \_\_z=0

52.         *\#train*

53.         **for** t **in** xrange(len(self.\_\_y)/4):

54.             *\#forward propagation*

55.             \_\_l0 = self.\_\_x\[\_\_z:(\_\_z+5)\]

56.             \_\_l1 = self.sigma(np.dot(\_\_l0, self.\_\_w0))

57.             \_\_l2 = self.sigma(np.dot(\_\_l1, self.\_\_w1))

58.             \_\_l3 = self.sigma(np.dot(\_\_l2, self.\_\_w2))

59.             \_\_l4 = self.sigma(np.dot(\_\_l3, self.\_\_w3))

60.             *\#error + change calc*

61.             \_\_l4\_error = self.\_\_y\[\_\_z:(\_\_z+5)\] - \_\_l4  
     

62.             \_\_l4\_change = \_\_l4\_error\*self.sigmaDeriv(\_\_l4)

63.             \_\_l3\_error = \_\_l4\_change.dot(self.\_\_w3.T)

64.             \_\_l3\_change = \_\_l3\_error
    \* self.sigmaDeriv(\_\_l3)

65.             \_\_l2\_error = \_\_l3\_change.dot(self.\_\_w2.T)

66.             \_\_l2\_change = \_\_l2\_error
    \* self.sigmaDeriv(\_\_l2)

67.             \_\_l1\_error= \_\_l2\_change.dot(self.\_\_w1.T)

68.             \_\_l1\_change = \_\_l1\_error
    \* self.sigmaDeriv(\_\_l1)

69.             *\#update weights*

70.             self.\_\_w3 += np.dot(\_\_l3.T, \_\_l4\_change)

71.             self.\_\_w2 += np.dot(\_\_l2.T, \_\_l3\_change)

72.             self.\_\_w1 += np.dot(\_\_l1.T, \_\_l2\_change)

73.             self.\_\_w0 += np.dot(\_\_l0.T, \_\_l1\_change)

74.             \_\_z += 5

75.     **def** processCards(self,card01,card02):

76.         **if** card01\[:1\] == 'T': \_\_c1 = 10

77.         **elif** card01\[:1\] == 'J': \_\_c1 = 11

78.         **elif** card01\[:1\] == 'Q': \_\_c1 = 12

79.         **elif** card01\[:1\] == 'K': \_\_c1 = 13

80.         **elif** card01\[:1\] == 'A': \_\_c1 = 14

81.         **else**: \_\_c1 = int(card01\[:1\])

82.         **if** card02\[:1\] == 'T': \_\_c2 = 10

83.         **elif** card02\[:1\] == 'J': \_\_c2 = 11

84.         **elif** card02\[:1\] == 'Q': \_\_c2 = 12

85.         **elif** card02\[:1\] == 'K': \_\_c2 = 13

86.         **elif** card02\[:1\] == 'A': \_\_c2 = 14

87.         **else**: \_\_c2 = int(card02\[:1\])

88.         **if** card01\[-1:\]==card02\[-1:\]: \_\_s = 1

89.         **else**: \_\_s = 0

90.         \_\_c1 = float(\_\_c1)/14

91.         \_\_c2 = float(\_\_c2)/14

92.         **return** \[\_\_c1,\_\_c2,\_\_s\]

93.  

94. card1 = raw\_input("Card 1: ")

95. card2 = raw\_input("Card 2: ")

96. sdg\_nn().setAction(card1,card2)

97. **print** str(sdg\_nn().getAction())

###  E: poker.py – The final solution.

1.  *\#Import dependancies*

2.  **import** sys

3.  **from** random **import** randint

4.  **import** numpy **as** np

5.   

6.  **class** Game:

7.      \_\_gRound = 1 *\#game round*

8.      \_\_quit = False

9.      \_\_reset = False

10.     \_\_gName = '' *\#game name*

11.     \_\_ai = None

12.     \_\_human = None

13.     \_\_gameOver = ''

14.     \_\_table = None

15.  

16.     **def** \_\_init\_\_(self, gName):

17.         self.\_\_gName = gName

18.         **print** "Welcome to texas holdem!"

19.     **def** setupGame(self):

20.         self.\_\_human = Player(raw\_input("Please enter your name:
    "))

21.         self.\_\_ai = AI()

22.         self.\_\_table = Table()

23.         self.\_\_human.setMoney(1000000)

24.         self.\_\_ai.setMoney(1000000)

25.     **def** menu(self):

26.         **while** self.\_\_quit == False:

27.          
      **if** self.\_\_gRound == 1 **or** self.\_\_reset == True:

28.                 self.setupGame()

29.                 self.\_\_gRound = 1

30.             **print** "You are on round: " + str(self.\_\_gRound)

31.             CardPile().reset()

32.             self.setupCards()

33.             **print** "Congratulations " + str(self.playGame()) + ",
    you won!"

34.             **print** "The AI's cards were:
    " + str(self.\_\_ai.getCard())

35.             **print** str(self.\_\_human.getName()) + ", your cards
    were: " + str(self.\_\_human.getCard())

36.             **print** "The score is: AI:
    " + str(self.\_\_ai.getScore()) + " |
    " + str(self.\_\_human.getScore()) + "
    :" + str(self.\_\_human.getName()).upper()

37.          
      **if** self.\_\_gameOver == 'ai' **or** self.\_\_gameOver == 'human':

38.                 **print** "Since " + str(self.\_\_gameOver) + " ran
    out of money the game is over. The game will now be reset."

39.                 self.\_\_reset = True

40.                 **if** raw\_input("Would you like to quit the game?
    (y/n):") == 'y': self.\_\_quit = True

41.                 **else**: self.\_\_quit = False

42.             **else**:  

43.                 self.\_\_gRound = self.\_\_gRound + 1

44.                 **if** raw\_input("Would you like to reset the game?
    (y/n):") == 'y': self.\_\_reset = True

45.                 **else**: self.\_\_reset = False

46.                 **if** raw\_input("Would you like to quit the game?
    (y/n):") == 'y': self.\_\_quit = True

47.                 **else**: self.\_\_quit = False

48.         sys.exit()

49.     **def** setupCards(self):

50.         self.\_\_table.setCards()

51.         self.\_\_human.setCard()

52.         self.\_\_ai.setCard()

53.         self.\_\_ai.reset()

54.     **def** playGame(self):

55.         self.\_\_human.setMoney(-self.\_\_table.getEntryMoney())

56.         self.\_\_ai.setMoney(-self.\_\_table.getEntryMoney())

57.         self.\_\_table.setPot(2\*self.\_\_table.getEntryMoney())

58.         self.\_\_table.setNextPlayer('r')

59.         **if** self.bettingRound() == False:

60.             **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2))

61.             self.\_\_human.setAction('-')

62.             self.\_\_ai.setAction('-')

63.             **if** self.bettingRound() == False:

64.                 **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2)+",
    "+self.\_\_table.getCards(3))

65.                 self.\_\_human.setAction('-')

66.                 self.\_\_ai.setAction('-')

67.                 **if** self.bettingRound() == False:

68.                     **print** "The table's cards are:
    " + str(self.\_\_table.getCards(0)+",
    "+self.\_\_table.getCards(1)+", "+self.\_\_table.getCards(2)+",
    "+self.\_\_table.getCards(3)+", "+self.\_\_table.getCards(4))

69.                     self.\_\_human.setAction('-')

70.                     self.\_\_ai.setAction('-')

71.                     **if** self.bettingRound() == False:

72.                      
      self.\_\_table.setWinner(Compare().cardCompare(self.\_\_human.getCard(), self.\_\_ai.getCard(),\[self.\_\_table.getCards(0),self.\_\_table.getCards(1),self.\_\_table.getCards(2),self.\_\_table.getCards(3),self.\_\_table.getCards(4)\]))

73.                      
      **if** self.\_\_table.getWinner() == 'Human':

74.                          
      self.\_\_human.setMoney(self.\_\_table.getPot())

75.                             self.\_\_table.setPot(0)

76.                             self.\_\_human.setScore(1)

77.                          
      self.\_\_table.setWinnersCards(str(self.\_\_human.getCard()))

78.                             **return** str(self.\_\_human.getName())

79.                         **elif** self.\_\_table.getWinner() == 'AI':

80.                          
      self.\_\_ai.setMoney(self.\_\_table.getPot())

81.                             self.\_\_table.setPot(0)

82.                             self.\_\_ai.setScore(1)

83.                          
      self.\_\_table.setWinnersCards(str(self.\_\_ai.getCard()))

84.                             **return** 'AI'

85.                         **else**:

86.                          
      self.\_\_human.setMoney(self.\_\_table.getPot()/2)

87.                          
      self.\_\_ai.setMoney(self.\_\_table.getPot()/2)

88.                             self.\_\_table.setPot(0)

89.                             self.\_\_table.setWinnersCards('')

90.                             **return** 'no-one'

91.         **else**:

92.             **if** self.\_\_gameOver == 'ai':

93.                 **return** str(self.\_\_human.getName())

94.             **if** self.\_\_gameOver == 'human':

95.                 **return** 'AI'

96.             **elif** self.\_\_table.getWinner() == 'Human':

97.              
      self.\_\_table.setWinnersCards(str(self.\_\_human.getCard()))

98.                 **return** str(self.\_\_human.getName())

99.             **elif** self.\_\_table.getWinner() == 'AI':

100.              
      self.\_\_table.setWinnersCards(str(self.\_\_ai.getCard()))

101.                 **return** 'AI'

102.             **else**:

103.                 self.\_\_table.setWinnersCards('')

104.                 **return** 'no-one'

105.     **def** checkMoney(self,flag):

106.      
      **if** int(self.\_\_human.getMoney()) &lt; 0 **and** flag == False:

107.                     self.\_\_gameOver = 'human'

108.                     self.\_\_table.setWinner('AI')

109.                     self.\_\_table.setWon('t')

110.                     self.\_\_ai.setScore(1)

111.                     **return** True

112.      
      **elif** int(self.\_\_ai.getMoney()) &lt; 0 **and** flag == False:

113.                     self.\_\_gameOver = 'ai'

114.                     self.\_\_table.setWinner('Human')

115.                     self.\_\_table.setWon('t')

116.                     self.\_\_human.setScore(1)

117.                     **return** True

118.         **elif** flag == True: **return** True

119.         **else**: **return** False

120.     **def** bettingRound(self):

121.         self.\_\_table.setWon('f')

122.         \_\_flag = False

123.         **if** self.\_\_table.getNextPlayer() == 1:

124.             **while** \_\_flag == False:

125.                 \_\_flag = self.checkMoney(\_\_flag)

126.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

127.                 **print** "AI money:
    " + str(self.\_\_ai.getMoney())

128.                 **print** "Pot: " + str(self.\_\_table.getPot())

129.                 **if** \_\_flag == False:

130.                  
      **if** self.bettingRoundHuman()== True **and** \_\_flag == False:

131.                         self.\_\_table.setNextPlayer('a')

132.                         \_\_flag = True

133.                 \_\_flag = self.checkMoney(\_\_flag)

134.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

135.                 **print** "AI money:
    " + str(self.\_\_ai.getMoney())

136.                 **print** "Pot: " + str(self.\_\_table.getPot())

137.                 **if** \_\_flag == False:

138.                  
      **if** self.bettingRoundAi() == True **and** \_\_flag == False:

139.                         self.\_\_table.setNextPlayer('h')

140.                         \_\_flag = True

141.         **elif** self.\_\_table.getNextPlayer() == 2:

142.             **while** \_\_flag == False:

143.                 \_\_flag = self.checkMoney(\_\_flag)

144.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

145.                 **print** "AI money:
    " + str(self.\_\_ai.getMoney())

146.                 **print** "Pot: " + str(self.\_\_table.getPot())

147.                 **if** \_\_flag == False:

148.                  
      **if** self.bettingRoundAi()== True **and** \_\_flag == False:

149.                         self.\_\_table.setNextPlayer('h')

150.                         \_\_flag = True

151.                 \_\_flag = self.checkMoney(\_\_flag)

152.                 **print** "Your money:
    " + str(self.\_\_human.getMoney())

153.                 **print** "AI money:
    " + str(self.\_\_ai.getMoney())

154.                 **print** "Pot: " + str(self.\_\_table.getPot())

155.                 **if** \_\_flag == False:

156.                  
      **if** self.bettingRoundHuman() == True **and** \_\_flag == False:

157.                         self.\_\_table.setNextPlayer('a')

158.                         \_\_flag = True

159.         **if** self.\_\_table.getWon() == True:

160.             **return** True

161.         **else**:

162.             **return** False

163.     **def** bettingRoundAi(self):

164.         self.\_\_ai.setAction('x')

165.         **if** self.\_\_ai.getAction() == 'f':

166.             **print** "AI folds with the cards:
    " + str(self.\_\_ai.getCard())

167.             self.\_\_human.setMoney(self.\_\_table.getPot())

168.             self.\_\_table.setPot(0)

169.             self.\_\_human.setScore(1)

170.             self.\_\_table.setWinner('Human')

171.             self.\_\_table.setWon('t')

172.             **return** True

173.         **elif** self.\_\_ai.getAction() == 'r':

174.             self.\_\_ai.setRaiseAmount()

175.             self.\_\_ai.setMoney(-self.\_\_ai.getRaiseAmount())

176.             self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

177.             **print** "AI raises by
    " + str(self.\_\_ai.getRaiseAmount())

178.             **if** self.\_\_human.getAction() == 'r':

179.              
      self.\_\_ai.setMoney(-self.\_\_human.getRaiseAmount())

180.              
      self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

181.                 self.\_\_table.setWon('f')

182.                 **return** False

183.             **elif** self.\_\_human.getAction() == 'c':

184.                 self.\_\_table.setWon('f')

185.                 **return** False

186.             **else**:

187.                 self.\_\_table.setWon('f')

188.                 **return** False

189.         **elif** self.\_\_ai.getAction() == 'c':

190.             **print** "AI calls"

191.             **if** self.\_\_human.getAction() ==  'r':

192.              
      self.\_\_ai.setMoney(-self.\_\_human.getRaiseAmount())

193.              
      self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

194.                 self.\_\_table.setWon('f')

195.                 **return** False

196.             **elif** self.\_\_human.getAction() == 'c':

197.                 self.\_\_table.setWon('f')

198.                 **return** True

199.             **else**:

200.                 self.\_\_table.setWon('f')

201.                 **return** False

202.     **def** bettingRoundHuman(self):

203.         **print** str(self.\_\_human.getName())+", your cards are:
    " + str(self.\_\_human.getCard())

204.         self.\_\_human.setAction(raw\_input("What is your move?
    (r/c/f): "))

205.         **if** self.\_\_human.getAction() == 'f':

206.             self.\_\_ai.setMoney(self.\_\_table.getPot())

207.             self.\_\_table.setPot(0)

208.             self.\_\_ai.setScore(1)

209.             self.\_\_table.setWinner('AI')

210.             self.\_\_table.setWon('t')

211.             **return** True

212.         **elif** self.\_\_human.getAction() == 'r':

213.             self.\_\_human.setRaiseAmount(input("Raise by: "))

214.          
      self.\_\_human.setMoney(-self.\_\_human.getRaiseAmount())

215.             self.\_\_table.setPot(self.\_\_human.getRaiseAmount())

216.             **if** self.\_\_ai.getAction() == 'r':

217.              
      self.\_\_human.setMoney(-self.\_\_ai.getRaiseAmount())

218.                 self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

219.                 self.\_\_table.setWon('f')

220.                 **return** False

221.             **elif** self.\_\_ai.getAction() == 'c':

222.                 self.\_\_table.setWon('f')

223.                 **return** False

224.             **else**:

225.                 self.\_\_table.setWon('f')

226.                 **return** False

227.         **elif** self.\_\_human.getAction() == 'c':

228.             **if** self.\_\_ai.getAction() == 'c':

229.                 self.\_\_table.setWon('f')

230.                 **return** True

231.             **elif** self.\_\_ai.getAction() ==  'r':

232.              
      self.\_\_human.setMoney(-self.\_\_ai.getRaiseAmount())

233.                 self.\_\_table.setPot(self.\_\_ai.getRaiseAmount())

234.                 self.\_\_table.setWon('f')

235.                 **return** False

236.             **else**:

237.                 self.\_\_table.setWon('f')

238.                 **return** False

239. **class** Table:

240.     \_\_flop1 = \[\]

241.     \_\_flop2 = \[\]

242.     \_\_flop3 = \[\]

243.     \_\_turn = \[\]

244.     \_\_river = \[\]

245.     \_\_entryMoney = 100

246.     \_\_pot = 0

247.     \_\_won = None

248.     \_\_winner = ''

249.     \_\_nextPlayer = None

250.     \_\_winnersCards = ''

251.  

252.     **def** setCards(self):

253.         self.\_\_flop1 = CardPile().getCard()

254.         self.\_\_flop2 = CardPile().getCard()

255.         self.\_\_flop3 = CardPile().getCard()

256.         self.\_\_turn = CardPile().getCard()

257.         self.\_\_river = CardPile().getCard()

258.     **def** getCards(self, amount):

259.      
      **return** \[self.\_\_flop1, self.\_\_flop2, self.\_\_flop3, self.\_\_turn, self.\_\_river\]\[amount\]

260.     **def** getEntryMoney(self):

261.         **return** self.\_\_entryMoney

262.     **def** setPot(self, amount):

263.         **if** amount == 0: self.\_\_pot = amount

264.         **else**: self.\_\_pot += amount

265.     **def** getPot(self):

266.         **return** self.\_\_pot

267.     **def** setWinner(self,winner):

268.         self.\_\_winner = str(winner)

269.     **def** getWinner(self):

270.         **return** self.\_\_winner

271.     **def** setWon(self,tf):

272.         **if** tf == 't': self.\_\_won = True

273.         **elif** tf == 'f': self.\_\_won = False

274.     **def** getWon(self):

275.         **return** self.\_\_won

276.     **def** setNextPlayer(self, x):

277.         **if** x == 'r':

278.             **if** randint(0,100) &gt;= 50:

279.                 self.\_\_nextPlayer = 1

280.             **else**:

281.                 self.\_\_nextPlayer = 2

282.         **elif** x == 'h':

283.             self.\_\_nextPlayer = 1

284.         **else**:

285.             self.\_\_nextPlayer = 2

286.     **def** getNextPlayer(self):

287.         **return** self.\_\_nextPlayer

288.     **def** setWinnersCards(self,x):

289.         self.\_\_winnersCards = str(x)

290.     **def** getWinnersCards(self):

291.         **return** self.\_\_winnersCards

292.  

293. **class** Player:

294.     \_\_card1 = \[\]

295.     \_\_card2 = \[\]

296.     \_\_money = 0

297.     \_\_score = 0

298.     \_\_action = ''

299.     \_\_raiseAmount = 0

300.     \_\_name = ''

301.  

302.     **def** \_\_init\_\_(self, name):

303.         self.\_\_name = name

304.     **def** setCard(self):

305.         self.\_\_card1 = CardPile().getCard()

306.         self.\_\_card2 = CardPile().getCard()

307.     **def** getCard(self):

308.         **return** \[self.\_\_card1, self.\_\_card2\]

309.     **def** setMoney(self, amount):

310.         self.\_\_money += amount

311.     **def** getMoney(self):

312.         **return** self.\_\_money

313.     **def** setScore(self, amount):

314.         self.\_\_score += amount

315.     **def** getScore(self):

316.         **return** self.\_\_score

317.     **def** setAction(self, action):

318.         self.\_\_action = action

319.     **def** getAction(self):

320.         **return** self.\_\_action

321.     **def** setRaiseAmount(self, amount):

322.         self.\_\_raiseAmount = amount

323.     **def** getRaiseAmount(self):

324.         **return** self.\_\_raiseAmount

325.     **def** setName(self, name):

326.         self.\_\_name = name

327.     **def** getName(self):

328.         **return** self.\_\_name

329.  

330. **class** AI(Player):

331.     *\#define datasets*

332.     \_\_x = np.genfromtxt('handstrained.csv', delimiter=',')

333.    
    \_\_y = np.genfromtxt('correctpredtrained.csv', delimiter=',')\[np.newaxis\]

334.     \_\_y = \_\_y.T

335.     *\#seed*

336.     np.random.seed(1)

337.     *\#weights*

338.     \_\_w0 = 2\*np.random.random((3,4))-1

339.     \_\_w1 = 2\*np.random.random((4,4))-1

340.     \_\_w2 = 2\*np.random.random((4,4))-1

341.     \_\_w3 = 2\*np.random.random((4,1))-1

342.     *\#raise check*

343.     \_\_allReadyRaise = False

344.    

345.     \_\_move = 0

346.    

347.     **def** \_\_init\_\_(self):

348.         Player.\_\_init\_\_(self, 'AI')

349.     **def** setCard(self):

350.         Player.setCard(self)

351.     **def** getCard(self):

352.         **return** Player.getCard(self)

353.     **def** setMoney(self, amount):

354.         Player.setMoney(self, amount)

355.     **def** getMoney(self):

356.         **return** Player.getMoney(self)

357.     **def** setScore(self, amount):

358.         Player.setScore(self, amount)

359.     **def** getScore(self):

360.         **return** Player.getScore(self)

361.     **def** setAction(self,x):

362.         **if** x == '-':

363.            Player.setAction(self, x)

364.         **else**:

365.            
    Player.setAction(self, self.predict(Player.getCard(self)\[0\],Player.getCard(self)\[1\]))

366.     **def** getAction(self):

367.         **return** Player.getAction(self)

368.     **def** setRaiseAmount(self):

369.            
    Player.setRaiseAmount(self, int(\*(self.\_\_move)\*(Player.getMoney(self)/2))/100)

370.     **def** getRaiseAmount(self):

371.         **return** Player.getRaiseAmount(self)

372.     **def** reset(self):

373.         self.\_\_allReadyRaise = False

374.     *\#make sigma*

375.     **def** sigma(self,x):

376.         **return** 1/(1+np.exp(-x))

377.     *\#sigma gradient*

378.     **def** sigmaDeriv(self,x):

379.         **return** x\*(1-x)

380.     **def** predict(self,card1,card2):

381.         \_\_carray = self.processCards(card1,card2)

382.         **for** i **in** xrange(10):

383.             self.epoch()

384.         *\#predict*

385.         \_\_c1 = \_\_carray\[0\]

386.         \_\_c2 = \_\_carray\[1\]

387.         \_\_s = \_\_carray\[2\]

388.         \_\_C = np.array(\[\[\_\_c1,\_\_c2,\_\_s\]\])

389.      
      self.\_\_move = self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(self.sigma(np.dot(\_\_C, self.\_\_w0)), self.\_\_w1)), self.\_\_w2)),self.\_\_w3))

390.        

391.      
      **if** self.\_\_move &gt;= 0.7 **and** self.\_\_allReadyRaise == False:

392.             self.\_\_allReadyRaise = True

393.             **return** 'r'

394.         **elif** self.\_\_move &gt;=0.5: **return** 'c'

395.         **else**: **return** 'f'

396.     **def** epoch(self):

397.         \_\_z=0

398.         *\#train*

399.         **for** t **in** xrange(len(self.\_\_y)/4):

400.             *\#forward propagation*

401.             \_\_l0 = self.\_\_x\[\_\_z:(\_\_z+5)\]

402.             \_\_l1 = self.sigma(np.dot(\_\_l0, self.\_\_w0))

403.             \_\_l2 = self.sigma(np.dot(\_\_l1, self.\_\_w1))

404.             \_\_l3 = self.sigma(np.dot(\_\_l2, self.\_\_w2))

405.             \_\_l4 = self.sigma(np.dot(\_\_l3, self.\_\_w3))

406.             *\#error + change calc*

407.             \_\_l4\_error = self.\_\_y\[\_\_z:(\_\_z+5)\] - \_\_l4
       

408.             \_\_l4\_change = \_\_l4\_error\*self.sigmaDeriv(\_\_l4)

409.             \_\_l3\_error = \_\_l4\_change.dot(self.\_\_w3.T)

410.             \_\_l3\_change = \_\_l3\_error
    \* self.sigmaDeriv(\_\_l3)

411.             \_\_l2\_error = \_\_l3\_change.dot(self.\_\_w2.T)

412.             \_\_l2\_change = \_\_l2\_error
    \* self.sigmaDeriv(\_\_l2)

413.             \_\_l1\_error= \_\_l2\_change.dot(self.\_\_w1.T)

414.             \_\_l1\_change = \_\_l1\_error
    \* self.sigmaDeriv(\_\_l1)

415.             *\#update weights*

416.             self.\_\_w3 += np.dot(\_\_l3.T, \_\_l4\_change)

417.             self.\_\_w2 += np.dot(\_\_l2.T, \_\_l3\_change)

418.             self.\_\_w1 += np.dot(\_\_l1.T, \_\_l2\_change)

419.             self.\_\_w0 += np.dot(\_\_l0.T, \_\_l1\_change)

420.             \_\_z += 5

421.     **def** processCards(self,card1,card2):

422.         **if** card1\[:1\] == 'T': \_\_c1 = 10

423.         **elif** card1\[:1\] == 'J': \_\_c1 = 11

424.         **elif** card1\[:1\] == 'Q': \_\_c1 = 12

425.         **elif** card1\[:1\] == 'K': \_\_c1 = 13

426.         **elif** card1\[:1\] == 'A': \_\_c1 = 14

427.         **else**: \_\_c1 = int(card1\[:1\])

428.         **if** card2\[:1\] == 'T': \_\_c2 = 10

429.         **elif** card2\[:1\] == 'J': \_\_c2 = 11

430.         **elif** card2\[:1\] == 'Q': \_\_c2 = 12

431.         **elif** card2\[:1\] == 'K': \_\_c2 = 13

432.         **elif** card2\[:1\] == 'A': \_\_c2 = 14

433.         **else**: \_\_c2 = int(card2\[:1\])

434.         **if** card1\[-1:\]==card2\[-1:\]: \_\_s = 1

435.         **else**: \_\_s = 0

436.         \_\_c1 = float(\_\_c1)/14

437.         \_\_c2 = float(\_\_c2)/14

438.         **return** \[\_\_c1,\_\_c2,\_\_s\]

439.  

440. **class** Compare:

441.     \_\_allHcards = \[\]

442.     \_\_allAcards = \[\]

443.     **def** cardCompare(self,hc,ac,tblc):

444.      
      self.\_\_allHcards = \[hc\[0\], hc\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

445.      
      self.\_\_allAcards = \[ac\[0\], ac\[1\], tblc\[0\], tblc\[1\], tblc\[2\], tblc\[3\], tblc\[4\]\]

446.      
      **if** self.evaluateCard(self.\_\_allHcards) &gt; self.evaluateCard(self.\_\_allAcards): **return** 'Human'

447.      
      **elif** self.evaluateCard(self.\_\_allAcards) &gt; self.evaluateCard(self.\_\_allHcards): **return** 'AI'

448.         **else**: **return** "no-one"

449.  

450.     **def** evaluateCard(self,hand):

451.        
    \_\_groups = self.group(\['--23456789TJQKA'.index(r) **for** r, s **in** hand\])

452.         \_\_counts, \_\_ranks = zip(\*\_\_groups)

453.         **if** \_\_ranks == (14, 5, 4, 3, 2):

454.             \_\_ranks = (5, 4, 3, 2, 1)

455.        
    \_\_straight = len(\_\_ranks) == 5 **and** max(\_\_ranks)-min(\_\_ranks) == 4

456.         \_\_flush = len(set(\[s **for** r, s **in** hand\])) == 1

457.         **return** (

458.             9 **if** (5, ) == \_\_counts **else**

459.             8 **if** \_\_straight **and** \_\_flush **else**

460.             7 **if** (4, 1) == \_\_counts **else**

461.             6 **if** (3, 2) == \_\_counts **else**

462.             5 **if** \_\_flush **else**

463.             4 **if** \_\_straight **else**

464.             3 **if** (3, 1, 1) == \_\_counts **else**

465.             2 **if** (2, 2, 1) == \_\_counts **else**

466.             1 **if** (2, 1, 1, 1) == \_\_counts **else**

467.             0), \_\_ranks

468.  

469.     **def** group(self,items):

470.        
    \_\_groups = \[(items.count(x), x) **for** x **in** set(items)\]

471.         **return** sorted(\_\_groups, reverse = True)

472.  

473. **class** CardPile:

474.    
    \_\_deck = \[r+s **for** r **in** '23456789TJQKA' **for** s **in** 'SHDC'\]

475.     \_\_usedCards  = \[\]

476.     **def** getCard(self):

477.         **while** True:

478.             \_\_randCard = self.\_\_deck\[randint(0,51)\]

479.             **if** \_\_randCard **not** **in** self.\_\_usedCards:

480.                 self.\_\_usedCards.append(\_\_randCard)

481.                 **return** \_\_randCard

482.                 **break**

483.     **def** reset(self):

484.         self.\_\_usedCards = \[\]

485.  

486. game = Game('One')

487. game.menu()

### \
F: Testing evidence.

  ------ ------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  N^o^   Purpose                                                                   Screenshot
  1.1    The game launches without errors.                                         ![](media/image5.png){width="5.469444444444444in" height="0.6083202099737532in"}
  1.2    The game successfully creates a new player object.                        ![](media/image6.png){width="5.467318460192476in" height="1.3476148293963255in"}
  1.3a   The game is able to interpret a player’s move.                            ![](media/image7.png){width="5.466666666666667in" height="2.209928915135608in"}
  1.3b   The game is able to interpret a player’s move.                            ![](media/image8.png){width="5.381758530183727in" height="1.3923611111111112in"}
  1.3c   The game is able to interpret a player’s move.                            ![](media/image9.png){width="5.38125in" height="2.1433803587051616in"}
  1.4    To see if the game correctly handles money.                               ![](media/image10.png){width="5.417391732283464in" height="2.4438637357830273in"}
  1.5    To see if the card comparison algorithm works correctly.                  ![](media/image11.png){width="5.391304680664917in" height="3.1350568678915134in"}
  1.6    To see if the game is able to reset itself.                               ![](media/image12.png){width="5.382609361329834in" height="1.6491382327209099in"}
  1.7    To see if the game quits successfully.                                    ![](media/image13.png){width="5.399849081364829in" height="0.6173917322834646in"}
  1.8a   To see if the game displays relevant information about the game.          ![](media/image14.png){width="5.460869422572179in" height="0.933480971128609in"}
  1.8b   To see if the game displays relevant information about the game.          ![](media/image15.png){width="5.433578302712161in" height="0.5130435258092738in"}
  1.8c   To see if the game displays relevant information about the game.          ![](media/image16.png){width="5.404856736657917in" height="0.8086953193350831in"}
  1.8d   To see if the game displays relevant information about the game.          ![](media/image17.png){width="5.503288495188102in" height="0.6695658355205599in"}
  1.9    The game is able to correctly carry out an entire betting round           ![](media/image18.png){width="5.440451662292213in" height="8.069564741907262in"}
  2.1    To see if the AI can make a move within the game.                         ![](media/image19.png){width="5.417391732283464in" height="1.0215660542432197in"}
  2.2    To see if the AI can handle the human player folding.                     ![](media/image20.png){width="5.347825896762904in" height="7.088241469816273in"}
  2.3    To see if the AI is able to play after multiple resets.                   ![](media/image21.png){width="3.2608694225721786in" height="7.120673665791776in"}
  3.1a   To see if the AI makes the correct move according to the dataset given.   ![](media/image22.png){width="5.389418197725284in" height="2.3043482064741907in"}
  3.1b   To see if the AI makes the correct move according to the dataset given.   ![](media/image23.png){width="5.4086953193350835in" height="0.9684722222222222in"}
  4.1    Game v AI                                                                 ![](media/image24.png){width="5.417391732283464in" height="2.544534120734908in"}
  4.2    Game v AI                                                                 ![](media/image25.png){width="5.313043525809274in" height="2.4815430883639547in"}
  4.3    Game v AI                                                                 ![](media/image26.png){width="5.347825896762904in" height="1.8289096675415573in"}
  4.4    Game v AI                                                                 ![](media/image27.png){width="5.304348206474191in" height="2.138396762904637in"}
  4.5    Game v AI                                                                 ![](media/image28.png){width="5.26956583552056in" height="1.8584623797025372in"}
  4.6    Game v AI                                                                 ![](media/image29.png){width="5.321738845144357in" height="2.005680227471566in"}
  4.7    Game v AI                                                                 ![](media/image30.png){width="5.42037510936133in" height="2.0608694225721784in"}
  4.8    Game v AI                                                                 ![](media/image31.png){width="5.434782370953631in" height="1.5527963692038496in"}
  4.9    Game v AI                                                                 ![](media/image32.png){width="5.3909722222222225in" height="2.5066305774278215in"}
  4.10   Game v AI                                                                 ![](media/image33.png){width="5.391304680664917in" height="1.8390890201224848in"}
  ------ ------------------------------------------------------------------------- ------------------------------------------------------------------------------------


