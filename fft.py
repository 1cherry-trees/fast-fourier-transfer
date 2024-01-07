import numpy as np
def fft(x):
    n = len(x)

    # Base case: if the length of the input sequence is 1, return the DFT of the sequence
    if n == 1:
        return x

    # Divide the input sequence into even and odd parts
    even = x[0::2]
    odd = x[1::2]

    # Compute the DFT of the even and odd parts using the FFT algorithm recursively
    even_dft = fft(even)
    odd_dft = fft(odd)

    # Combine the results to obtain the final DFT
    dft = [0] * n
    for k in range(n // 2):
        t = np.exp(-2j * np.pi * k / n) * odd_dft[k]
        dft[k] = even_dft[k] + t
        dft[k + n // 2] = even_dft[k] - t

    return dft


x = [1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j]

# Compute the DFT of the sequence using the fft function
dft = fft(x)

# Print the DFT of the sequence
print(dft)
