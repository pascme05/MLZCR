# Authors: Pascal Schirmer & Iosif Mporas University of Hertfordshire, UK
# Cite: "Energy Disaggregation from Low
# Sampling Frequency Measurements Using Multi-Layer Zero Crossing Rate", IEEE ICASSP 2020

# x: input signal (frame)
# xmin: minimum amplitude of x (optional)
# xmax: maximum amplitude of x (optional)
# nlayers: number of selected layers
# zc: output Zero Crossings per layer
# zcr: output Zero Crossing Rate per layer

import numpy as np


def mlzcr(x, nlayers, xmax=None, xmin=None):
    if xmin is None:
        xmin = np.min(x)
    x = x - xmin

    if xmax is None:
        xmax = np.max(x)

    step = xmax / (nlayers - 1)
    zc = np.zeros((nlayers, 1))

    for i in range(0, nlayers):
        xdc = x - i * step
        zc[i] = np.sum(np.diff(np.sign(xdc)) != 0, axis=0)
        if i == 0 or i == (nlayers - 1):
            zc[i] = zc[i] / 2

    zcr = zc / len(x)

    return [zc, zcr]
