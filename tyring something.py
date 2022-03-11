date='12/7/2018'
scores=[185,195,205]

score_d={date:scores}
print(score_d)

scoring=open('scroring.txt','a')
scoring.write(str(score_d))
scoring.close()
print(scoring)