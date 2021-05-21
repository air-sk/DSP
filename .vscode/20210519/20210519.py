import matplotlib.pyplot as plt#导入matplotlib.pyplot并命名为plt
import numpy as np#导入nunpy并命名为np
x=np.linspace(0,3*np.pi,100)#在0到3π之间取100个点作为x轴坐标
y=np.sin(x)#y轴为一sin函数

plt.rcParams['font.sans-serif']=['SimHei']#图表能够显示中文
plt.rcParams['axes.unicode_minus']=False    #能显示正负号

plt.subplot(121)#在第一行第一列输出第一幅图像
plt.title(r'$f(x)=sin(x)$')#输出图像标题f(x)=sin(x)
plt.plot(x,y)#通过x，y描点画图
x1=[t*0.375*np.pi for t in x]#循环把x中每一个元素进行t*0.375*np.pi运算，生成一串新的x轴坐标
y1=np.sin(x1)#y轴为一sin函数
plt.subplot(122)#在第一行第二列输出第二幅图像
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8} \pi$')#输出图像标题f(x)=sin(wx)，w=3π/8
plt.plot(x,y1)#通过x，y1描点画图
plt.show()#在屏幕输出图像