import sys

GREETINGS = {
    "english": "Hello",
    "french": "Bonjour",
    "russian": "Привет",
}

def greet(name="World", language="english"):
    language = language.lower()
    greeting = GREETINGS.get(language)
    if greeting is None:
        print(f"Unsupported language: {language}")
        print(f"Supported languages: {', '.join(GREETINGS)}")
        sys.exit(1)
    print(f"{greeting}, {name}!")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    language = sys.argv[2] if len(sys.argv) > 2 else "english"
    greet(name, language)
