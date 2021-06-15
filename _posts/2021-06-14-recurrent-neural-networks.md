---
layout: post
title: What are Recurrent Neural Networks?
subtitle: Read if you are hearing about RNNs for the first time
---

# What are RNNs?

RNNs stands for Recurrent Neural Networks. 
They use backpropagation through time instead for just forwardpassing through time.
They work expecially well for sequential data processing. 
They are also ideal for cases when input sequences are not of the same size.
Think of RNNs when you have to work with:

1. Variable length input
2. Reference dependencies after an interval
3. Keep track of order of events

# How do RNNs work?

Recurrent neural networks have loops in them that allows for information to persist through time.
This re-occourance of information gets them the name Recurrent as :
Information is passed from one time step to the next within the network.

Let 
x be the input
t be the time step.
y be the output
ht be  update to internal state

Formula for the recurrence relation can be given by

_ht = fw(h(t-1), xt)_
where fw function with respect to weights.

# What is the algorithm for RNNs?

1. Initialize RNN with hidden state, random weights and take input
2. Loop through each word in the sentence
3. At each time step current word and previous state are used as input
4. Prediction is generated for next word in the sequence and use it for updating state
5. After looping and all words have been fed, a new word is output

Formula for updating the sate of the RNN and output:

_ht = tanh(W1*h(t+1) + W2*xt)_

where W1 and W2 are weight matrices each.

Think of RNN as multiple copies of same network where each copy sents a message to next copy based on ht, which is the internal state.
Weight matrix W1 and weight matrix W2 are the same across time steps.
Summation of losses accross time steps is taken gives us the total loss.

# How to implement an RNN?

In TensorFlow we can use the SimpleRNN layer.

1. Update hidden state by ht formula
2. Take previous hidden state and input x and multiply by weight matrices 
4. Take summation
5. Pass through a non-linear function
6. Return current output and updated hidden state at each time step

# How to train an RNN model?



# What are RNNs used for?

1. Detecting the language used in the given text
2. Machine translation
3. Next word prediction
4. Self-driving cars
5. Text and music generation
6. Weather forecasting
7. Time series forcasting
8. Time series data

# What models are better than RNNs in some particular applications?

1. LSTMs: Long Short-Term Memory models
2. Attention-based models

Note: These are my notes based on MIT lectures.
