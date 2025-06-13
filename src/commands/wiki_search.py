import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import re

patterns = [
    r"^(can you tell me|do you know|i want to know|what is|who is|what are|give me|can you define what|can you do a wiki search for|can you tell me what is) ",
    r"( is| are)?( about| regarding)?$",
]


def invoke(query: str):
    if query == "":
        print("Query is empty. Please ask me something to search on the Wikipedia page.")
        return
    
    # TODO: Perform some preprocessing to the query
    # "can you tell me what the game half life is?" --> "the game half life is?"

    cleaned_query = clean_query(query)
    print(f"[DEBUG] Searching for '{cleaned_query}'.")

    try:
        result = wikipedia.summary(query, sentences = 3) 
        print(result)
    except DisambiguationError as e:
        print("That topic is ambiguous. Did you mean one of the following?")
        print(", ".join(e.options[:5]))
    except PageError:
        print(f"No matching page found for the processed query: '{cleaned_query}'.")
    except Exception as e:
        print(f"Unknown exception has occured: {e}.")


def clean_query(query: str) -> str:
    for pattern in patterns:
        query = re.sub(pattern, '', query)

    return query.strip()