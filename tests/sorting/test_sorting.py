from src.pre_built.sorting import sort_by

mocks = [

    {"min_salary": 500, "max_salary": 1500},
    {"min_salary": 1000, "max_salary": 2500},
    {"min_salary": 1500, "max_salary": 3500},
]

order_max = [ 
    {"min_salary": 1500, "max_salary": 3500},
    {"min_salary": 1000, "max_salary": 2500},
    {"min_salary": 500, "max_salary": 1500},
]

order_min = [
    {"min_salary": 500, "max_salary": 1500},
    {"min_salary": 1000, "max_salary": 2500},
    {"min_salary": 1500, "max_salary": 3500},
]


def test_sort_by_criteria():
    sort_by(mocks, "min_salary")
    assert mocks == order_min
    sort_by(mocks, "max_salary")
    assert mocks == order_max
    pass
