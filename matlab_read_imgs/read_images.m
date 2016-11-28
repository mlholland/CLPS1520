function [image_list,alex_list] = read_images(path,net)
    %Loads a whole directory of images into a cell array of matrices
    images = dir(path);
    num = 1;
    image_list = {};
    %accepted file types:
    types = {'peg','jpg','png','PEG','JPG','PNG'};
    
    for i = images'
        name = i.name;
        if length(name)>3 && any(ismember(types,name(length(name)-2:length(name))))
            alex_list{num} = gpuArray(imread_alexnet([path '/' name],net));
            image_list{num} = uint8(imread([path '/' name]));
            num = num + 1;
        end
    end
end