# Multi-Layer Zero Crossing Rate (MLZCR)
This code implements a more general version of the MLZCR as proposed in [1] for energy disaggregation. In detail, arbitrary frames of signals are processed using multiple layers
for possible zero crossings between a minimum and maximum value. The paper can be found on [IEEE Xplore](https://ieeexplore.ieee.org/document/9054637) and [here](https://www.pascalschirmer.com/)

# Code
The code for the MLZCR is provided for Matlab and python implementation.

1) Inputs  
x:        frame of a signal with arbitrary length  
nlayers:  number of zero crossing layers  
xmin:     static minimum value of the signal (optional)  
xmax:     static maximum value of the signal (optional)  

2) Output  
zc:       number of zero crossings for each layer (dim: nlayers x 1)  
zcr:      zero crossing rate (dim: nlayers x 1)  

# References
[1] P. A. Schirmer and I. Mporas, “ENERGY DISAGGREGATION FROM LOW SAMPLING FREQUENCY MEASUREMENTS USING MULTI-LAYER ZERO CROSSING RATE,” 
in 2020 45th IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Barcelona, Spain, 2020.
