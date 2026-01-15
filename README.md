# SMS-Security-Filter 

A Machine Learning project designed to dectect if an incoming message is malicious

## Overview
This project demonstrates how Natural Language Processing can be used to filter unwanted messages. It uses **Naive Bayes** algorithm, which is a standard method for text classifications.

##Tech Stack
* **Language:** Python 3
* **Libraries:** Pandas and Scikti-Learn
* **Concepts:** Test Vectorization (CountVectorizer), Supervised Learning
  
##How it works
1. **Ingestion:** The system loads a dataset of sms logs
2. **Vectorization:** Raw test is tokenized and then converted to a matrix
3. **Training:** A SUpervised Learning model (MultinomialNB) lears to differentiate between safe messages and spam messages (security threats)
4. **Detection:** The model flags unseen messages in real-time

##Results
* The model successfully identifies common spam keywords like URGENT, Click now etc. while ignoring safe messages

##Future Scope
*Can be improved with larger datasets
*Integration with real-time API streams
