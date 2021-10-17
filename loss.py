class ListMinLengthError(Exception):
    pass


def find_max_loss(prises):
    if len(prises) < 2:
        raise ListMinLengthError("Getting a loss requires at least 2 prices")

    max_price, max_loss = prises[0], prises[0] - prises[1]

    for current_price in prises:
        potential_loss = max_price - current_price
        max_loss = max(max_loss, potential_loss)
        max_price = max(max_price, current_price)

    # in case the loss is impossible then max_loss will be a negative number
    return max(max_loss, 0)


from unittest import TestCase


class TestFindMaxLoss(TestCase):
    def test_not_enough_data(self):
        with self.assertRaises(ListMinLengthError):
            find_max_loss([])

        with self.assertRaises(ListMinLengthError):
            find_max_loss([10])

    def test_all_transactions_make_a_profit(self):
        self.assertEqual(find_max_loss([10.5, 20.45, 30.01, 40]), 0)

    def test_max_loss_at_the_start_of_prices_list(self):
        self.assertEqual(find_max_loss([100, 10, 40, 50, 20]), 90)

    def test_max_loss_at_the_middle_of_prices_list(self):
        self.assertEqual(find_max_loss([100, 10, 1000, 50, 60]), 950)

    def test_max_loss_at_the_end_of_prices_list(self):
        self.assertEqual(find_max_loss([20, 10, 0, 20, 100, 10]), 90)

    def test_max_loss_use_extreme_elements(self):
        self.assertEqual(find_max_loss([100, 20, 50, 10]), 90)

    def test_max_loss_is_not_min_max_difference(self):
        self.assertEqual(find_max_loss([20, 10, 100, 100, 30]), 70)

    def test_time_complexity(self):
        # the best solution has at most linear complexity
        import time
        import random

        length = 100_000
        prices = random.sample(range(0, 100_000), length)

        def goal_time():
            start_time = time.time()
            for i in range(length):
                prices[i] = 2 * prices[i] - prices[i]
            return time.time() - start_time

        from timeout_decorator import timeout

        timeout(
            seconds=goal_time() * 10,
            exception_message="The function is slower than 10*O(n)")
        (
            find_max_loss(prices)
        )
