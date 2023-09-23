from tensorflow import keras
from keras import layers, Sequential

model = Sequential([
    layers.LSTM(512, activation='sigmoid', return_sequences=True),
    layers.Dropout(0.2),
    layers.LSTM(128, activation='sigmoid', return_sequences=True),
    layers.LSTM(64),
    layers.Dropout(0.2),
    layers.Dense(3, activation='sigmoid')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

