## 파일 실행 폴더 생성
import os
from datetime import timedelta
"""
* 초 단위 시간을 SRT 형식(HH:MM:SS,mmm)으로 변환
* datetime.timedelta() 
: float 초 반환
: 내부적으로 days, seconds, microseconds 등을 관리
: 3662.567ch -> 0 days, 1 hour, 1 minutes, 2 seconds, 567 microseconds
"""
seconds = 3662.567

td = timedelta(seconds=seconds)
print(td)

'''
* 전체 초를 3600(1시간)으로 나워 시간만 추출
* // 는 나눗셈 후 소수점 버림
'''
hours = int(td.total_seconds()) // 3600
print('hours >>',hours)

'''
* 전체 초에서 시간 부분을 뺀 나머지
* 이 중 60으로 나눈 몫
'''
minutes = int(td.total_seconds() % 3600 // 60)
print('minutes >>', minutes)

'''
* 전체 초에서 60으로 나눈 나머지
'''
seconds = int(td.total_seconds() % 60)
print('seconds >>', seconds) 

'''
* 소수점 아래 부분 추출 -> 밀리초로 변환
* 3662.567 % 1 = 0.567 -> 0.567 * 1000 = 567
* milliseconds
'''
milliseconds = int((td.total_seconds() % 1) * 1000)
print('milliseconds >>', milliseconds)

result = f'{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}'
print('result >>', result)