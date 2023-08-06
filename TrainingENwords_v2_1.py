import pathlib
import random


# przechowuje wyraz EN - PL
class WordENPL:
    def __init__(self, word_en, word_pl):
        self.wordEN = word_en
        self.wordPL = word_pl

    # wyświetlanie słówka
    def print_word_en_pl(self):
        print(self.wordEN + " - " + self.wordPL)


# przechowuje w postaci listy obiekty. W tym wypadku wyrazy EN - PL
class ListObjectWordENPL:
    def __init__(self):
        self.list_objects_WordEN_PL = []

    # dodawanie obiektu do listy
    def add_object_to_list_word_en_pl(self, obj):
        self.list_objects_WordEN_PL.append(obj)

    # wyświetlanie całej listy słówek
    def print_object_list_word_en_pl(self):
        for objx in self.list_objects_WordEN_PL:
            print(f"EN: {objx.wordEN} | PL: {objx.wordPL}")

    # wyświetlanie losowego słówka EN - PL
    def print_draw_word_en_pl(self):
        draw_result = random.choice(self.list_objects_WordEN_PL)
        print(draw_result.wordEN, draw_result.wordPL)

    # losowanie EN - PL
    def learn_draw_word_en_pl(self):
        draw_result = random.choice(self.list_objects_WordEN_PL)
        print("ENG:", draw_result.wordEN, "\n")
        input("Press ENTER to show meaning in PL...")
        print("PL:", draw_result.wordPL, "\n\n------------------------")
        input("Press ENTER for next word in ENG...")


# dodanie słówek do listy, w postaci obiektów
def load_words_from_file(list_):
    with open(pathToFile, mode="r", encoding="utf-8") as file:
        for line in file:
            # rozdzielanie string EN - PL
            temp_line = line.strip().split(" - ")
            # próba stworzenia obiektu z polami string i dodania do listy
            try:
                list_.add_object_to_list_word_en_pl(WordENPL(temp_line[0], temp_line[1]))
            except IndexError:
                print("Check the file. Is it compatible with the scheme: EN - PL")
                exit()


# ------------------------------------------------------------
# ścieżka do pliku
pathToFile = "slowka.txt"

# utworzenie instancji listy pod obiekty
list_of_objects = ListObjectWordENPL()

# dodanie danych do listy
load_words_from_file(list_of_objects)

# wypisanie obiektów z listy
# list_of_objects.print_object_list_word_en_pl()

# wypisanie słówka metodą z klasy WordENPL
# list_of_objects.list_objects_WordEN_PL[1].print_word_en_pl()

# wypisanie losowego obiektu z listy
# list_of_objects.print_draw_word_en_pl()

# losowanie słówek w pętli
while True:
    list_of_objects.learn_draw_word_en_pl()

