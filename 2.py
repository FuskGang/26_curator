with open('ex1.txt') as f:
    n, k = map(int, f.readline().split())
    tm = []
    
    for _ in range(n):
        st, end = map(int, f.readline().split())
        
        if st == end:
            tm.append([st, st, end])
        else:
            tm.append([st + end, st + end, end])
            
    tm.sort()
    cnt = 1
    ans_cnt = 0
    fl = False
    ans = 0
    
    tm[0][0] += 240
    
    for i in range(1, len(tm)):
        cnt += 1
        tm[i][0] += 240 * (i + 1) - (tm[i][1] - tm[i - 1][1])
        
        if cnt == k:
            ans = tm[i][0]
            fl = True
        
        if fl:
            if tm[i][1] > ans:
                ans_cnt += 1
        
            
print(ans_cnt, ans)
