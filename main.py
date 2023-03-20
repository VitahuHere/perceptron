import csv
import random


def parse_data(path: str) -> list:
    data = csv.reader(open(path), delimiter=",")
    return [
        [float(a) if a.replace(".", "").isdigit() else a for a in row] for row in data
    ]


def modify_weight_vector(
    weight_vector: list[float],
    alpha: float,
    d: float,
    y: float,
    input_vector: list[float],
) -> list:
    multiplier = alpha * (d - y)
    new_input = [a * multiplier for a in input_vector]
    return [x + y for x, y in zip(weight_vector, new_input)]


def modify_theta(old_theta: float, alpha: float, d: float, y: float) -> float:
    return old_theta - alpha * (d - y)


def perceptron(
    weight_vector: list[float],
    theta: float,
    input_vector: list[float],
) -> float:
    return (
        1 if sum([x * y for x, y in zip(weight_vector, input_vector)]) >= theta else 0
    )


def train_perceptron(
    weight_vector: list[float],
    theta: float,
    alpha: float,
    data: list[list],
    value_map: dict[str, int],
) -> tuple[list[float], float]:
    for row in data:
        d = value_map[row[-1]]
        y = perceptron(weight_vector, theta, row[:-1])
        weight_vector = modify_weight_vector(weight_vector, alpha, d, y, row[:-1])
        theta = modify_theta(theta, alpha, d, y)
    return weight_vector, theta


def static():
    alpha = 0.01
    theta = 3

    data = parse_data("perceptron.data")
    test_data = parse_data("perceptron.test.data")

    value_map = {
        value: index
        for index, value in enumerate(sorted(set([row[-1] for row in data])))
    }

    weights = [random.random() for _ in range(len(data[0]) - 1)]

    for i in range(1, 101):
        weight_vector = weights.copy()
        for _ in range(i):
            weight_vector, theta = train_perceptron(
                weight_vector, theta, alpha, data, value_map
            )

        correct = 0
        for row in test_data:
            result = perceptron(weight_vector, theta, row[:-1])
            if result == value_map[row[-1]]:
                correct += 1
        print(f"Accuracy for {i} epochs: {correct / len(test_data) * 100}%")


def with_input():
    train_data = parse_data(input("Train data path: "))
    alpha = float(input("Alpha: "))
    vector = [float(a) for a in input("Input vector: ").split(",")]
    weights = [random.random() for _ in range(len(train_data[0]) - 1)]
    epochs = int(input("Epochs: "))
    value_map = {
        value: index
        for index, value in enumerate(sorted(set([row[-1] for row in train_data])))
    }
    theta = 3
    for _ in range(epochs):
        weights, theta = train_perceptron(weights, theta, alpha, train_data, value_map)

    print(list(value_map.keys())[list(value_map.values()).index(perceptron(weights, theta, vector))])


def main():
    print("Pick a function to run:")
    print("1. Static")
    print("2. With input")
    choice = input("Choice: ")
    match choice:
        case "1":
            static()
        case "2":
            with_input()


if __name__ == "__main__":
    main()
