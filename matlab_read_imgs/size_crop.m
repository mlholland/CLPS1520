function crop = size_crop(img,s)
    x = size(img,1);
    y = size(img,2);
    dx = round((x - s)/2);
    dy = round((y - s)/2);
    crop = img(dx:x-dx,dy:y-dy,:); 
end