from gensim.models import Word2Vec

pre_proc_file = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/segmentationPP.txt","r")

docs = []

for line in pre_proc_file:
    # print(line)
    docs.append(line.split())

# print(docs)

model = Word2Vec(docs, cbow_mean=0, size=100, window=5, negative=0, hs=1,  sample=1e-3, workers=12, sg=1, min_count=1)
model.wv.save_word2vec_format('W2V_model.txt', binary=0)
model.wv.save_word2vec_format('W2V_model.bin')


# model = Word2Vec.load('model.bin')