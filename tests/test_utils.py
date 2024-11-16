import pytest
from app.utils import format_usd

def test_format_usd():
    assert format_usd(1234567.89) == "$1,234,567.89"
    assert format_usd(0) == "$0.00"
    assert format_usd(-9876.543) == "$-9,876.54"
    assert format_usd(100) == "$100.00"