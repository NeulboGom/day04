#LIST
'''
scores=("B+","A+","C+")
print(scores[1])
listed=list(scores)
print(listed)
listed[1]="C+"
listed[2]="A+"
scores=tuple(listed)
print(scores)
'''
import copy

big_bang=["GD","태양","탑","대성","승리"]
big_bang.insert(1,"인하")

#print(big_bang)
#print(big_bang*2)

exo=["백현","첸"]


#extend
#exo.extend(big_bang)
print(exo)

#append
exo.append(big_bang)
#print(exo)
#print(exo[2][2])

# offset으로 항목 바꾸기
exo[1]="시우민"
print(exo)

#삭제 방법: delete / remove / pop
#pop은 맨 뒤에 있는걸 삭제하고 동시에 Return 한다.

print(exo[2].pop())  #승리 pop
print(exo[2].pop(-2))  #탑 pop
del exo[2][-1]  #대성 delete
exo[2].remove("인하")
print(exo)



'''
primes.sort()
print(primes)  #원본 바뀜
'''
'''primes_sorted=sorted(primes)
print(primes)
print(primes_sorted)  #원본이 안 바뀐다.
'''


'''
# 리스트 정렬 및 얕은 복사
primes=[2,19,3.0,5,7,11]
primes_cp=primes

print(primes)
print(primes_cp)
primes[-1]="Lunch time"
print(primes)
print(primes_cp)
'''

'''
#얕은 복사에 따른 각자 다른 객체들
a=[1,2,3]
b=a.copy()
c=list(a)
d=a[:]

a[0]="Start!"
d[2]="check"

print(a,b,c,d)'''


# deepcopy
import copy
a=[1,2,[5,-9]]
b=copy.deepcopy(a)

a[2][1]=7  #mutable, but deepcopy
print(a,b)


#comprehension

# odd_list=[]
# for i in range(1,11):
#     if i%2==1:
#         odd_list.append(i)
# print(odd_list)

#odd_list=[i for i in range(1,11) if i%2==1]
odd_tuples=(i for i in range(1,11) if i%2==1)
print(odd_tuples)