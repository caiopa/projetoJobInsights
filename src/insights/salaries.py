from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salary = [
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()]
    return max(max_salary)
    # raise NotImplementedError


def get_min_salary(path: str) -> int:
    jobs = read(path)
    max_salary = [
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()]
    return min(max_salary)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
    except (TypeError, TypeError, KeyError):
        raise ValueError
    if min_salary > max_salary or type(salary) not in [int, str]:
        raise ValueError
    return int(min_salary) <= int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
