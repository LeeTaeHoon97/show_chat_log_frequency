from datetime import datetime
import sys
import copy


class ChatLog:
    
    one_day=3600*24
    latest_day=None
    raw_txt=None

    def __init__(self,path) -> None:                #chat파일을 불러옴
        self.raw_txt=open(path,'r',encoding="UTF-8").readlines()
        self.latest_day=self.get_latest_day(self.raw_txt)


    def get_latest_day(self,txt):
        for i in range(len(txt)-1,-1,-1):
            line=txt[i].rstrip().split(" ")
            if line[0]=='---------------' and line[-1] == '---------------':                # 마지막 날의 날짜 확인
                some_time=self.make_datetime(line[1:4])
                return some_time

    def make_datetime(self,List_lst):
        temp=""
        for i in List_lst:
            i=i[:-1]
            if len(i)==1:
                i='0'+i    
            temp+=i
        res=datetime.strptime(temp,'%Y%m%d').date()
        return res


    def analysis(self,String_user,String_date) -> dict:       #date : all / year / month/ week / day
        Dict_date={"all":sys.maxsize,"year":365,"month":30,"week":7,"day":1}
        Dict_word={}
        Dict_result={}
        Dict_result2={}
        is_analyze=False

        if String_date not in Dict_date.keys():
            print("wrong type!")
            return
        else:
            for lines in self.raw_txt:
                line=lines.rstrip().rsplit(" ")                                                 #한줄의 단어가 들어있는 리스트
                if line[0]=='---------------' and line[-1] == '---------------' and is_analyze == False:                # 분석이 시작되지 않고, 상단부일때 날짜 확인
                    some_time=self.make_datetime(line[1:4])

                    if ((self.latest_day-some_time).total_seconds()//self.one_day) <= Dict_date[String_date]:          # 날짜부가 지정한 키워드 이내일 경우 분석시작
                        is_analyze=True
                elif is_analyze:
                    if line[0] not in Dict_result:
                        Dict_result[line[0]]=copy.deepcopy(Dict_word)           #line[0] mean user name
                    for word in line[3:]:                                       #본문 내용은 line[3]부터
                        if word not in Dict_result[line[0]]:
                            Dict_result[line[0]][word]=1
                        else:
                            Dict_result[line[0]][word]+=1
            
            is_analyze=False

            String_user='['+String_user+']'

            best_words=sorted(Dict_result[String_user].items(),key=lambda x:-x[1])[:5]     #최다 사용 단어 Top5

            Dict_str={}
            for w,_ in best_words:
                Dict_str[w]=0
            """
            위에서 찾은 단어가 포함된 문자열
            """

            for lines in self.raw_txt:
                line=lines.rstrip().rsplit(" ")                                                 #한줄의 단어가 들어있는 리스트
                if line[0]=='---------------' and line[-1] == '---------------' and is_analyze == False:                # 분석이 시작되지 않고, 상단부일때 날짜 확인
                    some_time=self.make_datetime(line[1:4])

                    if ((self.latest_day-some_time).total_seconds()//self.one_day) <= Dict_date[String_date]:          # 날짜부가 지정한 키워드 이내일 경우 분석시작
                        is_analyze=True
                elif is_analyze:
                    if line[0] not in Dict_result2:         
                        Dict_result2[line[0]]=copy.deepcopy(Dict_str)
                    for word in line[3:]:
                        for w, _ in best_words:
                            if word.find(w)!= -1:    # 단어가 포함된 문자열 발견 시 
                                Dict_result2[line[0]][w]+=1 
         
            
            best_str=(Dict_result2[String_user])
            Dict_date_keyword={"all":"","year":" 일년 간","month":" 한달 간","week":" 일주일 간","day":" 하루 간"}
            print(f"{String_user}님의{Dict_date_keyword[String_date]} 최다 사용 단어는\n{best_words}입니다.")

            print(f"{String_user}님의{Dict_date_keyword[String_date]} 최다 사용 단어가 포함된 횟수는\n{best_str}입니다.")

            return [best_words,best_str]
