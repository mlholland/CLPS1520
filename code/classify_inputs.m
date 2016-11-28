function [ x ] = test( input_fname , result_fname )
	x = 'hello';
	net = vl_simplenn_tidy(load('alexnet.mat'));
	in = single(resize227(imread(input_fname)));
	in_norm = bsxfun(@minus, in, net.meta.normalization.averageImage);
	output = vl_simplenn(net, in_norm);
	cl = gather(output(end).x);
	[score, label] = max(cl);
	labels = net.meta.classes.description;
	fileID = fopen(result_fname,'w');
	result = char(labels(label));
	fprintf(fileID, '%s, %s\n', input_fname, result);
	fclose(fileID);
	
end
