import numpy as np
from matplotlib import pyplot as plt
import wave
import struct

Amax = 1000 #最大振幅
Fs = 44100 #サンプリング周波数
sec = 0.5 #時間

# 金属
A = -1000 #最大振幅
B = 30 #減衰率
w = 2000 #角周波数

# 木
""" A = -500
B = 40
w = 250 """

# ゴム
""" A = -1000
B = 40
w = 100 """

Qt = []

step = np.linspace(0,sec,Fs)
print(step)
for t in step:
    qt = A*np.exp(-B*t)*np.sin(w*t)
    Qt.append(qt)

plt.plot(step,Qt)
plt.show()

Qt = [int(step/Amax *32767.0) for step in Qt] #16bit符号付き変数に変換

#バイナリ化
binwave = struct.pack("h"*len(Qt), *Qt)

#減衰正弦波をwavファイルとして書き出し
w = wave.Wave_write(str(A)+"exp(-"+str(B)+"t)sin("+str(w)+"t).wav")
p = (1,2,Fs,len(binwave),'NONE','not compressed')
w.setparams(p)
w.writeframes(binwave)
w.close()
