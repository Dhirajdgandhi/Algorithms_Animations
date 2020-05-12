load('data2.mat')
Max_iters = 10; %% set up the maximum iterations
Init_centroid = [3 3, 6 2, 8 5]; %%step 1
figure('visible','on'); hold on;
Plot_progress(X, init-centroid, init-centroid, idx, K, 1);%%plot the illustration
[~,~] = kmeans(X, init-centroid, Max-iters, true)%% step two and 3