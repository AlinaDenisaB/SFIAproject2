import pytest
import app
from application import routes
    
def test_randletgen():
    assert len(routes.letGen())==15

def test_type():
    assert type(routes.letGen())==str
