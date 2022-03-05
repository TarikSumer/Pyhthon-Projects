import sys
import time
if len(sys.argv) != 3:
    print("You must write two arguments for this program")
    exit()
sys.argv[1]= open("correct_words.txt", "r", encoding="utf-8")
kelime_listeleri = []
for line in sys.argv[1].readlines():
    kelime_listeleri.append(line.strip("\n\ufeff"))
kelime_sözlüğü = {}
for i in kelime_listeleri:                                 # karışık harfler ve karşılıkları sözlüğü   KELİME LİSTELERİ
    j = i.split(":")
    kelime_sözlüğü[j[0]] = j[1]
sys.argv[1].close()
sys.argv[2] = open("letter_values.txt", "r", encoding="utf-8")
values = {}
for line in sys.argv[2]:
    line = line.strip("\n\ufeff")
    key,value = line.split(":")
    values[key] = value
sys.argv[2].close()
harf_degerleri = {}                               #dictionary for values of letters
for harf, value in values.items():
    if harf == "I":
        harf = harf.replace("I", "ı")
        harf_degerleri[harf] = value
    elif harf == "İ":
        harf = harf.replace("İ", "i")
        harf_degerleri[harf] = value
    else:
        harf = harf.lower()
        harf_degerleri[harf] = value
lower_kelime_sozlugu = {}
for kelime,dogrular in kelime_sözlüğü.items():
    if  "I" in kelime:
        kelime = kelime.replace("I", "ı")
        kelime = kelime.lower()
        lower_kelime_sozlugu[kelime] = dogrular
    elif "İ" in kelime:
        kelime = kelime.replace("İ","i")
        kelime = kelime.lower()
        lower_kelime_sozlugu[kelime] = dogrular
    else:
        kelime = kelime.lower()
        lower_kelime_sozlugu[kelime] = dogrular

for key in lower_kelime_sozlugu.keys():
    lower_kelime_sozlugu[key] = lower_kelime_sozlugu[key].split(",")
    for i in range(len(lower_kelime_sozlugu[key])):                   # tüm anlamlı kelimelere lowercase fonksiyonu uyguladım
        if "I" in lower_kelime_sozlugu[key][i]:
            lower_kelime_sozlugu[key][i] = lower_kelime_sozlugu[key][i].replace("I", "ı")
            lower_kelime_sozlugu[key][i] = lower_kelime_sozlugu[key][i].lower()
        elif "İ" in lower_kelime_sozlugu[key][i]:
            lower_kelime_sozlugu[key][i] = lower_kelime_sozlugu[key][i].replace("İ", "i")
            lower_kelime_sozlugu[key][i] = lower_kelime_sozlugu[key][i].lower()
        else:
            lower_kelime_sozlugu[key][i] = lower_kelime_sozlugu[key][i].lower()

for shuffled_letters in lower_kelime_sozlugu.keys():
    print("Shuffled letters are: ", shuffled_letters, "Please guess words for these letters with minimum three letters")
    start_time = time.time()
    point = 0
    known_words = []


    while 30 - (time.time() - start_time) > 0 and (start_time - time.time() <= 0):

        guessed_word = input("Guessed word: ")
        if 30 - (time.time()-start_time) < 0:
            print("your guessed word is not a valid word")
            print("you have 0 time")
        elif guessed_word in lower_kelime_sozlugu[shuffled_letters]:
            if guessed_word in known_words:
                print("This word is guessed before")
                print("you have {} time".format(int(30 - (time.time() - start_time))))
            else:
                known_words.append(guessed_word)
                print("you have {} time".format(int(30 - (time.time() - start_time))))
                for letter in guessed_word:

                    point += len(guessed_word) * int(harf_degerleri[letter])
        else:
            print("your guessed word is not a valid word")
            print("you have {} time".format(int(30 - (time.time() - start_time) +1)))
        if 30 - (time.time() - start_time) <= 0:
            if len(known_words) > 0:
                print("Score for {} is {} and guessed words are: ".format(shuffled_letters, point), end="")
                print((*known_words), sep="-")
                break
            else:
                print("Score for {} is {}".format(shuffled_letters,point))






