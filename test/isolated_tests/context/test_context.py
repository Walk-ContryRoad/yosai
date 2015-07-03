import pytest
from yosai import (
    MapContext,
)


def test_mapcontext_init():
    MapContext()

def test_mapcontext_attributes(default_map_context):
    assert isinstance(default_map_context.attributes, list)

def test_mapcontext_values(default_map_context):
    assert isinstance(default_map_context.values, tuple)

def test_mapcontext_clear(default_map_context):
    default_map_context.clear()
    assert len(default_map_context.context) == 0

def test_mapcontext_len(default_map_context):
    assert len(default_map_context) == 3

def test_mapcontext_nonzero():
    emptycontext1 = MapContext()
    emptycontext2 = MapContext({'one': 1})
    assert not emptycontext1 and emptycontext2

def test_mapcontext_contains(default_map_context):
    assert ('nine' not in default_map_context and
            'attribute2' not in default_map_context and
            'attr3' in default_map_context)

def test_mapcontext_setattr(default_map_context):
    default_map_context.test = 'testing'
    assert default_map_context.context.get('test') == 'testing'

def test_mapcontext_getattr(default_map_context):
    assert default_map_context.attr2 == 'attribute2'

def test_mapcontext_delattr(default_map_context):
    del default_map_context.attr1
    assert default_map_context.context.get('attr1', 'nope') == 'nope'
