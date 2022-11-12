import requests
import json

base_url="https://api.dictionaryapi.dev/api/v2/entries/en/"
word_to_search=input("Enter the word you want to search:")

raw_data=requests.get(base_url+word_to_search)
data = json.loads(raw_data.text)
print("The word: ",data[0]["word"])
#print(data[0]["meanings"])

#print(json.dumps(data, indent=4))
for item in data[0]["meanings"]:
    print("#"*10)
    print("Part of speech: ",item["partOfSpeech"])
    for definition in item["definitions"]:
        print("Definition: ",definition["definition"])
        print("Synonyms: ",definition["synonyms"])
        print("Antonyms: ",definition["antonyms"])
        print()
    print()
