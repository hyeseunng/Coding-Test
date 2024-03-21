# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

import datetime
d=datetime.date.today()
print(d.isoformat())