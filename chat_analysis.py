from tkinter.messagebox import RETRY
import numpy as np

#사용 방식 : chat=ChatLog(path);   chat.analysis("tom","all") 
#톡방에 있는 인원 닉네임 파악, 사용기간

#return 형식은 dict형식 하나, top 5까지 , top1이 포함된 문자열 갯수 
class ChatLog:
    

    raw_txt=None
    result_dict=dict()
    

    def __init__(self,path) -> None:                #chat파일을 불러옴
        self.raw_txt=open(path,'r',encoding="UTF-8").readlines()
    def analysis(self,user,date) -> dict:       #date : all / year / month/ week / day
        
        # chat txt 를 기간에 맞게 resize
        if date=="all":
            pass
        elif date=="year":
            pass
        elif date=="monty":
            pass
        elif date=="week":
            pass
        elif date=="day":
            pass
        else:
            print("wrong type!")
            return
    
        return 
        # 이후  txt파일을 완전 탐색하여 


a=ChatLog("chat_log/sample.txt")
for line in a.raw_txt:
    l=line.rstrip().rsplit(" ")
    print(l)
    
