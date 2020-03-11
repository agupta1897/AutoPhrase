import re

segmented_file = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/segmentation.txt", "r")
post_tag_removal_file = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/segmentationPP.txt","w")
segmented_phrases_found = open(r"C:/Edata/UIUC_Academics/Spring2020/CS512/Assignment-1/AutoPhrase/models/cate/phrases_segmentation_step.txt", "w")

phrase_list = []

def remove_tags_join_to_word_func(matchObject):
    string = matchObject.group(0)
    # print(string)
    string = matchObject.group(0).replace(" ", "_")[8:-9]
    # print(string)
    if string not in phrase_list:
        phrase_list.append(string)
    return string


# counter = 0
for line in segmented_file:

    # print(line)
    proc_line = re.sub(r"<phrase>.*?</phrase>", remove_tags_join_to_word_func, line)
    post_tag_removal_file.write(proc_line)
    # print(proc_line)
    # counter += 1
    # if counter%2 == 0: break

for phrase in phrase_list:
    segmented_phrases_found.write(phrase + "\n")



