"""
This is a simple application for sentence embeddings: semantic search

We have a corpus with various sentences. Then, for a given query sentence,
we want to find the most similar sentence in this corpus.

This script outputs for various queries the top 5 most similar sentences in the corpus.
"""
from sentence_transformers import SentenceTransformer, util
import torch
import redis


embedder = SentenceTransformer('all-MiniLM-L6-v2')
fp = open("data/ml-terms.txt")
corpus =  fp.read().splitlines()
corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

red5 = redis.Redis(host='localhost', port=6379, db=5,encoding='utf-8',decode_responses=True)
red6 = redis.Redis(host='localhost', port=6379, db=6,encoding='utf-8',decode_responses=True)


def process(vid):
    
    chapters = red5.get(vid)
    if(chapters is None):
        return
    queries=chapters.splitlines()
    print(queries)
    tags=set()
    for query in queries:
        #print(f"\n{query}")
        query_embedding = embedder.encode(query, convert_to_tensor=True)

        # Alternatively, we can also use util.semantic_search to perform cosine similarty + topk
        hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1)
        hits = hits[0]      #Get the hits for the first query
        for hit in hits:
            if(hit['score']>.6):
                match=corpus[hit['corpus_id']]
                print(match)
                tags.add(match)
                red6.sadd(vid,match)
                print(f"{hit['score']:.2f}")


    #print(tags)
    print("**************")
    print(",".join(list(tags)))
    print("\n")



fp=open("data/vids.txt")
lines = fp.read().splitlines()
for line in lines[:500]:
    vid=line.strip()
    #if(red6.exists(vid)):
    #    continue
    process(vid)