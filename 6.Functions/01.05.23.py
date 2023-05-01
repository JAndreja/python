def combine_words(word,**kwords):
    if "prefix" in kwords:
         return f"{kwords['prefix']}{word}"
    elif "suffix" in kwords:
         return f"{word}{kwords['suffix']}"
    else:
         return word
    

print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))