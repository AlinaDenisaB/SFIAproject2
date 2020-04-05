import pytest
import app
from application import routes
    
def test_randnumsgen2():
    assert len(routes.numGen())==5

def test_type():
    assert type(routes.numGen())==str
