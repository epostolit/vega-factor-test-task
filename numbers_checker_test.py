from numbers_checker_solutions import *


@dataclass
class NumbersStep:
    m: int
    n: int

    def next(self) -> int:
        return self.m**2 + self.n**2 + 1

    def __eq__(self, value: object) -> bool:
        return (
            self.m == value.m
            and self.n == value.n
            or self.n == value.m
            and self.m == value.n
        )


def test_23():
    a = 2
    b = 3
    checker = Checker(3)
    checker.run_check()

    correct_path = NumbersPath(a, b, ([NumbersStep(1, 1)], []))

    path = checker.get_path(a, b)
    assert path == correct_path


def test_34():
    a = 3
    b = 4
    checker = Checker(4)
    checker.run_check()

    correct_path = NumbersPath(
        a,
        b,
        (
            [NumbersStep(1, 2), NumbersStep(3, 3), NumbersStep(11, 8)],
            [NumbersStep(4, 0), NumbersStep(13, 4)],
        ),
    )

    path = checker.get_path(a, b)
    assert path == correct_path


def test_correct_path():
    N = 10
    checker = Checker(N)
    checker.run_check()

    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            path = checker.get_path(a, b)
            assert path.a == a
            assert path.b == b

            cur_a, cur_b = a, b
            for numbers_step in path.steps[0]:  # check a
                assert numbers_step.m + numbers_step.n == cur_a
                cur_a = numbers_step.next()

            for numbers_step in path.steps[1]:  # check b
                assert numbers_step.m + numbers_step.n == cur_b
                cur_b = numbers_step.next()

            assert cur_a == cur_b


if __name__ == "__main__":
    test_23()
    test_34()
    test_correct_path()
