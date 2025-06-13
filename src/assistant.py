from intent_classifier import IntentClassifier
import commands.check_time as check_time
import commands.greeting as greeting
import commands.joke as tell_joke
import commands.wiki_search as wiki_search

COMMANDS: dict = {
    "greeting": lambda query: greeting.invoke(query),
    "check_time": lambda query: check_time.invoke(query),
    "joke": lambda query: tell_joke.invoke(query),
    "wiki_search": lambda query: wiki_search.invoke(query),
}


class Assistant():
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.is_on = True  # Responsible for keeping the main loop running; if False, assistant terminates gracefully
        self.debug_mode = False

    def run(self):
        """The main loop of the assistant program"""
        while self.is_on:
            query = str(input("Ask:\t"))
            self.ask(query)

    def ask(self, query: str):
        intent = self.intent_classifier.predict(query)
        
        # Process the intent of the user's query
        if intent == "exit":
            print("Goodbye!")
            self.is_on = False
        elif intent in COMMANDS:
            COMMANDS[intent](query)
        else:
            print(f"I'm sorry, I don't understand how to process commands for '{intent}' yet.")


if __name__ == '__main__':
    assistant = Assistant()
    assistant.run()