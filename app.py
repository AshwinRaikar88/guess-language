import guess_language


chi_text = '這是一個非常美麗的地方' # This is a very beautiful place
hin_text = "मेरा नाम अनमोल है और मैं स्कूल जाता हूँ" # My name  is Anmol and I go to school
kan_text = 'ನನ್ನ ಹೆಸರು ಅನ್ಮೋಲ್ ಮತ್ತು ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ' # My name  is Anmol and I go to school
tel_text = "నా పేరు అన్మోల్ మరియు నేను పాఠశాలకు వెళ్తాను" # My name  is Anmol and I go to school

text = tel_text


print(guess_language.guessLanguage(text.encode('utf-8')))
print(guess_language.guessLanguageInfo(text.encode('utf-8')))
