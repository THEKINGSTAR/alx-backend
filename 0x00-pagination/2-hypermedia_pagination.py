#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""


import csv
import math
from typing import Dict
from typing import List, Union


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

    #  def get_hyper (self, page: int = 1, page_size: int = 10)
    #  -> Dict{page_size, page, data,next_page,prev_page,total_pages}:
    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> Dict[str, Union[int, List[List], int]]:
        """
        Implement get_hyper method that takes the same arguments (and defaults)
        as get_page and returns a dictionary containing the
        following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.
        You can use the math module if necessary.
        """
        data_set = self.get_page(page, page_size)

        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        prev_page = page - 1
        if prev_page <= 0:
            prev_page = None

        next_page = page + 1
        if next_page > total_pages:
            next_page = None
        if page > total_pages:
            page_size = 0
        key_value_dic = {"page_size": page_size,
                         "page": page,
                         "data": data_set,
                         "next_page": next_page,
                         "prev_page": prev_page,
                         "total_pages": total_pages}

        return (key_value_dic)
