#Ch4 5
# 請同時用for迴圈和串列表達式來練習將'Simon Peter John'變成['S****', 'P****', 'J***']。
# string1='Simon Peter John'
# b=string1.split()
# t='*'
# for i in range (0,3):
#   print(b[i][0],end='')
#   print(t*(len(b[i])-1),end=' ')


# 請將['Company 1','Company 2','Company 3']變成['Company_1', 'Company_2', 'Company_3']（這個題目很實用，許多時候我們拿到的資料會有空格，但變數命名不允許空格。可以用這個方法解決！）
# x = ['Company 1','Company 2','Company 3']
# t = []
# for i in range(0,3):
#     t.append(x[i].replace(' ','_'))
#     print(t)





# 請將[1,2,3,4,5,6]變成['1$', '2$', '3$', '4$', '5$', '6$']。zip
# list1 = [1,2,3,4,5,6]
# string2 = []
# for i in list1:
#     string2.append(str(i)+'$')
# print(string2)


   
# # 承上題，請把['1$', '2$', '3$', '4$', '5$', '6$']，還原成[1,2,3,4,5,6]。
# x =['1$', '2$', '3$', '4$', '5$', '6$']
# z = []
# for i in range(0,5):
#     z.append(int(x[i].replace('$',' ')))
#     print(z)


   
# 請將[1,2,3,4]和[5,6,7,8]變成[(1, 5), (2, 6), (3, 7), (4, 8)]
# list1 = [1,2,3,4]

# list2 = [5,6,7,8]

# print(list(zip(list1,list2)))

# 1. 我們做個練習，用字典來建立文字次數的計算程式。字串s 的內容為：
# s = "I love you and you love him and who loves who"
# 在s中，I出現1次，love出現2次。我們將引導同學一步一步完成本題組。
# (1)	先用split()將s分解成不同的串列元素，用空白鍵為區隔。
# name  = s = {'I' 'love' 'you' 'and' 'you' 'love' 'him' 'and' 'who' 'loves' 'who'}
# (2) 請用set()算出共有幾個不同的字，並存到keys變數。
# (3) 請建立一個字典，其鍵值是keys裡的元素，但值都為0。
# (4) 請寫一個for迴圈將s裡的每個字取出，並將上題的字典依其對應的「鍵」將「值」加1。最後的答案會是：{'I': 1, 'and': 2, 'him': 1, 'love': 2, 'loves': 1, 'who': 2, 'you': 2}。

# s="I love you and you love him and who loves who"#字串建立成字典

# x=s.split()

# keys=set(x)#set函數是為了找出字串的相異值並存進 字典Key裡

# values=[0 for i in keys]#key值裡的元素0
# d={key:value for key,value in zip(keys,values)}#字典語法 key:value for key,再用zip結合
# for i in x:
#     d[i]+=1#
# print(d)




































