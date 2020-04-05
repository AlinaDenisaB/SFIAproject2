import pytest
import app
from application import routes
    
def test_randnumsgen():
    assert len(routes.numGen())==3

def test_type():
    assert type(routes.numGen())==str
