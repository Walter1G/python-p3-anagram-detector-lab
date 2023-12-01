# your code goes here!
class Anagram:

  def __init__(self, word):
    self.word = word

  def match(self, list_of_words):
    anagram = []
    for listword in list_of_words:
      if (sorted(self.word) == sorted(listword)):
        anagram.append(listword)
      else:
          pass

    return anagram