dust = 49

if dust > 50:
    print('50 초과')
else:
    print('50 이하')

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
