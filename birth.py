from parents import Mom, Dad
from types import Boy
from legal_system import marriage
from operations import consummate

parental_units = marriage.Hetero(Dad(), Mom(), "Hudkins")
Hudkins = parental_units.__class__

nick = None
while not nick:
    if consummate.attempt(*(parental_units.partners)):
        nick = new Hudkins("Nick", Boy())