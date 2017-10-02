import unittest
import requests
#import calc
def make_calc_request(expression, expected_value):
    result = requests.get("http://localhost:8080/calc/"+expression)
    assert result.status_code == 200
    assert 'json' in result.headers['Content-Type']
    data = result.json()
    assert (data['value']) == expected_value

class Service_TestCase(unittest.TestCase):
    def test_000_do_nothing(self):
        pass

    def test_001_test_simple_expression(self):
        make_calc_request("1+2+3+4",10)
        make_calc_request("1+1",2)
        make_calc_request("1",1)
        make_calc_request("-4e2",-400)
        make_calc_request("-4e-2",-0.04)
        make_calc_request("-4e+-2","#NONE#")


if __name__ == "__main__":
    unittest.main(verbosity=2)
