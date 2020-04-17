字符串、列表、字典

### 一、字符串

#### 1.1 介绍

~~~pytohn
把字符连成串. 在python中⽤用', ", ''', """引起来的内容被称为字符串
~~~

#### 1.2 常用

* 索引

  ~~~python
  v = "我在自学python"
  v1 = v[0] # 0 1 2 3 ... 从前向后
  v2 = v[-1] # -1 -2 -3 ...从后向前
  ~~~

* 切片

  ~~~python
  v = "我在自学python"
  
  ### 普通切片
  v1 = v[2:4]   # 2<= 切割索引位置 < 4 前包后不包 
  print(v1) >> 自学
  v2 = v[3:-1]  # 3<= 切割索引位置 < -1 前包后不包
  print(v2) >> 学pytho
  v3 = v[3:]    # 3<= 切割索引位置 <= -1 可以取到最后
  print(v3) >> 学python
  v4 = v[:-1]   # 0<= 切割索引位置 < -1 前包后不包
  print(v4) >> 我在自学pytho
  v5 = v[-4:-1] # -4<= 切割索引位置 < -1 前包后不包
  print(v5) >> tho
  # NOTE：对于全部是负数的索引，左边必须是小于右边，不可以v[-4:-1]
  
  ### 步长
  v1 = v[0:-1:2] # 0<= 切割索引位置 < -1 不包括最后一个，每2个字符串取一个
  print(v1) >> 我自pto
  v2 = v[1::2]    # 0<= 切割索引位置 < -1 不包括最后一个，每2个字符串取一个
  print(v2) >> 在学yhn
  v3 = v[::2]  # 取全部，每2个字符串取一个
  print(v3) >> 我自pto
  v4 = v[-1:0:-2] # 从最后一个开始，到第0个索引，但是不包括0
  print(v4) >> nhy学在
  # 注意：正常情况[-1:0] 无法获取获取索引对应的值，步长为负的时候，意思是反着取
  
  ~~~

* 切割

  ~~~python
  1) .strip() 去空格，字符串2端
  2) .lstrip() 去左边空格
  3) .rstrip() 去右边空格
  4) .split() 根据空格切割，切割后伟列表
  5) .lsplit()/.rsplit() 切割左边或者右边空格
  6) .split("a") 根据某一个字符切割
  7) .replace("a","b") 将a替换为b，如果a有多个，按顺序逐个替换，不能指定替换某一个
  ~~~

  

* 常用方法

  ~~~python
  1) .upper() 小写变大写
  2) .lower() 大写变小写
  3) .capitalize() 首字母大写
  4) .startwith("") 以什么什么开头
  5) .endwith("") 以什么什么结尾
  6) .count("") 统计某一个字符出现的次数
  7) .index("") 查找某一个元素的索引位置，不存在报错
  ~~~

* 条件判断

  > 返回True或者False

  ~~~python
  1) .isalnum() 是否由字母和数字组成
  2) .isalpha() 是否由字母组成
  3) .isdigit() 是否由数字组成(不包含小数)
  ~~~

* 补充

  ~~~python
  # format 格式化
  name = "我叫{0},今年{1}岁".format("小花","20")
  print(name)
  
  # join 拼接
  name = "tchua"
  result = "_".join(name)
  print(result)
  t_c_h_u_a
  ~~~

  

#### 1.3 练习题

~~~python
# 1.计算字符串中有多少个数字
v = "ads2kjf5adja453421sdfsdf"
total = 0
index_len = len(v)
index = 0
while True:
    val = v[index]
    flag = val.isdigit()
    if flag:
        total = total + 1
    if index  == index_len - 1:  # 字符串长度 - 1 就是字符串最大的索引位置
        break
    index += 1
print(total)

# 2.将字符串反转
v = "我在自学python"

result = v[::-1]
print(result) >> nohtyp学自在我

~~~

### 二、列表

#### 2.1 介绍

~~~python
列表是python的基础数据类型之一 ,其他编程语⾔也有类似的数据类型. 比如JS中的数组, java中的数组等. 它是以[ ]括起来, 每个元素⽤' , '隔开⽽且可以存放各种数据类型
~~~

#### 2.2  功能概述

* 索引

  ~~~python
  users = ["hua","ab","22"]
  val = users[0] # 0 1 2 
  ~~~

* 切片

  ~~~python
  users = ["hua","ab","22"]
  val = users[0:2] # 前包后不包
  print(val) >> ['hua', 'ab']
  
  # ##步长
  users = ["hua","ab","22"]
  val = users[0:2:2] # 前包后不包
  print(val) >> ['hua']
  ~~~

* 删除

  ~~~python
  users = ["hua","ab","22"]
  # 方式一
  users.pop(1) # 指定索引位置删除，索引不存在会报错，若不指定索引，默认从最后删除。
  # 方式二
  del users[1] # 指定索引位置删除，索引不存在会报错
  # 方式三
  users.remove("ab") # 删除指定元素
  ~~~

* 修改

  ~~~python
  users = ["hua","ab","22"]
  users[1] = "我"
  users[0][1] = "a" # 不可修改，因为字符串是不可变类型
  ~~~

* 独有功能

  ~~~python
  # 1. append
  users = []
  users.append("xiaohua")
  # 2. insert
  users = ["hua","ab","22"]
  users.insert(1,"xiaohua") # 在索引位置为1的地方插入指定元素
  # 3. clear
  users = ["hua","ab","22"]
  users.clear()  # 清空列表
  ~~~

* 嵌套

  ~~~python
  users = ['hua','xiaohua',True,[11,33,"Python"],[1,['tchua','huauha'],2,3]]
  
  users[0]
  users[0][2] >> 先取出hua >> 再取u
  users[3][-1] >> [11,33,"Python"] >> Python
  ~~~

* 其它

  ~~~python
  # 1. join
  v2 = " ".join(["唐开发",'李忠伟'])
  print(v2) 会以字符串的形式打印出来
  # 2. 字符串>>列表
  v1 = list("tchua")
  print(v1) >> ['t', 'c', 'h', 'u', 'a']
  # 3. 元祖>>列表
  v1 = list( (11,22,33,44,) )
  print(v1) >> [11, 22, 33, 44]
  ~~~

* 补充

  ~~~python
  # 1. 反转
  v1 = [1,2,3111,32,13]
  v1.reverse()
  print(v1) >> [13, 32, 3111, 2, 1]
  # 2. 排序
  v1 = [1,2,3111,32,13]
  
  v1.sort() 默认从小到大排序
  v1.sort(reverse=True) 从大到小排序
  ~~~

  

#### 2.3 练习题

~~~python
# 1. 请通过for循环和数字计数器实现：users = ['李邵奇','利奇航','张三丰','李子森']
users = ['李邵奇','利奇航','张三丰','李子森']
count = 0
for el in users:
    print(count,el)
    count += 1
# ## 方案二
users = ['李邵奇','利奇航','张三丰','李子森']
count = len(users)
for num in range(0,count):
    print(num,users[num])
# 2. 把下面列表以_的形式连接起来(11_22_33_44)
nums = [11,22,33,44]
for i in range(0,len(nums)):
    nums[i] = str(nums[i])
resutl = '_'.join(nums)
print(resutl)
~~~

### 三、元祖

#### 3.1 介绍

~~~python
users = [11,22,33,"我"] # 列表（可变）
users = (11,22,33,"我") # 元组（不可变）
~~~

#### 3.2 功能

~~~python
元祖功能与列表基本相同
~~~

#### 3.3 特殊

~~~python
# 1. 元祖中的元素不能被修改
v1 = (11,22,33)
v1[1] = 999 # 错误
v1 = 999  # 正确
# 2. 嵌套
v2 = [11,22,33,(11,22,33)]
v2[-1][1] = 99 # 错误
v2[-1] = 123 # 正确
# 3. 元素中有可变元素时嵌套
v3 = (11,[1,2,3],22,33)
v3[1] = 666 # 错误
v3[1][2] = 123
~~~

### 四、字典

#### 4.1 介绍

~~~python
帮助用户去表示一个事物的信息（事物是有多个属性）

# 基本格式
data = {键:值,键:值,键:值,键:值,键:值,键:值,}

~~~

#### 4.2 功能概述

* keys 获取字典中所有的键

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  for item in info: 
      print(item) >> name,age,gender,hobby
  ~~~

* values，获取字典中所有的值

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  for item in info.values():
      print(item)  >> 刘伟达,18,男，同桌
  ~~~

* items，获取字典中的所有键值对

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  for k,v in info.items():
      print(k,v)
  ~~~

* len , 统计字典长度

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  print(len(info)) >> 4
  ~~~

* 索引

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  print(info["name"]) >> 刘伟达
  print(info["age"])  >> 18
  ~~~

* 修改

  ~~~python
  # 改值
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  
  info['age'] = 22
  print(info)
  
  # 改键 删除后新增
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  
  del info['name']
  info['user'] = "刘伟达"
  
  ~~~

* 删除

  ~~~python
  info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
  
  del info['name']
  ~~~

* 补充

  ~~~python
  # 1. get
  info = {'k1':'v1','k2':'v2'}
  info['k1111'] # key不存在时会报错
  info.get('k1111') # key不存在时返回None
  info.get('k1111',999) # key不存在时返回999
  
  # 2. pop
  info = {'k1':'v1','k2':'v2'}
  
  result = info.pop('k1')  # 删除k1对应的键值对，并返回k1对应的值v1
  print(result) >> v1
  
  # 3.update
  info = {'k1':'v1','k2':'v2'}
  
  info.update({'k3':'v3','k2':'v22','k4':'v4'}) # 更新时，键值对不存在则新增，存在更新
  print(info)
  {'k1': 'v1', 'k2': 'v22', 'k3': 'v3', 'k4': 'v4'}
  ~~~

  

#### 4.3 练习题

~~~python
# 1. 登录验证
userinfo = {'usenrame':'alex','password':"oldboy"}

user = input('请输入用户：')
pwd = input('请输入密码：')

if userinfo['username'] == user and userinfo['password'] == pwd:
    print('登陆成功')
else:
    print('用户名或密码错误')
    
# 2. 判断 ‘v2’ 是否在字典的value中 v = {'k1':'v1','k2':'v2','k3':'v3'}
v = {'v2':'v1','k2':'v2','k3':'v3'}

for item in v.values():
    if item == 'v2':
        print("存在值中")

~~~

### 五、集合

#### 5.1 介绍

~~~python
set集合是python的一个基本数据类型. ⼀般不是很常⽤. set中的元素是不重复的.⽆序的.⾥面的元素必须是可hash的
# 定义
set()
~~~

#### 5.2 功能概述

* 增加

  ~~~python
  s = {1,2,'k1','hua'}
  s.add("k2")
  print(s) >> {1, 2, 'k2', 'hua', 'k1'}
  
  s.add("k1") >> # 重复内容不会添加
  ~~~

* update 迭代增加

  ~~~python
  s = {1,2,'k1','hua'}
  s.update("23")  # 会把23打散并以字符串的形式增加
  print(s) >> {1, 2, 'hua', '2', 'k1', '3'}
  ~~~

### 六、内存相关

~~~python
# 1. 内部修改
v1 = [11,22,33]
v2 = v1 
v1.append(666)
print(v2) # 含 666 >> [11,22,33,66]

总结：对于list, set, dict来说, 直接赋值. 其实是把内存地址交给变量，并不是复制⼀份内容，所以，v1的内存指向和v2是一样的. lst1改变了, lst2也发⽣生了改变

# 2. 重新赋值
v1 = [11,22,33]
v2 = v1
v1 = [1,2,3,4]

print(v2) >> [11,22,33] 

总结：v1重新赋值，等于开辟新的内存，这样v1 v2内存地址指向就不一样了
~~~

== 和 is有什么区别？

* == 用于比较值是否相等
* is 用于比较内存地址是否相等