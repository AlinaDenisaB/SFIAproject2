import pytest
import app
from application import routes
    
def test_specialchargen2():
    assert len(routes.specialChar())==3

def test_type():
    assert type(routes.specialChar())==str
