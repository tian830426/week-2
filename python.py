# Answer 1
def calculate(min, max, step):
    #建立新變數並宣告list陣列
    total = [min]
    #for迴圈並搭配range(start ,stop)
    #range(預設index從1開始,取整數int(最大值-最小值/ 參數step) 可得到要加幾個間隔＋1 (因為python index 從0開始)
    #取出 i= 1-3 (index 0,1,2)
    for i in range(1, int((max-min)/step)+1):
        #設定新變數 new去取得 min + 1*1
        new = min + i*step
        #假設新變數 new 小於等於 max
        if new <= max:
            #將new得到的值 增加在totle 這個list後面
            total.append(new)
            
    print("total=", total) 
    print(sum(total)) 
    
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0


#Answer 2
def avg(data):
    non_manger_salary=[]
    for i in range(0, len(data["employees"])):
        if not data["employees"][i]["manager"]:
            non_manger_salary.append(data["employees"][i]["salary"])
    
    avg_salary = sum(non_manger_salary)/len(non_manger_salary)    
    print(non_manger_salary)   
    print("avg_salary: ", avg_salary)   

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式

# Answer 3
def func(a):
    def cal(b, c):
        print(str(a), "+ (", str(b), "*", str(c), ")")
        return(a+(b*c))
    return(cal) 

print(func(2)(3, 4)) # 你補完的函式能印出 2+(3*4) 的結果 14
print(func(5)(1, -5)) # 你補完的函式能印出 5+(1*-5) 的結果 0
print(func(-3)(2, 9)) # 你補完的函式能印出 -3+(2*9) 的結果 15


#Answer 4
def maxProduct(nums):
    #設定一個空陣列
    num = []
    #建立一個i去算出參數的長度
    for i in range(0, len(nums)):
         #建立一個j去算出參數的長度
        for j in range(1, len(nums)):
            #但假設i不等於j
            if i!=j:
                #空陣列會等於所有組合相乘並且不重複
                num.append(nums[i]*nums[j])
    print('totle num',num)
    #max()取最大值 /min()取最小值
    print(max(num))
  
    #num1 = nums[0] * nums[1]
    #num2 = nums[0] * nums[2]
    #num3 = nums[0] * nums[3]
    #num4 = nums[1] * nums[2]
    #num5 = nums[1] * nums[3]
    #num6 = nums[2] * nums[3]
    
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

# Answer 5
#tw0Sum(變數)有兩個參數分別是 nums / target
def twoSum(nums, target):
    #建立變數i去取得 nums的長度 
    for i in range(0, len(nums)):
        #建立變數j去取得target的長度
        for j in range(1, len(nums)):
            #設定判斷式i不等於j ，但當nums值想加後等於target
            if i!=j and nums[i]+nums[j]==target:
                #回傳值
                return(i, j)
            
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# Answer 6
def maxZeros(nums):
    str_num = ''.join(map(str,nums))
    zero = str_num.split("1")
    le = map(len,zero)
    print(max(a))
    
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3