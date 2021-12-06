from VoteChain import VoteChain
import math
from vote import vote
voteChain= VoteChain()
Candidates = ["zyzz" , "rick sanchez" , "giorno giovanna"]

def results():
    res = {}
    for c in Candidates:
        res[c]=0
    vs=voteChain.votes[1:]
    for v in vs:
        for t in v["transaction"]:
            candidate=t["recipient"]
            points=t["amount"]
            res.update({candidate : points + res[candidate]})
    print(res)

while(True):
    print("""
    1) vote
    2) see results
    3) quit
    """)
    try : 
        choice = (int)(input("type the chosen option : "))
    except: 
        print("wrong!!! choose again ... ")
        choice = 4
    if(choice==1):
        vote(voteChain,Candidates)
    else:
        if(choice==2):
            results()
        else:
            if(choice == 3 ):
                break
    