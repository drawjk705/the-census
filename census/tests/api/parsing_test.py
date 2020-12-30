from typing import Any, Dict
from census.api.parsing import parseVariableData
from collections import defaultdict
from census.api.models import GroupVariable
from hypothesis.core import given
import hypothesis.strategies as st
from hypothesis import assume


@given(
    group=st.text(),
    concept=st.text(),
    varCode1=st.text(),
    label1=st.text(),
    predicateType1=st.text(),
    limit1=st.integers(),
    predicateOnly1=st.booleans(),
    varCode2=st.text(),
    label2=st.text(),
    predicateType2=st.text(),
    limit2=st.integers(),
    predicateOnly2=st.booleans(),
)
def test_parseVariableData(
    concept: str,
    group: str,
    varCode1: str,
    label1: str,
    predicateType1: str,
    limit1: int,
    predicateOnly1: bool,
    varCode2: str,
    label2: str,
    predicateType2: str,
    limit2: int,
    predicateOnly2: bool,
):
    assume(varCode1 != varCode2)

    variables = {
        "variables": {
            varCode1: {
                "label": label1,
                "concept": concept,
                "predicateType": predicateType1,
                "group": group,
                "limit": limit1,
                "predicateOnly": predicateOnly1,
            },
            varCode2: {
                "label": label2,
                "concept": concept,
                "predicateType": predicateType2,
                "group": group,
                "limit": limit2,
                "predicateOnly": predicateOnly2,
            },
        }
    }

    expectedVar1 = GroupVariable(varCode1, variables["variables"][varCode1])

    expectedVar2 = GroupVariable(varCode2, variables["variables"][varCode2])

    expected = [expectedVar1, expectedVar2]

    actual = parseVariableData(variables)

    assert actual == expected
