#! /usr/bin/python3.12

import requests, re, sys, os
from tqdm import tqdm

def clear_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def find_words(re_word: str) -> set[str]:
        
    # url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    url = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(url)
    print(response.status_code)

    word_list: str = response.content.decode()

    return list(set(re.findall(f"{re_word}", word_list, flags=re.IGNORECASE)))


def actual_words(words: list[str]) -> None:
    actual_words = set() 
    progress_bar = tqdm(range(len(words)), position=1, leave=True)
    try:
        for word in words:
            if not word.isalpha():
                continue

            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

            response = requests.get(url)
            
            if response.status_code == 200:
                actual_words.add(word)
                clear_terminal()
                print('\n'.join(actual_words))
            # else:
            #     print(word, "not valid")
            progress_bar.update(1)
    except KeyboardInterrupt:
        clear_terminal() 
        print("\n".join(actual_words))


       
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("syntax:\n\tpython app.py regex_pattern\n")
    else:
        actual_words(find_words(sys.argv[1].replace("_", ".")))
