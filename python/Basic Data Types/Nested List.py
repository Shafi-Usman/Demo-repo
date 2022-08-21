result = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    result.append([name,score])
    scores.append(score)
    
scores = list(set(scores))
scores.sort()
b = [i[0] for i in result if i[1] == scores[1]]
b.sort()
for i in b:
    print(i)


