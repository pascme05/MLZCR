function [zc, zcr] = mlzcr(x, nlayers, xmin, xmax)
% Authors: Pascal A. Schirmer & Iosif Mporas
% University of Hertfordshire, UK
% Cite: "Energy Disaggregation from Low Sampling Frequency Measurements Using Multi-Layer Zero Crossing Rate", IEEE ICASSP 2020

% x: input signal (frame)
% xmin: minimum amplitude of x (optional)
% xmax: maximum amplitude of x (optional)
% nlayers: number of selected layers
% zc: output Zero Crossings per layer
% zcr: output Zero Crossing Rate per layer

if nargin < 3
    xmin = min(x);
end
x = x - xmin;

if nargin < 4
    xmax = max(x);
end

step = xmax / ( nlayers - 1 );
zc = zeros(nlayers,1);

for i = 1 : nlayers
    xdc = x - (i-1)*step;
    zc(i) = length(find(diff(sign(xdc))));
    if i == 1 || i == nlayers
        zc(i) = zc(i)/2;
    end
end

zcr = zc/length(x);