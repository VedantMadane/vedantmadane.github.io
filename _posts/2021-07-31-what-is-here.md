---
title: What Exists Here May Be Found Elsewhere
subtitle:  What is not here can scarcely be found
#cover-img: https://user-images.githubusercontent.com/6527493/127737983-83b6619f-1811-4165-9872-0ae8a8762238.png
thumbnail-img: https://jovian.ml/api/user/vedant-madane/avatar/d38cb98c1c1240769984fde7615eba01
tags:[project]
---
Vaiśampāyana told Janamejaya,\
`What exists here may be found elsewhere, `\
`What is not here can scarcely be found. `

## यत् इह अस्ति तत् अन्यत्र 
## यत् न इह अस्ति न तत् क्वचित् ॥ १.६२.५३

Although India's IT industry has been reporting record breaking profits year on year, the benefits of this superficial digital transformation rarely trickles down beyond tier-2 cities. A testament to this fact is that most Indian languages are considered low-resource despite having centuries of written literature. A language is generally considered low-resource when there are less than ten thousand annotated sentences for a given language pair. This becomes a problem for carrying out natural language processing tasks without machine learning.

Natural language processing is a broad term encompassing everything from chatbots to speech recognition. We have to work with unstructured data for the majority of NLP tasks. Unstructured data means the information is not neatly organized in tables in a database. Written text, voice commands, sensor input are all examples of unstructured data which form a large portion of the data in the public domain. The easy way out would be to simply run a pre-trained language model on your corpus and get state-of-the-art results. However, SOTA models have the drawback of giving jaw-dropping but unreproducible results, unless you have the means to afford the compute resources.

[![](https://user-images.githubusercontent.com/6527493/127737983-83b6619f-1811-4165-9872-0ae8a8762238.png)](https://vedantmadane.github.io/maha/poster)

In order to work with text, it's often important that you encode it in numeric form. Mining Data from text includes building feature vector representations of text, which involves representing text in numeric form. Now let's say you have a host of labeled text data and you want to train a classification model, and you want this classification model to perform sentiment analysis. Once you have a fully trained classifier, you want to feed in input in the form of sentences, that is, text, and you want to get an output that tells you whether the text is positive or negative. In order to work with text, it's often important that you encode it in numeric form. Mining Data from text includes building feature vector representations of text, which involves representing text in numeric form. Now let's say you have a host of labeled text data and you want to train a classification model, and you want this classification model to perform sentiment analysis. Once you have a fully trained classifier, you want to feed in input in the form of sentences, that is, text, and you want to get an output that tells you whether the text is positive or negative.
[![image](https://user-images.githubusercontent.com/6527493/127738035-6b75e64f-2c3d-4651-89dd-c5143296b3fe.png)](https://vedantmadane.github.io/maha/poster)

There are multiple ways of transforming unstructured data into something a computer can understand. For our project we used the bag-of-words approach. In BoW, we disregard the order in which the words occur in the text, giving them weights instead in accordance with the frequency with which they occur in the text.
post.png
Another approach is n-grams. Imagine a window sliding over your text, where n is the number of words that can be fitted in each window. You iterate over your text capturing the relation and relative position of words by adding the next word after your current n-gram and removing the first word of it, to form a new n-gram. This approach can pick up phrases and the relation between two words as long as they are not separated by a distance greater than n. Even Google with its massive resources does not store more than 7-grams for its search.
One-hot encoding is another approach for vectorizing text. Vectorizing means imposing a structure to our data. In 1-hot encoding, we put 1 if a word present in our dictionary occurs in a sentence.

In this way, we build features from our text data using the bag-of-words, as well as the bag-of-n-grams representation. This allowed us to gain insights from the Mahābhārata, summarize any given page of the text, classify any page into a category of topics- main war narrative, philosophy and side-quests. Then we plotted the change of sentiment from page-to-page by having the progress from 0% to 100% on the X-axis and the sentiment score from -1 (negative sentiment) to +1 (positive sentiment) on the Y-axis. We also plotted word clouds to garner information of the relative importance of the people mentioned in the Mahabhārata, and how their position changes with changing circumstances from Parva to Parva.

Click below to access the interactive project page:
[![Click here to go to the project page](https://user-images.githubusercontent.com/6527493/127737965-60049c6c-6ae7-4467-b36b-675b9777bb35.png)](https://vedantmadane.github.io/maha/poster)
