from lib.report_length import *

def test_report_length_report_5_from_hello():
    result = report_length("hello")
    assert result == "This string was 5 characters"
    
