function [ ] = classify_inputs( input_dir, output_fname )
    %given a directory, an extension type, and a output filename, open
    %all files with the given extension in the input directory, classify
    %them using alexnet, and print the results to text in the output
    %filename. Results are a csv of "image filename, classification".
    %input_dir: path to directory of images.  Must end with a forward slash
    %extension: examples '.jpg' or '.png'
    %output_fname: filename of output file.
    %example use: classify_inputs('../misc/', '.jpg', 'out.csv')
    %NOTE: alexnet.mat is tooo big for github, make sure there's a copy in this directory.
    working = 'yes' 
    net = vl_simplenn_tidy(load('alexnet.mat'));
    labels = net.meta.classes.description;
    files = dir(strcat(input_dir,'*g'));
    num_images = numel(files)
    output_str = '';
    counter = 0;
    for file = files'
	if mod(counter, 100) == 0
	    counter
	end
	counter = counter + 1;
        image = single(resize227(imread(strcat(input_dir, file.name))));
        image_norm = bsxfun(@minus, image, net.meta.normalization.averageImage);
        net_input = gpuArray(image_norm);
	%previous line can gpuwrap if we can ge batch scripts to include gpus
	net_output = vl_simplenn(net, image_norm);
        cl = gather(net_output(end).x);
        [score, label] = max(cl);
	output_str = sprintf('%s%s,"%s","%s"\n',output_str, file.name, char(labels(label)), mat2str(squeeze(cl)));
    end
	out_file = fopen(output_fname,'a');
	fprintf(out_file, '%s', output_str);
	fclose(out_file);
	
end
