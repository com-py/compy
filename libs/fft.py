# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program 5.1 (DOC): Fast Fourier transform (fft.py)
# J Wang, Computational modeling and visualization with Python
#

import math as ma, numpy as np  # needed for constants $e, \pi$
    
def fft_rec(f, L):              # recursive FFT of 2**L pts, f unchanged
    if (L==0): return f         # length 1, $g_0=f_0$
    
    g0 = fft_rec(f[::2], L-1)           # even part $[0,2,4,...]$ 
    g1 = fft_rec(f[1::2], L-1)          # odd part  $[1,3,5,...]$ 

    N = 2**L
    g, M = [0.0]*N, N//2
    for m in range(M):                  # assemble two halves
        w = ma.e**(-2j*ma.pi*m/N)
        g[m]   = g0[m] + w * g1[m]      # 1st half  
        g[m+M] = g0[m] - w * g1[m]      # 2nd half  
    return g

def ifft_rec(f, L):             # inverse FFT
    g = np.conjugate(f)
    return np.conjugate(fft_rec(g, L))/2**L

def fft(f, L):          # return FFT of 2**L data points, f changed
    divs = 1            # number of divisions, initially = 1
    pairs = 2**(L-1)    # number of pairs per division, initially=N/2
    stride = divs       # period, distance between pair-wise elements
    bit_reverse_array(f, L)         # bit reverse array
    for level in range(L):          # iterate ln(N) levels
        gap = 2*divs                # distance to next pair
        w = 1.0                     # exp(-i m pi/divs), initial = 1
        x = ma.e**(-1j*ma.pi/divs)  # cumulative exp factor
        for m in range(divs):       # run over each division
            # combine butterflies, start with 1st item in each division
            for i in range(m, pairs*gap, gap):
                tmp = w * f[i + stride]
                f[i + stride] = f[i] - tmp
                f[i] = f[i] + tmp
            w = w*x                 # update w
        divs = divs*2               # subdivide the problem
        pairs = pairs//2
        stride = divs
    return f
# end fft()

# return the bit-reversed integer n in a bit field of 'width'
def bit_reverse(n, width):
    bits = list(bin(n))         # convert to bits, e.g., 2 --> '0b10'
    bits.reverse()              #     in-place reverse bits to '01b0'
    bits=''.join(bits[:-2])     # back to string & discard last 'b0' chars
    pad = width - len(bits)
    if (pad>0):                 # pad trailing '0', e.g., '10' to '1000'
        bits = bits + '0'*pad
    return int(bits,2)          # binary to decimal

# bit reverse an array, mostly for array size of 2**integer power
def bit_reverse_array(a, width):
    for i in range(len(a)):
        j = bit_reverse(i, width)
        if (i < j):             # swap only once
            a[i], a[j] = a[j], a[i]
