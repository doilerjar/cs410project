import metapy

doc = metapy.index.Document()
doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")

tok = metapy.analyzers.ICUTokenizer()
tok.set_content(doc.content())  # this could be any string
[token for token in tok]

tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
tok.set_content(doc.content())
[token for token in tok]

tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
tok.set_content(doc.content())
[token for token in tok]

# lemmatizer
tok = metapy.analyzers.Porter2Filter(tok)
tok.set_content(doc.content())
[token for token in tok]

tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
tok = metapy.analyzers.LowercaseFilter(tok)
tok.set_content(doc.content())
[token for token in tok]

# bag of words or unigram word counts
ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
print(doc.content())
ana.analyze(doc)

# 2-gram or Bigram
ana = metapy.analyzers.NGramWordAnalyzer(2, tok)
ana.analyze(doc)

# n-gram characters
tok = metapy.analyzers.CharacterTokenizer()
ana = metapy.analyzers.NGramWordAnalyzer(4, tok)
ana.analyze(doc)

# Part of speech tagging
seq = metapy.sequence.Sequence()
for word in ["The", "dog", "ran", "across", "the", "park", "."]:
    seq.add_symbol(word)
print(seq)

'''
!wget -nc https://github.com/meta-toolkit/meta/releases/download/v3.0.1/greedy-perceptron-tagger.tar.gz
!tar xvf greedy-perceptron-tagger.tar.gz
'''
#Part of speech tagger
tagger = metapy.sequence.PerceptronTagger("perceptron-tagger/")
tagger.tag(seq)
print(seq)


tok = metapy.analyzers.ICUTokenizer() # keep sentence boundaries!
tok = metapy.analyzers.PennTreebankNormalizer(tok)
tok.set_content(doc.content())
[token for token in tok]

# write me a function that can take a token stream that contains sentence boundary tags and
# returns a list of Sequence objects. Don't include the sentence boundary tags in the actual Sequence objects.
def extract_sequences(tok):
    sequences = []
    for token in tok:
        if token == '<s>':
            sequences.append(metapy.sequence.Sequence())
        elif token != '</s>':
            sequences[-1].add_symbol(token)
    return sequences

tok.set_content(doc.content())
for seq in extract_sequences(tok):
    tagger.tag(seq)
    print(seq)

# Parse these sequences of POS-tagged words to obtain a tree for each sentence
parser = metapy.parser.Parser("parser/")
print(' '.join([obs.symbol for obs in seq]))
print(seq)
tree = parser.parse(seq)
print(tree.pretty_str())
# Parse all sentences in our file
tok.set_content(doc.content())
for seq in extract_sequences(tok):
    tagger.tag(seq)
    print(parser.parse(seq).pretty_str())
'''
!wget -nc https://meta-toolkit.org/data/2017-03-27/headlines.tar.gz # please be nice!
!tar xvf headlines.tar.gz
!echo "" && echo "README:"
!cat headlines/README.md
'''
