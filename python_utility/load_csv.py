import numpy as np
import pandas as pd
import os

data = {}
learned= {}

def load_csv(): #csv파일 불러오는 인터페이스
        global data
        print("어떤 파일을 읽어 오시겠습니까?")
        file_list = os.listdir()
        for x in range(len(file_list)):
            print(str(x) + ' : ' + file_list[x])

        while True:
            inp = int(input("INSERT : "))
            file_name = file_list[inp].split(".")
            if len(file_name)!= 2:
                print("파일 형식이 유효하지 않습니다")
            elif file_name[1]!="csv":
                print("파일 형식이 .csv가 아닙니다")
            else:
                data[file_name[0]] = pd.read_csv(file_list[inp])
                break

def print_data():#데이터 프레임 출력 인터페이스
    key = list(data.keys())
    print("어떤 데이터를 출력하시겠습니까?")
    for x in range(len(key)):
        print(x,":",key[x])
    while True:
        inp = int(input("INSERT : "))
        if inp >= 0 and inp <= len(key):
            print(data[key[inp]])
            break
        else:
            print("유효하지 않은 입력입니다.")
