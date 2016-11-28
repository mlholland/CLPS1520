vl_setupnn
%websave('alexnet.mat','http://www.vlfeat.org/matconvnet/models/beta16/imagenet-caffe-alex.mat');
net = load('alexnet.mat');
net = vl_simplenn_tidy(net);
net = vl_simplenn_move(net, 'gpu');