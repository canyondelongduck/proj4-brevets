"""
Nose tests for acp_times.py
"""
from acp_times import open_time, close_time

START = "2017-01-01T00:00:00+00:00"


# basic cases on a 200 km brevet

def test_60km_on_200():
    assert open_time(60, 200, START) == "2017-01-01T01:46:00+00:00"
    assert close_time(60, 200, START) == "2017-01-01T04:00:00+00:00"


def test_120km_on_200():
    assert open_time(120, 200, START) == "2017-01-01T03:32:00+00:00"
    assert close_time(120, 200, START) == "2017-01-01T08:00:00+00:00"


def test_175km_on_200():
    assert open_time(175, 200, START) == "2017-01-01T05:09:00+00:00"
    assert close_time(175, 200, START) == "2017-01-01T11:40:00+00:00"


# edge cases near the start

def test_0km_closes_after_one_hour():
    assert open_time(0, 200, START) == "2017-01-01T00:00:00+00:00"
    assert close_time(0, 200, START) == "2017-01-01T01:00:00+00:00"


def test_61km_uses_standard_rule():
    # just past the 60 km relaxed rule cutoff
    assert open_time(61, 200, START) == "2017-01-01T01:48:00+00:00"
    assert close_time(61, 200, START) == "2017-01-01T04:04:00+00:00"


# finish controls

def test_200km_finish_uses_fixed_limit():
    assert open_time(200, 200, START) == "2017-01-01T05:53:00+00:00"
    assert close_time(200, 200, START) == "2017-01-01T13:30:00+00:00"


def test_205km_is_capped_to_200():
    assert open_time(205, 200, START) == open_time(200, 200, START)
    assert close_time(205, 200, START) == "2017-01-01T13:30:00+00:00"


def test_250km_is_capped_to_200():
    assert open_time(250, 200, START) == open_time(200, 200, START)
    assert close_time(250, 200, START) == close_time(200, 200, START)


def test_300km_finish_on_300():
    assert open_time(300, 300, START) == "2017-01-01T09:00:00+00:00"
    assert close_time(300, 300, START) == "2017-01-01T20:00:00+00:00"


def test_400km_finish_uses_fixed_limit():
    assert open_time(400, 400, START) == "2017-01-01T12:08:00+00:00"
    assert close_time(400, 400, START) == "2017-01-02T03:00:00+00:00"


def test_600km_finish_on_600():
    assert open_time(600, 600, START) == "2017-01-01T18:48:00+00:00"
    assert close_time(600, 600, START) == "2017-01-02T16:00:00+00:00"


def test_1000km_finish_on_1000():
    assert open_time(1000, 1000, START) == "2017-01-02T09:05:00+00:00"
    assert close_time(1000, 1000, START) == "2017-01-04T03:00:00+00:00"


# controls over several speed ranges

def test_100km_on_600():
    assert open_time(100, 600, START) == "2017-01-01T02:56:00+00:00"
    assert close_time(100, 600, START) == "2017-01-01T06:40:00+00:00"


def test_350km_on_600():
    assert open_time(350, 600, START) == "2017-01-01T10:34:00+00:00"
    assert close_time(350, 600, START) == "2017-01-01T23:20:00+00:00"


def test_550km_on_600():
    assert open_time(550, 600, START) == "2017-01-01T17:08:00+00:00"
    assert close_time(550, 600, START) == "2017-01-02T12:40:00+00:00"


def test_300km_on_400():
    assert open_time(300, 400, START) == "2017-01-01T09:00:00+00:00"
    assert close_time(300, 400, START) == "2017-01-01T20:00:00+00:00"


def test_890km_on_1000():
    assert open_time(890, 1000, START) == "2017-01-02T05:09:00+00:00"
    assert close_time(890, 1000, START) == "2017-01-03T17:23:00+00:00"