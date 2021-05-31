import wikipedia

def get_wiki():
    name = input("Enter Search: ")
    while name:
        try:
            get_page = wikipedia.page(name, auto_suggest=False)
            print(get_page.title)
            print(get_page.summary)
            print(get_page.url)
            name = input("Enter Search: ")

        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)


get_wiki()