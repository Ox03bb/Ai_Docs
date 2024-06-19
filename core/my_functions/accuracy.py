import numpy as np

def BC_acuracy(y_true, y_pred,trechold=0.5):
    
    y_pred = y_pred.flatten()
    y_true = y_true.flatten()
    

    for i in range(len(y_pred)):
        if y_pred[i] >= trechold:
            y_pred[i] = 1
        else:
            y_pred[i] = 0

    accuracy = np.sum(y_pred == y_true) * 100 / len(y_true)
    print(accuracy)