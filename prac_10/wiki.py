import wikipedia

search_phrase = input("Search Phrase: ")
while search_phrase != "":
    try:
        page_object = wikipedia.page(search_phrase)
        print(f"{page_object.title}\n{page_object.summary}\n{page_object.url}")
    except wikipedia.exceptions.DisambiguationError:
        print("Search Phrase not specific")
    search_phrase = input("Search Phrase: ")
print("Finished")



