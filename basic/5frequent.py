# find 5 most frequent words in a txt file

with open('re.txt') as f:
    txt=f.read()
    word_dict={}
    for word in txt.split(' '):
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

# res=sorted(word_dict.items())
tmp=list()
for k,v in word_dict.items():
    tmp.append((v,k))

tmp=sorted(tmp,reverse=True)
print(tmp[:10])