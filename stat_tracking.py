def main():
    match_series,total_gms,_t_pinfall=scores()
    t_average,ong_avg=avg_calculation(match_series,total_gms,_t_pinfall)
    handicap=handicap_calc(ong_avg)
    print()
    print("This Week's Series: ", match_series)
    print("Today's average: ",format(t_average,'.2f'))
    print('Total Games for Season: ', total_gms)
    print('Total Pinfall: ', _t_pinfall)
    print('YTD League Average: ', format(ong_avg,'.2f'))
    print('Your Handicap Next Week: ', format(handicap,'.0f'))


def scores():
    '''date=input('enter date of match: ')'''
    score_lst = []
    while len(score_lst) != 3:
        if len(score_lst) == 0:
            scores = int(input('enter first game '))
        elif len(score_lst) == 1:
            scores = int(input('enter second game '))
        elif len(score_lst) == 2:
            scores = int(input('enter third game '))

        if scores >= 0 and scores <= 300:
            score_lst.append(scores)
        else:
            print('invalid scores try again')
    #writing to file for use in score review function. might revise to
    #dictionary later.
    with open('scoring.txt','a') as score_list:
        for item in score_lst:
            #the below line %s is a placeholder value item will insert
            #when called \n is a new line so the file will create lines for
            #each value. the % next to item is to pass item's values to the
            #placeholder
            score_list.write('%s\n' % item)

    all_games=[]
    with open('scoring.txt','r') as gl:
        for line in gl:
            #the below variable removes the newline character from each line
            # the -1 index is the last character in each string
            cp=line[:-1]
            all_games.append(cp)
    #list comprehension to convert list string to integers
    pinfall=[int(x) for x in all_games]


    total_games=len(all_games)

    total_pinfall=sum(pinfall)

    series=sum(score_lst)

    return series,total_games,total_pinfall

def avg_calculation(series,total_games,total_pinfall):

    average=series/3
    ong_average=total_pinfall/total_games


    return average,ong_average

def handicap_calc(ong_average):
    if ong_average<230:
        handi=(230-ong_average)*.95
    else: handi=0

    return handi















main()