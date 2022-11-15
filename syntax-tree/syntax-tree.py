import stanza

text = 'For the past 400 years, astronomers have sought to observe and interpret the Universe by building more powerful telescopes.'

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')
doc = nlp(text)

for sentence in doc.sentences:
    for word in sentence.words:
        print(f'word: {word.text}\thead: {sentence.words[word.head-1].text if word.head > 0 else "root"}\t')


nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
doc = nlp(text)
for sentence in doc.sentences:
    print(sentence.constituency)
