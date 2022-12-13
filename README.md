# 64120-final-project

In their paper, Tenenbaum and Griffiths describe how errors in probabilistic reasoning and other inference phenomena can be attributed to representativeness. Representativeness refers to how "good" an example of something is, i.e., how good of a representative it is of a particular category or process. Tenenbaum and Griffiths argue that representativeness strongly influences human reasoning. They outline how past approaches have attempted to quantify representativeness through models like the likelihood or similarity models. However, they describe how these models are not good at capturing representativeness. Using coin flip and animal categorization experiments, they demonstrate that the Bayesian inference model more closely approximates human ideas of representativeness. 

In this project, we will extend the analysis done by Tenenbaum and Griffiths to analyze different models of representativeness in the context of a card-shuffling paradigm. A deck of playing cards has added complexities, like memory (i.e., the same card cannot appear twice) and greater card variability (with four possible suits and thirteen possible values). Through this project, we explore how these added complexities affect human judgments of shuffled-ness. By comparing the Bayesian model, likelihood model, and similarity model, we aim to answer the question: How do various models of representativeness compare at predicting human judgments of card deck shuffled-ness?

We compared the results of a Bayesian Inference model to the human data results. Furthermore, we used the human data to fine-tune the priors to see how closely we can approximate the human results with Bayesian Inference.

We also use a Likelihood model and Similarity model to show how the Bayesian Analysis provides a more robust understanding of human prediction of shuffled-ness.

We first needed to collect data about human judgments of the shuffled-ness of a deck of cards. To do this, we developed the following three different methods of shuffling, which we assumed, for this experiment, made up the set of possible shuffle hypotheses. Our hypothesis are as follow:

- The deck is fully shuffled.
- The deck is shuffled by number.
- The deck is shuffled by suit.


-*Fully Shuffled:* This is a deck that is completely shuffled as normal.

-*Shuffled by suit:* The cards in the deck are separated by suit, each suit group is shuffled, and then the suits are all put back together to form the complete deck. Note that the suits are not in a particular order, but all the card of the suit are grouped together in the deck. NOTE: All suits are present in the deck after shuffling.}
   - Example: All Clubs, All Diamond cards, All Spades cards, All Heart cards.
  
-*Shuffled by number:* The cards in the deck are separated by number (e.g. 2, 7, King), then each number group is shuffled. To put all the cards back together, your friend takes one card at a time from each number group and forms groups of 4 ascending sequences of numbers or 4 descending sequences of 
        -For instance, if your friend chose to shuffle by number in ascending order, the deck would look like Ace, 2, 3, 4, . . . , King , Ace, 2, 3, 4, . . . , King, Ace, 2, 3, 4, . . . , King, Ace, 2, 3, 4, . . .
        
 **Keywords:** Bayesian Inference Model; Likelihood Model; Similarity Model; Shuffled-ness
