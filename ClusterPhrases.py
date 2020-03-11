import gensim
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans

segmented_phrases_found_file = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/phrases_segmentation_step.txt", "r")
# 93 phrases found during segmentation step are not present in W2V vocab (some of them seem to be ill-formed)
# updated_segmented_phrases_found_file = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/phrases_segmentation_step.txt", "w")
clustered_words = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/clustered_words.txt", "w")
model = gensim.models.KeyedVectors.load_word2vec_format('W2V_model.bin')

phrases_not_present_in_W2V = []
embedding_array = []
phrase_embedding = []
countNT = 0
count = 0
for line in segmented_phrases_found_file:
    phrase = line.strip('\n')
    # phrase = line.split(maxsplit=1)[1]
    # phrase = phrase.replace(" ", "_")
    # print(phrase)
    count += 1
    if phrase not in model.vocab:
        print("Not There:" + phrase)
        countNT += 1
    else:
        # updated_segmented_phrases_found_file.write(phrase + "\n")
        phrase_embedding.append(phrase)
        embedding_array.append(model[phrase])
    # print(embedding_array)
    # break
print(countNT)
print(count)


phrases_cat_wise = [["", ], ["", ], ["", ], ["", ], ["", ], ["", ]]
kmeans = KMeans(n_clusters=6, random_state=0).fit(embedding_array)
print("completed Kmeans")

for index, labels in enumerate(kmeans.labels_):
    phrases_cat_wise[labels].append(phrase_embedding[index])

print("Added to the list")

for i in range(len(phrases_cat_wise)):
    clustered_words.write("####### Category" + str(i) + " #######" + "\n")
    for j in phrases_cat_wise[i]:
        clustered_words.write(j + "\n")

print("Stored in the file")

