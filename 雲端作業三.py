# # 1. 假設score是投籃者的姓名和每次投進的球數，score = [' 小徐',5,9,6,8,7,10,6]，請取得投籃者的姓名和投進的球數。
# list = score = [' 小徐',5,9,6,8,7,10,6]

# x = list[0:10]

# print(x)


# # (1) 請用max函數計算小徐最多進了幾球。

# list = score = [' 小徐',5,9,6,8,7,10,6]

# y = list[0]

# x = max(list[1:7])

# print(y+'最多進了幾球:', x,'顆')


# # (2) 使用min函數計算小徐最少進了幾球。

# list = score = [' 小徐',5,9,6,8,7,10,6]

# x  = min(list[1:7])

# y = list[0]

# print(y+'最多少了幾球:', x ,'顆')



# # (3) 用sorted計算小徐進球數最多的三回合各投入多少球。
# list = score = [' 小徐',5,9,6,8,7,10,6]
 
# x = sorted(list[1:7][-3:])

# y = list[0]

# print(y+'進球數最多的三個回合',x)
 

# # (4) 計算小徐進球數最少的三回合各投入多少球。

# list = score = [' 小徐',5,9,6,8,7,10,6]
 
# x = sorted(list[1:7][0:3])
 
# print(list[0]+'進球數最少的三個回合',x)

# # (5) 用sum()和len()計算小徐進籃的平均球數。

# list = score = [' 小徐',5,9,6,8,7,10,6]

# a = sum(list[1:7])

# b = len(list[1:7])

# print(list[0]+'進籃的平均球數:',a/b)

#2. 請寫一個9*9乘法表，注意輸出格式的對齊(個位對個位、十位數對十位數)
# #    
# i = 1
# while  i <= 9:
#     j = 1
#     while j <= 9:
#           result = i * j
#           print("%d*%d=%-3d" %(i,j,result),end ="")
#           #end  ="  " (換行用)
#           j += 1
#     print()
#     i += 1

#小明寫情書給女朋友abey，想寫I love you so so ... (隨機次數) much。請改以for 迴圈來完成此題。

# import random #random 是隨機數模組套件

# x = random.randint(1, 100)#設定隨機數X 

# y = 'I Love You'
# print(y,end=' ')
# for i in range(x):
#     print('so',end=' ')
# print('much')
































