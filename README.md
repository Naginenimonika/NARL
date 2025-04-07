# NARL
**ABSTRACT**


Noise Removal and Peak Picking of Advanced Indian MST Radar Wind Velocity Data Using Neural Networks.The Advanced Indian MST (Mesosphere, Stratosphere and Troposphere) Radar situated at National Atmospheric Research Laboratory (NARL), Gadanki is a fully active phased array radar built to study the atmosphere and near-Earth space. It operates in the VHF band at 53MHz using a 32x32 antenna array, each radiating a power of 1kW. The radar data can be used to generate wind velocity-range plots which is useful for atmospheric studies. The data, however, gets contaminated with noise at higher altitudes due to various factors. This project aims to study the characteristics of such noise and eliminate it to produce denoised data using Neural Networks. Subsequently, peak picking is done and clean plots are generated.


**PROPOSED SYSTEM**

The proposed system introduces a Neural Network-based approach for noise removal and peak picking in MST Radar wind velocity data, significantly improving accuracy and reliability. Unlike traditional filtering techniques, which often fail to adapt to varying atmospheric conditions, the neural network model is designed to learn and distinguish noise patterns, ensuring better preservation of essential wind velocity signals.

The system consists of three key phases: data preprocessing, noise removal, and peak detection. In the preprocessing phase, raw radar data undergoes normalization, outlier removal, and missing data handling to improve data quality. The noise removal phase employs a deep learning model (Autoencoder/CNN/RNN) that is trained to differentiate between actual wind velocity signals and unwanted noise. Finally, peak picking is performed using an AI-enhanced thresholding technique, ensuring accurate identification of wind velocity peaks. 


**PROCESS**

The raw wind velocity data collected from the MST Radar is preprocessed, normalized and given for RNN processing.

![image](https://github.com/user-attachments/assets/5478393a-dfd6-4140-a505-987640de0d4d)

![image](https://github.com/user-attachments/assets/2e0f9a15-1aa3-47f0-ac21-7a0894f7de87)

The signals are generated from the data.

![image](https://github.com/user-attachments/assets/24612853-baf1-42ce-8d06-f3668977ab3b)

The noise in the signals is detected and are represented as red dots. The lower altitudes are having correct data whereas the higher altitudes are having the noise.

![image](https://github.com/user-attachments/assets/c6247c5d-1e40-4a55-94e7-70b495eccb6a)

Long Short Term Memory (LSTM) , a Recurrent Neural Network model,which is suitable for handling sequential data, is loaded and trained through which the noisy data is passed. Here 'Softmax' is used as activation function as it is best suitable for multi-class classification problems which outputs a probability distribution over the 'limit_width' classes, where each value represents the probability of the input belonging to that class. And 'categorical_crossentropy' is used as loss function which measures the difference between the predicted probability distribution and the true distribution.


![image](https://github.com/user-attachments/assets/2924436c-647a-4a90-bdb0-54cc3f7bf5ee)

![image](https://github.com/user-attachments/assets/968d1c08-7812-4ff4-bbba-d888cd75a17a)

![image](https://github.com/user-attachments/assets/cc7e873b-d4c3-4518-813d-21c6871783e1)


The visualization shows noise reduction in radar wind velocity data, where the LSTM model effectively isolates the true signal (blue) from noisy components (green and red). This confirms the model's ability to filter out noise and enhance data clarity for accurate wind velocity estimation.


![image](https://github.com/user-attachments/assets/28089757-d742-4e44-a864-d02709d1bf5e)




