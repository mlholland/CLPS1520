function image = imread_alexnet(file,net)
    image = imread(file);
    pad = [0 0];
    pad(1) = round((size(image,2)-size(image,1))/2);
    pad(2) = round((size(image,1)-size(image,2))/2);
    pad(pad<0)=0;
    image = padarray(image,[pad(1) pad(2)],'symmetric');
    image = imresize(image,[227 227]);
    image = single(image);
    image = bsxfun(@minus,image,net.meta.normalization.averageImage);
end