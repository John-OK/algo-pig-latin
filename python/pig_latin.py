# 1. Save variables of string of lowercase alphabet, uppercase alphabet, lower- and upper-case vowels, and empty array to hold new sentence.
# 2. Lowercase string and split into array on spaces to get indiviual words.
# 3. Iterate through words and check if begins with vowel.
# 4. If vowel, add "ay" to end and push to array (checking for punctuation).
# 5. If consonant, remove and add to end with "ay"

lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vowels = "aeiouAEIOU"

def piggify_word(word):

  letters = list(word)
  is_q = False
  front_consonants = []
  is_done_front_consonants = False
  new_word = []

  # Check for punctuation, and remove and preserve in arrays
  has_front_punctuation = word[0].lower() not in lower_alpha
  has_end_punctuation = word[-1].lower() not in lower_alpha
  front_punctuation = []
  end_punctuation = []
  if has_front_punctuation:
    front_punctuation = letters.pop(0)
  if has_end_punctuation:
    end_punctuation = letters.pop(-1)

  # Check for capitalization and beginning vowel
  is_capitalized = letters[0] in upper_alpha
  begins_with_vowel = letters[0] in vowels

  # Build piggified array
  if begins_with_vowel:
    new_word = letters

  else:
    for letter in letters:
      letter = letter.lower()
      if letter == 'q':
        is_q = True
        front_consonants.append(letter)
      elif is_q and letter == 'u':
        front_consonants.append(letter)
        is_q = False
      elif letter not in vowels and is_done_front_consonants == False:
        front_consonants.append(letter)
      else:
        is_done_front_consonants = True
        new_word.append(letter)
    new_word += front_consonants
  new_word += ['a', 'y']

  # Recapitalize words
  if is_capitalized == True:
    new_word[0] = new_word[0].upper()

  # Add punctuation back
  if has_front_punctuation:
    new_word.insert(0, front_punctuation)
  if has_end_punctuation:
    new_word.insert(len(new_word), end_punctuation)

  return "".join(new_word)

def translate(word_or_phrase):
  piggified_words = []
  words = word_or_phrase.split(" ")

  for word in words:
    piggified_words.append(piggify_word(word))

  return " ".join(piggified_words)

# print(translate("!The quick brown fox jumped over Bob!"))
