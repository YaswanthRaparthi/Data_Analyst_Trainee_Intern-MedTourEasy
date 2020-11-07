from sklearn import datasets
import matplotlib
from matplotlib import pyplot as plt
import numpy as np


np.random.seed(0)
feature_set, labels = datasets.make_moons(100, noise=0.1)
plt.figure(figsize=(10,7))
plt.scatter(feature_set[:,0], feature_set[:,1], c= labels, cmap=plt.cm.winter)

labels = labels.reshape(100,1)
##plt.show()

def sigmoid(x):
    return 1/(1+np.exp(x))
def sigmoid_der(x):
    return sigmoid(x) *(1-sigmoid(x))
    
wh = np.random.rand(len(feature_set[0]),4)
wo = np.random.rand(4,1)

lr = 0.5

for rpoch in range(20000):
    #Feedforword Propagation
    zh=np.dot(feature_set,wh)
    ah= sigmoid(zh)

    zo= np.dot(ah,wo)
    
    ao = sigmoid(zo)

    #Phase 1
    error_out = ((1/2) * (np.power((ao - labels),2)))
    print(error_out.sum())
    dcost_dao = ao - labels
    
    dao_dzo = sigmoid_der(zo)
    dzo_dwo = ah

    dcost_wo =np.dot(dzo_dwo.T, dcost_dao * dao_dzo)

    #Phase 2
    dcost_dzo = dcost_dao * dao_dzo

    dzo_dah = wo
    dcost_dah = np.dot(dcost_dzo, dzo_dah.T)

    dah_dzh = sigmoid_der(zh)
    dzh_dwh = feature_set
    dcost_wh = np.dot(dzh_dwh.T, dah_dzh * dcost_dah)

    #Updated Weights
    wh -= lr *dcost_wh
    wo -= lr *dcost_wo




