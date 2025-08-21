n, x = map(int, input().split())

blog = list(map(int, input().split()))

current_sum = sum(blog[:x])

max_blog = current_sum
count = 1

for i in range(x, n):
    current_sum += blog[i] - blog[i - x]
    if current_sum > max_blog:
        max_blog = current_sum
        count = 1
    elif current_sum == max_blog:
        count += 1

if max_blog == 0:
    print("SAD")
else:
    print(max_blog)
    print(count)