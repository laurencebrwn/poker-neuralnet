BASIC POKER NEURAL NETWORK
==========================

Brief introduction:
-------------------

The aim of this project is to see if it possible to make an AI that will
play Texas Hold ‘em and beat a player. The AI uses a stochastic gradient 
descent neural network to predict the best move based on a dataset of the 
possibilty of winning with the AI's hand cards. This project was created 
for the Non-Examined Assement section of my Computer Science A-Level. More 
details and the write up for this project can be found in the [NEA document](https://github.com/snowsnooks/poker-neuralnet/blob/master/Report.pdf).
  

Instructions:
-----------------

This project consists of 6 files:
1. poker.py

   This python file contains the game itself as well as the Texas Hold'em 
   Neural Network. Run this file to play poker against the AI.

2. datatrain.py

   This python file is used to generate the dataset the neural network uses
   to predict what move to make. It creates the dataset by running through
   all the possible moves for each possible hand and using the outcome of
   playing with those cards to determine the likelihood of winning.

3. correctpredtrained.csv
   
   This the training dataset for the AI.

4. handstrained.csv
   
   This dataset contains a list of all possible starting card combinations 
   and the likelyhood if it will win with the cards or not.

5. correctpredtrainedfloat.csv & correctpredtrainedUN.csv
   
   These are temporary files created when generating the datasets.