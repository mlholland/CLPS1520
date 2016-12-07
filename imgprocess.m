




% First, we have to make a dict of all the filenames.

base_path = 'dataset/backgrounds/images/all/';

[status, output] = system(['dir ' base_path '*.jpg']);
list = strsplit(output);

% We should have it in <list>.

L = size(list, 2);

%clutters = zeros(L);

out_file = fopen('backgroundclutters.csv','w');

for i = 1:(L-1)
    
    file = list{i};
    
    img = imread(file);
    
    clutter = imgclutter(img);
    
    %filenames = [filenames;file];
    
    fprintf(out_file,'%s,"%d"\n', file, clutter);
    
end



%disp(clutters);

%csvwrite('backgroundclutters.csv', filenames, 1,1);
%csvwrite('backgroundclutters.csv', clutters, 1,1);









