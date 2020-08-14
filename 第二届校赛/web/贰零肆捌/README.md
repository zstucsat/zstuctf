**考点：**

1）简单代码审计

a、 totp算法一次性验证；

b、前端修改数据绕过

2）md5强碰撞

3）PHP黑魔法

4）Linux基础

**难度：**一般

**思路：**

1）查看HTTP头可发现hint

2）查看JS源码发现前后端交互流程以及得到bypass思路

3）根据bypass思路撰写脚本到达第二关

脚本exp_web41.py

4）一共四个绕过

脚本exp_web42.py

a、md5强碰撞；

b、php弱类型+暴力破解；

c、is_numric()漏洞

d、linux基础+反斜杠绕过

