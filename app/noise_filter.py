import numpy as np
import scipy.signal

def reduce_noise(audio_signal, noise_estimation_method='spectral_subtraction', noise_reduction_factor=1.0):
    if noise_estimation_method == 'spectral_subtraction':
        return spectral_subtraction(audio_signal, noise_reduction_factor)
    else:
        raise ValueError("Unsupported noise estimation method: {}".format(noise_estimation_method))

def spectral_subtraction(audio_signal, noise_reduction_factor):
    # Estimate the noise power spectrum
    noise_power = np.mean(np.abs(audio_signal)**2)
    
    # Perform FFT
    freq_signal = np.fft.fft(audio_signal)
    
    # Subtract noise power
    freq_signal = freq_signal - noise_reduction_factor * np.sqrt(noise_power)
    
    # Ensure no negative values
    freq_signal = np.maximum(freq_signal, 0)
    
    # Perform inverse FFT
    filtered_signal = np.fft.ifft(freq_signal)
    
    return np.real(filtered_signal)