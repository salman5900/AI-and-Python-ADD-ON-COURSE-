import wikipedia
import webbrowser

print("=======================================")
print("=== 🤖 SMART DOUBT-SOLVING WIKI CHATBOT ===")
print("Type 'bye' anytime to exit the chat.")
print("=======================================")

# knowedge base
knowledge = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its readability and versatility.",
    "what is ai?": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
}

while True:
    question = input("Student: ").lower().strip()
    # Exit Condition
    if question == "bye":
        print("\n Bot: Goodbye: keep leaingning! 👋")
        break
    # if bot already knows the answer
    if question in knowledge:
        print(f"\n Bot: {knowledge[question]}\n")
        continue
    # try getting answer from wikipedia:
    try:
        print("Bot: Searching Wikipedia for an answer...")
        result = wikipedia.summary(question, sentences=2)
        print(f"\n Bot: According to Wikipedia: {result}\n")
        knowledge[question] = result  # learn the new info
        continue
    except Exception:
        print("Bot: I couldn't find an answer on Automatically.")
    # Ask Teacher of Google should ne used
    choice = input("Bot: should i search on Google? (yes/No): ")
    if choice == 'yes':
        print("Bot: Opening Google...")
        url = f"https://www.google.com/search?q={question.replace('','+')}"
        webbrowser.open(url)
        continue
    # Teacher provides correct answer manually
    answer = input("Bot: Please provide the correct answer: ")
    knowledge[question] = answer
    print("Bot: Answer saved! i will remember this next time:\n")
     
