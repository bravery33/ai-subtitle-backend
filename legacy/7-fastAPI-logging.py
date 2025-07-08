import logging

""" 
[level]
레벨            설명                                출력조건
----------------------------------------------------------------------------
DEBUG           상세한 내부 상태 출력(개발단계)     level=logging.DEBUG
INFO            일반적인 정보 메시지                INFO 이상
WARNING         경고 사항                           WARNING 이상
ERROR           에러 사항                           ERROR 이상
CRITICAL        치명적 오류                         항상 출력

[로그 레벨 순서]
DEBUG < INFO < WARNING < ERROR < CRITICAL
"""

## 1. 로깅 기본 설정
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s [%(levelname)s] - %(message)s')

## 2. 로거 객체 생성
logger = logging.getLogger(__name__)

userName = '홍길동'

## 3. 로그 출력
logger.debug('디버깅 메시지')
logger.info(f'정보 메시지 : {userName}')
logger.warning('경고 메시지 : %s %s', userName, '박보검')
logger.error('에러 메시지')
logger.critical('치명적인 에러 메시지')