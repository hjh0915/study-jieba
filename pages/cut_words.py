import jieba

# 读文件 jieba库
txt = open("三国演义.txt","r",encoding = "utf_8").read()
words = jieba.lcut(txt)  

# 列表变成字典
counts = {}
for word in words:
    if len(word) == 1: # 将"曰"还有"特殊符号"这些一个字的筛掉
        continue
    else:
        counts[word] = counts.get(word,0) + 1

# 排序
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)

# 取出排名前10并打印
for i in range(20):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))