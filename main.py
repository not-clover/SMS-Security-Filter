import pandas as pd           #For the Data Frame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

data = {
    'sms' : [
        "URGENT : Suspicious activity on your account",
        "URGENT : Verify this 500kr charge",
        "Security Alert : We detected a large purchase on your account. Call this number",
        "We have an easy task job for you, earn 500kr per hour, Apply now",
        "Your account is suspended. Verify details here, CLICK NOW",
        "Act Now or your account will be closed!!",
        "FREE 500kr giftcard, all you need to do is fill this survey, CLICK NOW",
        "Hej! When will we be meeting up?",
        "Hey Ish, Your order has been recieved by us",
        "Your verification code for xyz is ABCD",
        "Hey Ish, we want to remind you about your booking tonight at 22:00",
        "Account 1234 has been verified now",
        "Hello how are you doing",
        "Long time no see, would love to hang soon",
        "I cant wait to meet you at the party"
    ], 
    'label' : [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]    #1 FOR Spam and 0 for normal messages
}

df = pd.DataFrame(data)    #Load into a table

print("---- Data Loaded ----")
print(df.head())    #First few rows
print("\n")

'''Process of Vectorization : Converting the sms messages into numbers so that the AI model can read them'''
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['sms'])
y=df['label']

''' Splitting the Data : Splits into Training Data and Test Data (with ratio 80/20)'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

'''Training the model : Using Naive Bayes (works well for small datasets)'''
model = MultinomialNB()
model.fit(X_train, y_train)
print("---- Model Trained Successfully ----")

'''Evaluation'''
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy : {accuracy * 100}%\n")

'''Finally testing'''
print("\n" + "="*50)
print("SMS SECURITY FILTER SYSTEM IS READY")
print("Type a message to test (type in q to quit)")
print("="*50 + "\n")

while True:
    user_input = input("Enter SMS : ")
    
    if user_input == 'q':
        print("\n"+"="*50)
        print("Exiting Security Filter......")
        print("="*50)
        break

    print("Predicting incoming SMS....")
    input_vectorized = vectorizer.transform([user_input])
    prediction = model.predict(input_vectorized)

    if prediction[0] == 1:
        print("Oh no! SPAM detected")
    else:
        print("Safe sms")


