function centroids = computeCentoids(X, idx,K)
	[~, n] = size(X);
	centroids = zeros(K,n);
	%%go over every centroid and compute mean of all points that belongs to it, concretely, 			//the row vector centroids(i,:) should be contain the mean of the data points assigned to 	//centroid i
	for i = 1:K
		centroids(i,:)=sum(X(idx==i,:))./sum(idx==i);
	end
end