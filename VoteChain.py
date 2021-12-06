import hashlib
import json
from time import time

# the votes'chain is composed of blocks that representes the vote casted by a voter 
# when voting, the user ranks all the candidates from best to worst thus giving each one a score
# these scores represents the transactions 

class VoteChain(object):
    def __init__(self):
        self.votes =[]
        self.pending_transactions = []
        self.new_vote(previous_hash="SPQR")
    
    def new_vote(self,proof=None,previous_hash=None):
        vote = {
            'index' : len(self.votes) + 1,
            'timestamp' : time(),
            'transaction' : self.pending_transactions,
            'proof' : proof,
            'previous_hesh' : previous_hash or self.hash(self.votes[-1])
        }
        self.pending_transactions =[]
        self.votes.append(vote)

        return vote

    @property
    def last_vote(self):
        return self.votes[-1]

    def new_transaction(self,candidate,amout):
        transaction = {
            'recipient' : candidate,
            'amount' : amout
        }
        self.pending_transactions.append(transaction)
        return self.last_vote['index'] + 1

    def hash(self,block):
        string_object = json.dumps(block,sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

