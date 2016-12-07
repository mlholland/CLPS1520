function [ contrast ] = luminancecontrast( img )
%LUMINANCECONTRAST Summary of this function goes here
%   Detailed explanation goes here

L = img(:,:,1);
%{
kernel1 = fspecial('gaussian', 5);
kernel2 = fspecial('gaussian', 3);

kernel2 = [zeros(2,3) kernel2 zeros(2,3)];
kernel2 = [zeros(5,2); kernel2; zeros(5,2)];

kernel = kernel1 - kernel2;
%}
Lc = imgaussfilt(L,3) - imgaussfilt(L,5);

Lc = abs(Lc);

% Global maximum was casting complexity to 128 on large images - pixel
% maximum.  Instead, try averaging.
%contrast = max(max(Lc));

contrast = mean2(Lc);

%contrast = sum(Lc .^ 2);

end

