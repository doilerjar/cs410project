import metapy
idx = metapy.index.make_inverted_index('config.toml')

print(idx.num_docs())
print(idx.unique_terms())
print(idx.avg_doc_length())
print(idx.total_corpus_terms())
ranker = metapy.index.OkapiBM25()
query = metapy.index.Document()
query.content('mario luigi')
top_docs = ranker.score(idx, query, num_results=5)
print(top_docs)
for num, (d_id, _) in enumerate(top_docs):
    content = idx.metadata(d_id).get('content')
    print("{}. {}...\n".format(num + 1, content))