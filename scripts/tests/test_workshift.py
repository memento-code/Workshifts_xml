import pytest
import json
from workshifts import WorkshiftXML


def test_module():
    obj = WorkshiftXML('tests/test_workshifts.xml')
    data = obj.workshifts()
    assert json.loads(data.to_json()) == {"workshift_minutes": {"21-12-2011": 1027.3333333333,
                                                                "22-12-2011": 1147.3333333333,
                                                                "23-12-2011": 727.3333333333,
                                                                "24-12-2011": 842.3333333333}}


def test_filters():
    obj = WorkshiftXML('tests/test_workshifts.xml')
    data = obj.workshifts(filter_start_date='21-12-2011',
                          filter_end_date='23-12-2011',
                          logins='b.testobject,a.stepanova')

    assert json.loads(data.to_json()) == {"workshift_minutes": {"21-12-2011": 499.0833333333,
                                                                "22-12-2011": 619.0833333333}}


def test_empty_result():
    obj = WorkshiftXML('tests/test_workshifts.xml')
    data = obj.workshifts(filter_start_date='21-12-2022', filter_end_date='23-12-2022')
    assert data is None


def test_wrong_path():
    obj = WorkshiftXML('tests/test_workshifts.xmllllll')
    with pytest.raises(FileNotFoundError):
        obj.workshifts(filter_start_date='21-12-2001', filter_end_date='23-12-2022')
