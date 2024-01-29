#!/usr/bin/env python3
"""
1. Simple pagination
"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    The function should return a tuple of size two
    containing a start index
    and
    an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    p_range = (((page - 1) * page_size), ((page) * page_size))
    return (p_range)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """
        assert isinstance(page, int) and isinstance(page_size, int),\
            "page and page_size must be integers"
        assert page > 0 and page_size > 0,\
            "page and page_size must be greater than zero"

        strt_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if strt_idx > len(dataset):
            return ([])

        return dataset[strt_idx:end_idx]
