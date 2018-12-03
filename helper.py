# Arora, Priyank
# 1001-55-3349
# 2018-11-26
# Assignment-05-02

import sklearn.datasets
from sklearn.cluster import AgglomerativeClustering
import numpy as np

def generate_data(dataset_name, n_samples, n_classes):
    if dataset_name == 'swiss_roll':
        data = sklearn.datasets.make_swiss_roll(n_samples, noise=0.15, random_state=99)[0]
        data = data[:, [0, 2]]/10.0
    if dataset_name == 'moons':
        data = sklearn.datasets.make_moons(n_samples=n_samples, noise=0.15)[0]
    if dataset_name == 'blobs':
        data = sklearn.datasets.make_blobs(n_samples=n_samples, centers=n_classes*2, n_features=2, cluster_std=0.85*np.sqrt(n_classes), random_state=100)
        return data[0]/10., [i % n_classes for i in data[1]]
    if dataset_name == 's_curve':
        data = sklearn.datasets.make_s_curve(n_samples=n_samples, noise=0.15, random_state=100)[0]
        data = data[:, [0,2]]/1.1

    ward = AgglomerativeClustering(n_clusters=n_classes*2, linkage='ward').fit(data)
    return data[:]+np.random.randn(*data.shape)*0.03, [i % n_classes for i in ward.labels_]


