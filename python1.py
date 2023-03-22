keymap = ["AA"]
targets = ["B"]

def solution(keymap, targets):
    answer = []
    # targets 의 "ABCD"에 대해서
    for target in targets:
        cnt = 0
        # "ABCD"의 "A"에 대해서 
        for t in target:
            i_list = []
            # keymap의 "AVACD"에서 
            for i in range(len(keymap)):
                # "A"가 "AVACD"에 존재하면
                if t in keymap[i]:
                    i_list.append(keymap[i].index(t)+1)
            if i_list:        
                cnt += min(i_list)
            else:
                cnt = -1
        answer.append(cnt)
            
    return answer

print(solution(keymap, targets))