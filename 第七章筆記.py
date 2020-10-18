#import套件語法 
#import 套件 from 套件 import模組  from 套件 import模組 as 別名
   
# import pandas
# pandas.Series([1,2,3,4,5])
# print(pandas.Series([1,2,3,4,5]))

# from 套件 import模組
# from pandas import Series
# Series([1,2,3,4,5])
# print(Series([1,2,3,4,5]))


#from 套件 import模組 as別名
# from pandas import Series as kikilove 
# kikilove ([1,2,3,4,5])
# print(kikilove ([1,2,3,4,5]))

#撰寫函數用def,在設定函數名稱,用()加入參數,記得':'

# def draw_linel():
#     print(20*'*')#'*'的*是可以替換的
# print(draw_linel())


# def draw_linel():
#     print(20*'*')
# #需要重複執行時重複函數名
# draw_linel()
# draw_linel()
# draw_linel()
# draw_linel()
# draw_linel()
# print(draw_linel())

#可以用參數的寫法
# def draw_line2(n,symbol):
#     print(n*symbol)#'*'的*是可以替換的
# draw_line2(20,'*')
# print(draw_line2(20,'*'))


# def draw_line2(n,symbol):
#     print(n*symbol)#'*'的*是可以替換的
# draw_line2(20,'+')#(數量,'印出符號')括號中的參數的值是可以改變的
# print(draw_line2(20,'+'))


#定義加法函數並回傳
# def add(a,b):
#     return a+b
# result = add(1,2)
# print(result)

# def swap(a,b):
#     return b,a#return 反轉串列並回傳
# swap(3,5)
# print(swap(3,5))

#函數中的參數不固定使用"arg"，並使用元組(tuple)存放
#arg允許輸入不固定長度的參數
# def answer(*arg):
#     print('輸入參數的資料型態',type(arg),'其值為:',arg)
#     for i in arg:
#         print(i)
# answer(1,2,3,4,5,6,7,8,9,10)

 # def string_to_list(***kwarge):
 #     print(values)
     
























