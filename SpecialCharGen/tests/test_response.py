import pytest
import app
from application import routes
    
def test_specialchargen():
    assert len(routes.specialChar())==2

def test_type():
    assert type(routes.specialChar())==str
