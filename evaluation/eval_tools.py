class EvaluationTools:
    def __init__(self):
        pass

    def calculate_accuracy(self, true_labels, predicted_labels):
        correct_predictions = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == pred)
        return correct_predictions / len(true_labels) if len(true_labels) > 0 else 0

    def calculate_precision(self, true_labels, predicted_labels):
        true_positives = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == 1 and pred == 1)
        predicted_positives = sum(1 for pred in predicted_labels if pred == 1)
        return true_positives / predicted_positives if predicted_positives > 0 else 0

    def calculate_recall(self, true_labels, predicted_labels):
        true_positives = sum(1 for true, pred in zip(true_labels, predicted_labels) if true == 1 and pred == 1)
        actual_positives = sum(1 for true in true_labels if true == 1)
        return true_positives / actual_positives if actual_positives > 0 else 0

    def log_metrics(self, metrics):
        for metric, value in metrics.items():
            print(f"{metric}: {value}")

    def evaluate(self, true_labels, predicted_labels):
        metrics = {
            "accuracy": self.calculate_accuracy(true_labels, predicted_labels),
            "precision": self.calculate_precision(true_labels, predicted_labels),
            "recall": self.calculate_recall(true_labels, predicted_labels),
        }
        self.log_metrics(metrics)
        return metrics