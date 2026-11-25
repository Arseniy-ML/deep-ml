import numpy as np
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    # Implement your code here
    predicted = np.array(predicted)
    actual = np.array(actual)

    tp = np.sum((actual == 1) & (predicted == 1))
    tn = np.sum((actual == 0) & (predicted == 0))
    fp = np.sum((actual == 0) & (predicted == 1))
    fn = np.sum((actual == 1) & (predicted == 0))

    confusion_matrix = [[tp, fn], [fp, tn]]
    precision = float(tp / (tp + fp))
    accuracy = float((tp + tn) / (tp + tn + fp + fn))
    recall = float(tp / (tp + fn))
    negativePredictive = float(tn / (tn + fn))
    specificity = float(tn / (tn + fp))
    f1 = float((2 * precision * recall) / (precision + recall))

    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
