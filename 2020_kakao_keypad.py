def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
              4:(1,0), 5:(1,1),6:(1,2),
              7:(2,0), 8:(2,1),9:(2,2),
              '*':(3,0), 0:(3,1),'#':(3,2)}
    
    left = [1,4,7]
    right = [3,6,9]
    
    lhand = '*' # 초기위치
    rhand = '#' # 초기위치
    
    for i in numbers:
        if i in left:  # 왼쪽 열 숫자
            answer += 'L'
            lhand = i
        elif i in right: # 오른쪽 열 숫자
            answer += 'R'
            rhand = i
        else: # 가운데 열 
            curPos = key_dict[i] # 현재 눌러야할 숫자 좌표
            lPos = key_dict[lhand] # 왼손 위치 좌쵸
            rPos = key_dict[rhand] # 오른손 위치 좌표
    
            # 왼손과 오른손의 거리를 계산
            ldist = abs(curPos[0] - lPos[0]) + abs(curPos[1] - lPos[1])
            rdist = abs(curPos[0] - rPos[0]) + abs(curPos[1] - rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else: 
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
            
    return answer