function  Plot_progress(X, centroids, previous, idx, k)
	%%plot the data
	palette = hsv(k+1);%% create pallete
	colors = palette(idx,:);
	scatter(X(:,1),X(:,2),15,colors);%% plot
	
	%%plot centroid
	plot(centroids(:,1), centroids(:,2), 'x', 'MarkerEdgeColor','k','MarkerSize','10', 	'LineWidth','3')
	
	%%draw the history of the centroid
	for j = 1:size(centroids,1)
		drawLine(centroids(j,:), previous(j,:));
	end
end