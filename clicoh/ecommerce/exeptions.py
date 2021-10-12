"""Module with all exceptions for a ecommerce."""


class StockInProductError(Exception):
    """Error when trying to select a product without stock."""


class CuantityZeroError(Exception):
    """Error when Cuantity in order-detail is zero."""


class ProductRepetitionOrderError(Exception):
    """Product repetition in the same order."""
