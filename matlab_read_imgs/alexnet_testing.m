dir = 'alexnet_testing/wallet';
[image_list,alex_list] = read_images(dir,net);

for i = 1:numel(alex_list)
    fprintf('Image num: %d \n',i);
    classify_image(alex_list{i},net,5);
end