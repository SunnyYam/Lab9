def sort_sentence(sentence):
    confirmed_sentence = sentence.split(" ")
    confirmed_sentence = sorted(confirmed_sentence, key=len)
    confirmed_sentence = " ".join(confirmed_sentence)
    return (confirmed_sentence.capitalize())
