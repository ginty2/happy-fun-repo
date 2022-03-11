


def handicap_calc():
    ong_average=168.7
    if ong_average<230:
        handi=(230-ong_average)*.95
    else:handi=0

    print(format(handi,'.0f'))

handicap_calc()