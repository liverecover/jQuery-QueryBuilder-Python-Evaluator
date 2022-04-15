# make all strings lower case to do case insensitive match
def lower(data):
    if isinstance(data, str):
        return data.lower()

    if isinstance(data, list) and len(data) and isinstance(data[0], str):
        return [d.lower() for d in data]

    return data

class Operators:
    @staticmethod
    def eval_begins_with(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x.startswith(right), left))
        return left.startswith(right)

    @staticmethod
    def eval_between(input, bounds):
        return bounds[0] < input < bounds[1]

    @staticmethod
    def eval_contains(left, right):
        left = lower(left)
        right = lower(right)

        if isinstance(right, list):
            if isinstance(left, list):
                return any([any(map(lambda x: r in x, left)) for r in right])
            return any([r == left for r in right])
        else:
            if isinstance(left, list):
                return any(map(lambda x: right in x, left))
            return right in left

    @staticmethod
    def eval_ends_with(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x.endswith(right), left))
        return left.endswith(right)

    @staticmethod
    def eval_equal(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x == right, left))
        return left == right

    @staticmethod
    def eval_greater(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x > right, left))
        return left > right

    @staticmethod
    def eval_greater_or_equal(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x >= right, left))
        return left >= right

    @staticmethod
    def eval_in(left, right):
        return right in left

    @staticmethod
    def eval_is_empty(input, value):
        if isinstance(input, list):
            return not bool(input)
        return not bool(input and input.strip())

    @staticmethod
    def eval_is_not_empty(input, value):
        if isinstance(input, list):
            return bool(input)
        return bool(input and input.strip())

    @staticmethod
    def eval_is_not_null(input, value):
        return input is not None

    @staticmethod
    def eval_is_null(input, value):
        return input is None

    @staticmethod
    def eval_less(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x < right, left))
        return left < right

    @staticmethod
    def eval_less_or_equal(left, right):
        if isinstance(left, list):
            return any(map(lambda x: x <= right, left))
        return left <= right

    @staticmethod
    def eval_not_begins_with(left, right):
        if isinstance(left, list):
            return not any(map(lambda x: x.startswith(right), left))
        return not left.startswith(right)

    @staticmethod
    def eval_not_between(input, bounds):
        if isinstance(input, list):
            return not any(map(lambda x: x <= bounds[0] or x >= bounds[1], input))
        return input <= bounds[0] or input >= bounds[1]

    @staticmethod
    def eval_not_contains(left, right):
        left = lower(left)
        right = lower(right)

        if isinstance(right, list):
            if isinstance(left, list):
                return not any([any(map(lambda x: r in x, left)) for r in right])
            return not any([r == left for r in right])
        else:
            if isinstance(left, list):
                return not any(map(lambda x: right in x, left))
            return right not in left

    @staticmethod
    def eval_not_ends_with(left, right):
        if isinstance(left, list):
            return not any(map(lambda x: x.endswith(right), left))
        return not left.endswith(right)

    @staticmethod
    def eval_not_equal(left, right):
        if isinstance(left, list):
            return not any(map(lambda x: left == right, left))
        return left != right

    @staticmethod
    def eval_not_in(left, right):
        return right not in left


if __name__ == '__main__':
    assert Operators.eval_contains("A", ["a"]) == True
    assert Operators.eval_contains(["A"], "a") == True
    assert Operators.eval_contains("A", "a") == True
    assert Operators.eval_contains(["A"], ["a"]) == True
    assert Operators.eval_contains([], ["a"]) == False
    assert Operators.eval_contains("A", []) == False

    assert Operators.eval_not_contains("A", ["a"]) == False
    assert Operators.eval_not_contains(["A"], "a") == False
    assert Operators.eval_not_contains("A", "a") == False
    assert Operators.eval_not_contains(["A"], ["a"]) == False
    assert Operators.eval_not_contains([], ["a"]) == True
    assert Operators.eval_not_contains("A", []) == True
    print("OK")