#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wave
import numpy as np

def read_wav_data(filename):
  wav = wave.open(filename,"rb") # 打開一個wav格式的聲音文件流
  frame = wav.getnframes() # 獲取幀數
  channel=wav.getnchannels() # 獲取聲道數
  framerate=wav.getframerate() # 獲取幀速率
  sample_width=wav.getsampwidth() # 獲取實例的比特寬度，即每一幀的字節數

  print("frame=%i, channel=%i, framerate=%i, sample_width=%i" %(frame, channel, framerate, sample_width))

  str_data = wav.readframes(frame) # 讀取全部的幀
  wav.close() # 關閉流
  wave_data = np.fromstring(str_data, dtype = np.int16) # 將聲音文件數據轉換為數組矩陣形式
  wave_data.shape = -1, channel # 按照聲道數將數組整形，單聲道時候是一列數組，雙聲道時候是兩列的矩陣
  wave_data = wave_data.T # 將矩陣轉置
  wave_data = wave_data
  return wave_data, frame, framerate

if(__name__=='__main__'):
  wave_data, frame, framerate = read_wav_data("godwave.wav")

  string = ''
  norm = 0
  for i in range(frame):
    norm = norm+abs(wave_data[0][i])
    if (i+1) % 64 == 0:
      if norm > 100000:
          string += '1'
      else:
          string += '0'
      norm = 0
  with open('output.txt','w') as output:
    output.writelines(string)