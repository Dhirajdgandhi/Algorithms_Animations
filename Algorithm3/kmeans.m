function [centriods, idx] = kmeans(X, init_centroid, Max_iters, plot_progress)
	%% Set default value for plot progress
	If ~exist(?plot_progress?,?var?) || is empty(plot_progress)
		plot_progress = false;
	end

	%%plot the data if we are plotting progress
	if plot_progress
		figure;
		hold on;
	end
	%%initialize values
	[m n] = size(X);
	K = size(initcentroid,1);
	centroids = init-centroid, 1)
	previous_centroid = centroids;
	idx = zeros(m,1);

	%%run k-means
	for I = 1:max-iters
		%%out put progress
		fprint('K-Means iteration %d/%d?\n', i, max-iters);
		%% for each ampler of X, assign it to the closest centroid;
		idx = findClosetCentroids(X, centroids);
		%% optionally, plot progress here
		if plot_progress
			plotProgressKmeans(X, centroids, previous_centroids,idx,K,i);
			previous_centroids = centroids;
			fprintf('Press enter to continue')%%easy for illustration
			pause;
		end
		%%given the membership, compute new centroids
		centroids = computeCentroids(X, idx, K);
	end
end