from itaxotools.common.bindings import Binder, Property, PropertyObject


class DummyObject(PropertyObject):
    dummy = Property(int, 0)


def test_simple_bind():

    a = DummyObject()
    b = DummyObject()

    binder = Binder()
    binder.bind(a.properties.dummy, b.properties.dummy)

    assert b.dummy == 0
    a.dummy = 42
    assert b.dummy == 42


def test_proxy_bind():

    a = DummyObject()
    b = DummyObject()

    binder = Binder()
    binder.bind(a.properties.dummy, b.properties.dummy, proxy = lambda x: x + 1)

    assert b.dummy == 1
    a.dummy = 42
    assert b.dummy == 43


def test_conditional_bind():

    a = DummyObject()
    b = DummyObject()

    binder = Binder()
    binder.bind(a.properties.dummy, b.properties.dummy, condition = lambda x: x > 10)

    assert b.dummy == 0

    a.dummy = 9
    assert b.dummy == 0

    a.dummy = 11
    assert b.dummy == 11
