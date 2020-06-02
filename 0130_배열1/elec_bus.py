import sys

sys.stdin = open('elec_bus.txt', 'r')

testcase = int(input())

for i in range(1, testcase + 1):
    read = input().split(' ')
    fuel_limit = int(read[0])
    track_distance = int(read[1])
    number_of_station = int(read[2])
    station_list = list((map(int,input().split())))
    station_list.append(track_distance)
    print(fuel_limit, track_distance, number_of_station)
    print(station_list)
    #########################3
    distance = 0
    count = 0
    station_number = 0

    for j in range(track_distance):

        if fuel_limit > 0:  #아직 기름이 남아잇을때
            distance += 1
            fuel_limit -= 1
            print('방금 {} 칸으로 옴, 기름은 {}가 됨'.format(distance, fuel_limit))
        if fuel_limit ==0 :
            print('기름 다떨어짐')
            if distance not in station_list:
                print("도달하지 못햇도다")
                count = 0
                print(count)
                print('============================이게 정답입니다============================')
                break
        if distance == track_distance:
            print("왓노라 보았노라 풀엇도다")
            print(count ,  '\n============================이게 정답입니다============================')

            break
        ##만약에 주유소가 있다면


        if distance in station_list:
            print('#########{} 번째 주유소 도착########'.format(station_number+1))
            ##주유한다
            if fuel_limit <  station_list[station_number + 1] - distance:
                fuel_limit = int(read[0])              ##주유를 한다면 fuel limit을 다시 int(read[0])으로 채운다
                print('주유했다 기름이 {}이 되었다'.format(fuel_limit))
                count += 1
            ##주유를 안한다
            elif fuel_limit >=  station_list[station_number + 1] - distance:
                print('주유소가 있었지만 안하고 지나갓음')
                pass
            station_number += 1
        else:
            print('주유소가없으므로 그냥가겠음')





