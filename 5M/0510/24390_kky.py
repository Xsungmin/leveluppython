time = input()
# 분 저장
ans = 0
m = int(time[:2])
# 초 저장
s = int(time[3:])
ans += m//10 + m%10
# 30초 이상 > 시작버튼을 누르고 타이머세팅
# 30초 미만 > 시간을 세팅하고 시작
if s >= 30:
    ans += (s-30)//10
else:
    ans += s//10
print(ans+1)
