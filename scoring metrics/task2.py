import numpy as np

from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix



def classification_metrics(ground_truth, prediction):

    assert len(ground_truth) == len(prediction)

    # Calculate accuracy
    accuracy = accuracy_score(ground_truth, prediction)

    # Calculate AUC
    auc = roc_auc_score(ground_truth, prediction)

    # Calculate confusion matrix
    tn, fp, fn, tp = confusion_matrix(ground_truth, prediction).ravel()

    # Calculate sensitivity (true positive rate)
    sensitivity = tp / (tp + fn)

    # Calculate specificity (true negative rate)
    specificity = tn / (tn + fp)

    # Calculate F1 score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)



    return accuracy,auc,sensitivity,specificity,f1_score



