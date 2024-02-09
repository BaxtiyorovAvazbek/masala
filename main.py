# 1-masala
def func1(stutter):
    for x in stutter:
        st1 = stutter[:-8]
        st2 = stutter2[:-10]
        st3 = stutter3[:-9]
        print(st1,"...", st1,"...", stutter,"?")
        print(st2,"...", st2,"...", stutter2,"?")
        print(st3,"...", st3,"...", stutter3,"?")
        return stutter


stutter = ("incredible")
stutter2 = ("enthusiastic")
stutter3 = ("outstanding")
func1(stutter)

# 2-masala
def func2(person):
    if person == "Darth Vader":
        print("Luke, I am your father.")
    elif person == "Leia":
        print("Luke, I am your sister.")
    elif person == "Han":
        print("Luke, I am your brother in law.")
    else:
        print("Luke, I am your droid.")


person = input("Person: ")
func2(person)
# 3-masala
def func3(mood):
    if mood == "happy":
        print("Today, I am feeling happy")
    elif mood == "sad":
        print("Today, I am feeling sad")
    elif mood == "":
        print("Today, I am feeling neutral")
    else:
        print("?")


mood = input("Mood_Today: ")
func3(mood)
# 4-masala
def func4(count_vowels):
    vowels = 0
    for harf in count_vowels:
        if harf.lower() in "aeiou":
            vowels += 1
    return vowels


count_vowels = "Celebration"
vowels = func4(count_vowels)
print(vowels)
# 5-masala
# 6-masala
# 7-masala
def func7(replace_vowels):
    unli = ("aeiou")
    satr = ""
    for replace in replace_vowels:
        if replace in unli:
            satr += belgi
        else:
            satr += replace
    return satr


replace_vowels = ("the aardvark")
belgi = "#"
satr = func7(replace_vowels)
print(satr)
# 8-masala
def func8(card_hide):
    if len(card_hide)<=4:
        return card_hide
    else:
        part1 = card_hide[:-4]
        part2 = card_hide[-4:]
        natija = len(part1)*"*"
        natija += part2
        print(natija)
        return natija


card_hide = ("1234123456785678")
func8(card_hide)
# 9-masala
def func9(string):
    if string.lower().count("x") == string.count("o"):
        return True
    return False


print(func9('ooxx'))
print(func9("xooxx"))
print(func9("ooxXm"))
print(func9("zpzpzpp"))
print(func9("zzoo"))
# 10-masala
def func10(name_shuffle):
    for shuffle in name_shuffle:
        name, shuffle = name_shuffle.split()
        print(shuffle, name)
        return name_shuffle


name_shuffle = ("Donald Trump")
func10(name_shuffle)