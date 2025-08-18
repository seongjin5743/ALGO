n = int(input())

channel = [input() for _ in range(n)]

answer = ''

index_kbs1 = channel.index('KBS1')
answer += '1' * index_kbs1
answer += '4' * index_kbs1

channel.remove('KBS1')
channel.insert(0, 'KBS1')

index_kbs2 = channel.index('KBS2')
answer += '1' * index_kbs2
answer += '4' * (index_kbs2 - 1)

print(answer)