class ProductOfNumbers:

    def __init__(self):
        # self.products will store prefix products of non-zero numbers since the last zero.
        # It always starts with 1 to handle division for the product of the first element
        # in a sequence of non-zero numbers.
        # For example, if the current effective numbers are [a, b, c],
        # self.products will be [1, a, a*b, a*b*c].
        self.products = [1] 

    def add(self, num: int) -> None:
        if num == 0:
            # If 0 is added, any product involving this 0 will be 0.
            # Also, all previous non-zero prefix products become irrelevant for
            # future products that include this 0.
            # We reset the products list to just [1], effectively starting a new sequence
            # of prefix products for numbers added after this zero.
            self.products = [1]
        else:
            # If a non-zero number is added, we extend the prefix product list.
            # The new product is the last product in the list multiplied by the new number.
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        # N_effective is the count of non-zero numbers currently represented in our
        # self.products list. This is len(self.products) - 1, because self.products[0]
        # is the dummy '1' representing an empty product.
        N_effective = len(self.products) - 1

        if k > N_effective:
            # If k is greater than the count of non-zero numbers since the last zero,
            # it implies that the sequence of the last k numbers must include a zero
            # that caused a reset of the self.products list.
            # Therefore, the product of these k numbers is 0.
            return 0
        else:
            # If k <= N_effective, it means the last k numbers in the conceptual stream
            # (since the last zero or beginning) are all non-zero.
            # We can calculate their product using prefix products:
            # (product of all N_effective non-zero numbers) /
            # (product of the first N_effective - k non-zero numbers)
            # This corresponds to self.products[N_effective] / self.products[N_effective - k].
            # We use integer division // as the result is guaranteed to be an integer.
            return self.products[N_effective] // self.products[N_effective - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)