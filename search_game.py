'''
CS410 Project
search_game.py uses metapy to generate an inverted index of games.dat file then uses bm25 to
search and return top five matching document id's based on their ranks
'''
import sys
import metapy

try:
    query_string = str(sys.argv[1])
except:
    print("Please enter a search term in double or single quotes")
    exit(1)
else:
    idx = metapy.index.make_inverted_index('config.toml')

    print("total number of documents: ", idx.num_docs())
    print("total number of unique terms: ", idx.unique_terms())
    print("average document length: ", idx.avg_doc_length())
    print("total corpus terms: ", idx.total_corpus_terms())
    print()
    ranker = metapy.index.OkapiBM25()
    query = metapy.index.Document()
    query.content(query_string)
    top_docs = ranker.score(idx, query, num_results=5)
    print("Top five document id's matching the query, best matches first")
    print("-------------------------------------------------------------")
    for num, (doc_id, _) in enumerate(top_docs):
        content = idx.metadata(doc_id).get('content')
        # print("{}. {}...\n".format(num + 1, content)) doesn't work!
        print("{}. {}\n".format(num + 1, doc_id))