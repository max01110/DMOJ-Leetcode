nums = [-1,-1]
k = 1
book = {}
values = []
for i in nums:
    if i in book:
        book[i] += 1
    else:
        book.update({i:1})

book = sorted(book, key=book.get, reverse=True)
for p in book:
    values.append(p)
    if len(values)==k:
        break

print(values)
