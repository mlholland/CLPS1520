function [ output_image ] = resize227( input_image )
%Helper function to pad and resize images to fit the net.
    im = input_image;
    s = size(im);
    if s(1) > s(2)
        im = padarray(im, [0, ceil((s(1) - s(2)) / 2)], 'symmetric');
    end
    if s(2) > s(1)
        im = padarray(im, [ceil((s(2) - s(1)) / 2), 0], 'symmetric');
    end
    s = imresize(im, [227 227]);
    output_image = s;
end

