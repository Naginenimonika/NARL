import numpy as np
import matplotlib.pyplot as plt

def read_mst_radar_data(file_path):
    with open(file_path, 'rb') as fid:
        header = np.fromfile(fid, dtype=np.int16, count=64)
        nrgb = header[2] 
        nfft = header[3]  
        d_size = np.int32(nrgb) * np.int32(nfft)  
        fid.seek(0, 0)
        frame_count = 0
        w = []
        y = []
        
        while True:
            x = np.fromfile(fid, dtype=np.int16, count=64)
            x = np.fromfile(fid, dtype=np.int32, count=2 * d_size)
            
            if x.size < 128:
                break 
            
            frame_count += 1
            iq_matrix = x.reshape((nrgb, nfft, 2))  
            i_data = iq_matrix[:, :, 0]  
            q_data = iq_matrix[:, :, 1]  
            w.append(i_data)
            y.append(q_data)
            
        w = np.array(w)
        y = np.array(y)
        
        return w, y

def plot_signals(w, y, nrgb):
    plt.figure(figsize=(10, 6))
    color='green'
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(w+1j*y)))
    max_amplitude=np.max(spectrum)
    offset=max_amplitude*0.5
    for i in range(nrgb):
        plt.plot(spectrum[0,i, :]+i*offset,color=color, label=f'spectrum {i+1}')
    plt.xlabel('Time Index')
    plt.ylabel('Amplitude')
    plt.title('Radar Signal (I and Q Components)')
    ax=plt.gca()
    ax.set_facecolor("black")
    plt.show()
file_path = "C:\\Users\\monik\\OneDrive\\Desktop\\6JU2024SHT1.r1"
w, y = read_mst_radar_data(file_path)
plot_signals(w, y, w.shape[1])