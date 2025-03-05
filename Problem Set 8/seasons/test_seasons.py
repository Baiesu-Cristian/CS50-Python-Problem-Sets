from seasons import check_date
import pytest

def test_input():
     with pytest.raises(SystemExit):
         check_date("01-01-1999")