import math


def single_neuron_model(
    features: list[list[float]],
    labels: list[int],
    weights: list[float],
    bias: float,
) -> (list[float], float):
  probabilities = []
  squared_errors = []

  for feature_vector, label in zip(features, labels):

    z = sum(x * w for x, w in zip(feature_vector, weights)) + bias

    prob = 1 / (1 + math.exp(-z))
    probabilities.append(round(prob, 4))

    error = (prob - label) ** 2
    squared_errors.append(error)

  mse = round(sum(squared_errors) / len(labels), 4)

  return probabilities, mse
