import datetime


# current_time = datetime.datetime.now()
# print("current_time : ", current_time)

# today=datetime.date.today()
# print("today : ", today)



childName_list = ['이채은', '김재원', '김정윤']
profileUrl_list = ['https://hellokids.ap-northeast-2.s3.amazonaws.com/1_대동어린이집/profile/2019-06-15_이채은_2023090.jpg', 
                   'https://hellokids.ap-northeast-2.s3.amazonaws.com/1_대동어린이집/profile/2018-07-01_김재원_2023090.jpg', 
                   'https://hellokids.ap-northeast-2.s3.amazonaws.com/1_대동어린이집/profile/2019-09-09_김정윤_2023090.jpg']

today = datetime.date.today()
print("today : ", today)

# 반복문
if len(profileUrl_list) == len(childName_list) :

    h = 0
    for h in range( len(profileUrl_list) ) :

        new_filename = childName_list[h] +'_'+ str(today)

        i = 0
        for i in range( len(profileUrl_list) ) :
            j = 0
            for j in range( len(profileUrl_list) ) :

                print( "childName_list : ", childName_list[j] )
                print( "profileUrl_list : ", profileUrl_list[i] )

                j = j+1
            i = i+1
        print("new_filename : ", new_filename)
else : 
    print("길이 다름")