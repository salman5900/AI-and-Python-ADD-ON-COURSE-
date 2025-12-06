from textblob import TextBlob

def analyze_sentiment(text):
    polarity = TextBlob(text).polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    print("=== Simple Sentiment Analyser ===")
    while True:
        user_input = input("Enter text (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Sentiment Analyser.")
            print("Goodbye!")
            break
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}\n")
