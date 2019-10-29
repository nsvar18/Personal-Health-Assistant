import nltk
from sys import argv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import operator
import os

from nltk.stem.lancaster import LancasterStemmer
import nltk

def contains(a, b):
  return len(set(a).intersection(b))

#Word match
def WordMatch(question,stsent):
    Score = 0
    st = LancasterStemmer()
    #Use of pos_tag for questions
    qtag = nltk.pos_tag(question)
    # Use of pos_tag for sentences
    stag = nltk.pos_tag(stsent)
    #print(qtag,stag)

    for i in range(0,len(question)):
        for j in range(0,len(stsent)):
            tmp = []
            #using stemmer and assigning scores based on below criteria
            if('V' in qtag[i][1][0] and 'V' in stag[j][1][0]):
                if(st.stem(question[i]) == st.stem(stsent[j])):
                    Score = Score + 12

            elif('V' in qtag[i][1][0] or 'V' in stag[j][1][0]):
                if(st.stem(question[i]) == st.stem(stsent[j])):
                    Score = Score + 8


            elif ('NNS' in qtag[i] or 'NNS' in stag[j]):
                if(st.stem(question[i]) == st.stem(stsent[j])):
                    Score = Score + 4


           # print(question,stsent)

            elif (question[i].lower() == stsent[j].lower()):
                if stsent[j].lower() not in tmp:
                    Score = Score + 4
                    tmp.append(stsent[j].lower())

    return Score


#filename_story = "/Users/Ruchika/PycharmProjects/NLP_TermProject/Story_Hypertension.txt"
filename_story = "/Users/Ruchika/PycharmProjects/NLP_TermProject/Story_Diabetes.txt"

txt_story = open(filename_story)
data_story = txt_story.read()
st = data_story.split(".")
#print (st[10])
#print path

#filename_question = "/Users/Ruchika/PycharmProjects/NLP_TermProject/Question_Hypertension.txt"
filename_question = "/Users/Ruchika/PycharmProjects/NLP_TermProject/Question_Diabetes.txt"

txt_question = open(filename_question)
data_question = txt_question.read()
qs = data_question.split("?")
#print (qs)
#print (data_question)

#tokenize
sentNoStop = []
sentSplit=[]
#stop = stopwords.words('english')+['high','High','blood','pressure','Blood','Pressure', 'Hypertension', 'hypertension']
stop = stopwords.words('english')+ ['Diabetes', 'diabetes']
punct = list(string.punctuation)
for i in range(len(st)):

    sentSplit_temp = word_tokenize(st[i])
    for j in range(len(sentSplit_temp)):
        if sentSplit_temp[j] not in stop:
            if sentSplit_temp[j] not in punct:
                sentSplit.append(sentSplit_temp[j])
    sentNoStop.append(sentSplit)
    sentSplit=[]
#print (sentNoStop)
    #sentSplit.append(sentSplit_temp)

#stopwords



#print (sentNoStop)

#tokenize
qNoStop = []
qSplit=[]

for i in range(len(qs)-1):
    Score = []
    qSplit_temp = word_tokenize(qs[i])
    for j in range(len(qSplit_temp)):
        if qSplit_temp[j] not in stop:
            if qSplit_temp[j] not in punct:
                qSplit.append(qSplit_temp[j])
    qNoStop.append(qSplit)
    qSplit=[]

    for k in range(len(sentNoStop)):
        #print(sentNoStop[k])
        score = WordMatch(qNoStop[i], sentNoStop[k])
        #print(score)
        Score.append(score)


    m = max(Score)
    best = [i for i, j in enumerate(Score) if j == m]
    #print (best)
    #print (Score)

    sentSplit = st[best[0]]
    print ("\n\nQ"+":"+qs[i].strip("\n") + "?")


    if len(best) > 1:
        sentSplit2 = st[best[1]]
        print("Ans: " + sentSplit.strip("\n") + ". " + sentSplit2.strip("\n"))
    else:
        print("Ans: " + sentSplit.strip("\n"))
