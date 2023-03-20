import csv


def parse_data(path: str) -> list:
    with open(path, encoding="utf-8") as f:
        data = csv.reader(f, delimeter=",")
        print(data)


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


def main():
    alpha = 0.5
    theta = 3

    w = [2, -1, 4, 1]
    x = [7, -2, -5, 4]
    d = 1
    y = 0

    # print(modify_theta(theta, alpha, d, y))
    # print(modify_weight_vector(w, alpha, d, y, x))
    print(parse_data("perceptron.data"))


if __name__ == "__main__":
    main()
