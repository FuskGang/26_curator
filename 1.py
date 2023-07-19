with open('ex.txt') as f:
    n, k = map(int, f.readline().split())
    
    st = dict()
    vuz = dict()
    
    for _ in range(n):
        id_st, id_vuz, mon = map(int, f.readline().split())
        st[id_st] = [id_vuz, mon, 0]
        
    for _ in range(4 * n):
        id_st, *ex = map(int, f.readline().split())
        
        if 100 in ex:
            st[id_st][1] += 100
            st[id_st][2] += 100
        else:
            st[id_st][2] += (sum(ex) // 3)
    
    for _ in range(k):
        id_vuz, budz, price = map(int, f.readline().split())
        
        vuz[id_vuz] = [budz, price, []]
        
    
    for st_id, info in st.items():
        id_vuz, mon, ball = info
        vuz[id_vuz][2].append((ball, st_id))
    
    cnt_dolg = 0
    dolg = -10000000
        
    for id_vuz, info in vuz.items():
        budz, price, info_st = info
        
        info_st = sorted(info_st, reverse=True)
        
        for ball, st_id in info_st[budz:]:
            if info_st[budz - 1][0] == ball:
                continue
    
            babki = st[st_id][1] - price
            
            if babki < 0:
                cnt_dolg += 1
                dolg = max(dolg, babki)         
                
    print(cnt_dolg, abs(dolg))
