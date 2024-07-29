#! /usr/bin/python3

import requests, re, sys, os

def clear_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def find_words(re_word: str) -> list[str]:
        
    # url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    url = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(url)
    print(response.status_code)

    word_list: str = response.content.decode()

    return re.findall(f"{re_word}", word_list, flags=re.IGNORECASE)


def actual_words(words: list[str]) -> None:
    actual_words = set() 
    try:
        for word in  words:
            if not word.isalpha():
                continue

            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

            response = requests.get(url)
            
            if response.status_code == 200:
                actual_words.add(word)
                print(word, "valid")
            else:
                print(word, "not valid")
    except KeyboardInterrupt:
        clear_terminal() 
        print("\n".join(actual_words))

    clear_terminal()
    print("\n".join(actual_words))

       
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("syntax:\n\tpython app.py regex_pattern\n")
    else:
        actual_words(find_words(sys.argv[1].replace("_", ".")))
