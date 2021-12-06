Voters = ["alex" , "mike" , "peter" , "alfredo" , "chad"]



def vote(voteChain,Candidates):
    nC =len(Candidates)
    name = input("identify yourself : ")
    if name.lower() in Voters:
        print("our candidates are : " )
        for i in range(0,nC) : 
            print(i,'- ',Candidates[i])
        print("""please right your answer as a string of numbers ranking the candidates from best to worst
        seperated by a comma "," 
        for example the string 312 means candidate nb 3 the nb 1 and the worst in 2 """)
        invalid = True
        while(invalid):
            Vote = input("your vote : ")
            l = Vote.split(",")
            if ((len(Vote)==(2*nC-1)) and (len(set(l))==nC)):
                invalid = False
            else:
                print("that was invalid please try again ... ")
            rankings = []
        for i in range(0,nC):
            rankings.append(l.index(str(i)))
        m=max(rankings)
        points = []
        for i in range(0,len(rankings)):
            points=(abs(rankings[i]-m))
            voteChain.new_transaction(Candidates[i],points)
        voteChain.new_vote(proof=1000)
        Voters.remove(name.lower())
    else :
        print("you are not allowed to vote")