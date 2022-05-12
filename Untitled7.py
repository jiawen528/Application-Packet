#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商餘額明顯不足')


# In[ ]:




