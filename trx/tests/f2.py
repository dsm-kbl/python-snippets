from trx.p1 import f1
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

def test_case1():
    with unittest.mock.patch('p1.f1._test1') as test_mock:
        assert test_mock.call_count == 1
