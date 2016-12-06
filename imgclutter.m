function [ final_clutter ] = imgclutter( rgbImage )

% STEP 1: Convert image to CIELab color space

colorTransform = makecform('srgb2lab');

lab = applycform(rgbImage, colorTransform);

final_clutter = 0;

% STEP 2: Examine the image at three pyramid levels.
% Go up the pyramid at the end of the loop.
for zoom = 0:1:2
    
    % STEP 3: Get the two measures of clutter.
    contrast_clutter = luminancecontrast(lab);
    
    [Y,X,Z] = size(lab);
    lab1 = double(reshape(lab, [Y*X, Z]));
    covariance = cov(lab1);
    e = eig(covariance);
    
    color_clutter = 4/3 * pi * prod(e);

    clutter_avg = (contrast_clutter + nthroot(color_clutter, 3))/2;
    
    if final_clutter < clutter_avg
        final_clutter = clutter_avg;
    end
    
    lab = impyramid(lab, 'reduce');
    
end

end

