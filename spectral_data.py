import time
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

start = time.time()
directory = ''
filename = '4JU2024SHT1.d9'
file_path = os.path.join(directory,filename)
file = open(file_path,'rb')

def read_radar_data(file_path):
    with open(file_path,'rb') as f:
        radar_data = f.read()
    return radar_data

header_size = 128
def read_first_128_bytes(file_path):
    with open(file_path, 'rb') as file:
        first_128 = file.read(128)
    return first_128

A = np.fromfile(filename, dtype=np.int16, count=64)
print(A)

Radar_type = 0  #1
baudlength = 0  #2
nrgb = 0        #3
nfft = 0        #4
nci = 0        #5
nici = 0       #6
ipp = 0         #7
pwd = 0         #8
cflg = 0        #9
nwin = 0        #10
w1start = 0     #11
w1len = 0       #12
w2start = 0     #13
w2len = 0       #14
year = 0        #15
month = 0       #16
day = 0         #17
hour = 0        #18
Min = 0         #19
sec = 0         #20
nbeams = 0      #21
beam = 0        #22
scancycle = 0   #23
attn = 0        #24
w3start = 0     #25
w3len = 0       #26
simrange1 = 0   #27
txpower = 0     #28
winfn = 0       #29
noofpulses = 0  #30
dtype = 0       #31
Pulsedelay9 = 0 #32

variables = [
    "Radar_type", "baudlength", "nrgb", "nfft", "nci", "nici", "ipp", "pwd",
    "cflg", "nwin", "w1start", "w1len", "w2start", "w2len", "year", "month",
    "day", "hour", "Min", "sec", "nbeams", "beam", "scancycle", "attn", "w3start",
    "w3len", "simrange1", "txpower", "winfn", "noofpulses", "dtype", "Pulsedelay9"
]

for i in range(len(variables)):
    globals()[variables[i]] = A[i]

fs = 10**6 / (np.float64(ipp) * np.float64(nci))
frequency = np.linspace(-fs / 2, fs / 2, nfft)

datasize = np.uint32(nrgb) * np.uint32(nfft)
print(f'datasize: {datasize}')
Resolution_of_height = 1.5*100*baudlength
framecount = 0
file.seek(0,0)
print('78')
while True:
    x = np.fromfile(file, dtype=np.int16, count=64)
    x = np.fromfile(file, dtype=np.int32, count=datasize)
    framecount += 1
    if x.size < 128:
       break
    
nscan = framecount // (nbeams*nici)
print(f'Number of Frames: {framecount}')
print(f'Number of scans: {nscan}')

frameskip = 20
file.seek((128+4*datasize)*frameskip+128,0)

index = 0
spectra = np.zeros((nrgb, nfft), dtype=np.float64)

# for rgb in range(65,75):
#     plt.figure()
#     plt.plot(B[rgb, :])
#     plt.show()

for rgb in range(nrgb):
    for ft in range(nfft):
        spectra[rgb, ft] = np.fromfile(file=file, dtype=np.int32, count=1)
    m = np.mean(spectra[rgb, :])
    spectra[rgb, :] -= m

spectra = np.fft.fftshift(spectra, axes=1)
#print(I_Data_raw)
# I_Data[:,0] = 0 
# Q_Data[:,0] = 0
# avg_I = np.sum(I_Data, axis=1) / nfft
# avg_Q = np.sum(Q_Data, axis=1) / nfft
# I_Data = I_Data - avg_I.reshape(-1, 1)
# Q_Data = Q_Data - avg_Q.reshape(-1, 1)

plt.figure(figsize=(10, 6))
plt.gca().set_facecolor('#000000')
offset = 50000000
for rgb in range(nrgb):
    plt.plot(frequency, np.abs(spectra[rgb]) + offset * rgb, color='green')
    peak = np.argmax(spectra[rgb, :])
    plt.scatter(frequency[peak], spectra[rgb, peak] + offset * rgb, color='red')
plt.show()