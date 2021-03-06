# Attempts to determine the natural language of a selection of "Unicode (utf-8) text". 

This is a python3 port of Guess Language

Based on guesslanguage.cpp
http://websvn.kde.org/branches/work/sonnet-refactoring/common/nlp/guesslanguage.cpp?view=markup
by Jacob R Rideout for KDE which itself is based on
Language::Guess http://languid.cantbedone.org/ by Maciej Ceglowski.

Detects over 60 languages - all languages listed in the trigrams
http://code.google.com/p/guess-language/source/browse/trunk/guess_language/trigrams/
directory plus Japanese, Chinese, Korean and Greek.

guess_language uses heuristics based on the character set and trigrams in a sample text 
to detect the language. It works better with longer samples and will be confused if 
the sample text includes markup such as HTML tags.

### Requirements

numpy


### Installation

Clone the repository

Run app.py


### Usage

The main entry points all take a single string as input and return a language identifier. 
The string must be Unicode or UTF-8 text. The language identifer can be the language name
in English, the two- or three-letter IANA language code, a language ID or a tuple containing
all three codes.


```python
import guess_language


chi_text = '這是一個非常美麗的地方' # This is a very beautiful place
hin_text = "मेरा नाम अनमोल है और मैं स्कूल जाता हूँ" # My name  is Anmol and I go to school
kan_text = 'ನನ್ನ ಹೆಸರು ಅನ್ಮೋಲ್ ಮತ್ತು ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ' # My name  is Anmol and I go to school
tel_text = "నా పేరు అన్మోల్ మరియు నేను పాఠశాలకు వెళ్తాను" # My name  is Anmol and I go to school

text = tel_text # Choose your text here

print(guess_language.guessLanguage(text.encode('utf-8')))
print(guess_language.guessLanguageInfo(text.encode('utf-8')))
```

#### Issues 

If there are any issues while using the app let me know 

Note: This is a python 3 port of guess language originally derived from https://github.com/kent37/guess-language
guess_language has also been ported to
JavaScript (https://github.com/wooorm/franc)
R (https://github.com/MangoTheCat/franc)
