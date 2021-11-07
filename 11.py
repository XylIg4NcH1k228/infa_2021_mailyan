names = []
best = []
last = []
with open('score_board.txt', 'r') as g:
    for line in g.readlines():
        if line != '\n':
            a = line.split(':')
            names.append(a[0])
            b = a[1].split('|')
            last.append(int(b[0][8:len(b[0])]))
            best.append(int(b[1][8:len(b[1])]))
print(best)                
for j in range(len(names)):

    for i in range(0, len(names)-1-j):
        if best[i] < best[i+1]:
            m = best[i]
            best[i] = best[i+1]
            best[i+1] = m

            
            m = names[i]
            names[i] = names[i+1]
            names[i+1] = m

                
            m = last[i]
            last[i] = last[i+1]
            last[i+1] = m
        i += 1
print(best)
