# show_chat_log_frequency
카카오톡으로 내보내진 채팅로그를 분석하여 간단한 최대빈도 단어를 찾아내는 프로그램


## 사용방법
import chat_analysis

a=chat_analysis.ChatLog("chat_log\sample.txt")

a.analysis([user name],time_keyword)     time keyword는 all year month week day가 있음.

analysis함수는 반환형을 가지고 있어, 반환을 받을 수도 있음.
