import pytest
import threading
from task_2_3 import fetch_universities

def test_fetch_universities():
    result_dict = {}
    countries = ["Poland", "Germany"]

    threads = []
    for country in countries:
        thread = threading.Thread(target=fetch_universities, args=(country, result_dict))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for country in countries:
        assert country in result_dict
        assert isinstance(result_dict[country], list)