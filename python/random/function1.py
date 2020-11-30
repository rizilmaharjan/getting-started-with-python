def language(lang):
    if lang == "en":
        return "english"
    elif lang == "nep":
        return "Nepali"
    if lang == "br":
        return "british"
lang=  input("select language: ")
print("your preffered language is",language(lang)) 