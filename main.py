def modify_weight_vector(
    weight_vector: list[float],
    alpha: float,
    d: float,
    y: float,
    input_vector: list[float],
) -> list:
    multiplier = alpha * (d - y)
    v_prim = [a * multiplier for a in input_vector]
    return [x + y for x, y in zip(weight_vector, v_prim)]


def main():
    alpha = 0.5
    theta = 3

    x = [7, -2, -5, 4]
    d = 1


if __name__ == "__main__":
    main()
