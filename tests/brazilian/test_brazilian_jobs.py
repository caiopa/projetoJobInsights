from src.pre_built.brazilian_jobs import read_brazilian_file

mock = {"title": "", "salary": "", "type": ""}
path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    pass
    read_file = read_brazilian_file(path)

    for job in read_file:
        assert mock.keys() == job.keys()
