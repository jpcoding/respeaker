
#!/usr/bin/env python3
# genegare white noise
from scipy.io import wavfile
import numpy as np

def band_limited_noise(min_freq, max_freq, samples=1024, samplerate=1):
    freqs = np.abs(np.fft.fftfreq(samples, 1/samplerate))
    f = np.zeros(samples)
    idx = np.where(np.logical_and(freqs>=min_freq, freqs<=max_freq))[0]
    f[idx] = 1
    return fftnoise(f)

x = band_limited_noise(20, 20000, 44100, 44100)
x = np.int16(x * (2**15 - 1))
wavfile.write("./media/test.wav", 44100, x)