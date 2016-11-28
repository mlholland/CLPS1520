function [score,label] = classify_image(input,net,classes)
    output = vl_simplenn(net,input);
    classificationLayer = gather(output(end).x);
    labels = net.meta.classes.description;
    for i = (1:classes);
        [bestScore, bestLabel] = max(classificationLayer);
        if i == 1
            score = bestScore;
            label = bestLabel;
            
        end
        classificationLayer(bestLabel) = 0;
        fprintf('Category %d: %.20s (%d), score %.3f \n',i,labels{bestLabel},bestLabel,bestScore);
    end
end