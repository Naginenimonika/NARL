import numpy as np
def read_mst_radar_data(file_path):
    with open(file_path, 'rb') as fid:
        header = np.fromfile(fid, dtype=np.int16, count=64)
        nrgb = header[2] 
        nfft = header[3]  
        d_size = np.int32(nrgb) * np.int32(nfft)  
        fid.seek(0, 0)
        frame_count = 0
        w=[]
        y=[]
        while True:
            x= np.fromfile(fid, dtype=np.int16, count=64)
            x= np.fromfile(fid, dtype=np.int32, count=2 * d_size)
            frame_count += 1
            if x.size < 128:
                break 
            iq_matrix = x.reshape((nrgb, nfft, 2))  
            i_data = iq_matrix[:, :, 0]  
            q_data = iq_matrix[:, :, 1]  
            w.append(i_data)
            y.append(q_data)
            print(f"Frame {frame_count}:")
            print(f"I Component : {i_data.flatten()}")
            print(f"Q Component : {q_data.flatten()}")
            print("-" * 40)
        w=np.array(w)
        y=np.array(y)
        print(w)
        print(y)
file_path = "C:\\Users\\monik\\OneDrive\\Desktop\\6JU2024SHT1.r1"
read_mst_radar_data(file_path)