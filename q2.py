# 랜덤으로 스터디 날 정함
# 4일부터 28일 이내

from random import *
studyDate = int(random() * 24) + 4

print('오프라인 스터디 모임 날짜는 매월', studyDate, '일로 선정되었습니다.')