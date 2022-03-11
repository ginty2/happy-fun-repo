class Score_tracking:

    def __init__(self):
        self.__match_date=''
        self.scores=0

    def score_entry(self):
        score_lst=[]

        self.scores=int(input('enter match scores'))