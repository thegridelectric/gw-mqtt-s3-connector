"""Tests gt.pipe.flow.sensor.component.100 type"""
import json

import pytest

from schema.errors import MpSchemaError
from schema.gt.gt_pipe_flow_sensor_component.gt_pipe_flow_sensor_component_maker import (
    GtPipeFlowSensorComponent_Maker as Maker,
)


def test_gt_pipe_flow_sensor_component():

    gw_dict = {
        "ComponentId": "dd5ac673-91a8-40e2-a233-b67479cec709",
        "DisplayName": "Flow meter on pipe out of tank",
        "HwUid": "1234",
        "ComponentAttributeClassId": "14e7105a-e797-485a-a304-328ecc85cd98",
        "TypeAlias": "gt.pipe.flow.sensor.component.100",
    }

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple(gw_dict)

    with pytest.raises(MpSchemaError):
        Maker.type_to_tuple('"not a dict"')

    # Test type_to_tuple
    gw_type = json.dumps(gw_dict)
    gw_tuple = Maker.type_to_tuple(gw_type)

    # test type_to_tuple and tuple_to_type maps
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple

    # test Maker init
    t = Maker(
        component_id=gw_tuple.ComponentId,
        display_name=gw_tuple.DisplayName,
        component_attribute_class_id=gw_tuple.ComponentAttributeClassId,
        hw_uid=gw_tuple.HwUid,
        #
    ).tuple
    assert t == gw_tuple

    ######################################
    # MpSchemaError raised if missing a required attribute
    ######################################

    orig_value = gw_dict["TypeAlias"]
    del gw_dict["TypeAlias"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["TypeAlias"] = orig_value

    orig_value = gw_dict["ComponentId"]
    del gw_dict["ComponentId"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["ComponentId"] = orig_value

    orig_value = gw_dict["ComponentAttributeClassId"]
    del gw_dict["ComponentAttributeClassId"]
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["ComponentAttributeClassId"] = orig_value

    ######################################
    # Optional attributes can be removed from type
    ######################################

    orig_value = gw_dict["DisplayName"]
    del gw_dict["DisplayName"]
    gw_type = json.dumps(gw_dict)
    gw_tuple = Maker.type_to_tuple(gw_type)
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple
    gw_dict["DisplayName"] = orig_value

    orig_value = gw_dict["HwUid"]
    del gw_dict["HwUid"]
    gw_type = json.dumps(gw_dict)
    gw_tuple = Maker.type_to_tuple(gw_type)
    assert Maker.type_to_tuple(Maker.tuple_to_type(gw_tuple)) == gw_tuple
    gw_dict["HwUid"] = orig_value

    ######################################
    # MpSchemaError raised if attributes have incorrect type
    ######################################

    orig_value = gw_dict["ComponentId"]
    gw_dict["ComponentId"] = 42
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["ComponentId"] = orig_value

    orig_value = gw_dict["DisplayName"]
    gw_dict["DisplayName"] = 42
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["DisplayName"] = orig_value

    orig_value = gw_dict["ComponentAttributeClassId"]
    gw_dict["ComponentAttributeClassId"] = "Not a dataclass id"
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["ComponentAttributeClassId"] = orig_value

    orig_value = gw_dict["HwUid"]
    gw_dict["HwUid"] = 42
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["HwUid"] = orig_value

    ######################################
    # MpSchemaError raised if TypeAlias is incorrect
    ######################################

    gw_dict["TypeAlias"] = "not the type alias"
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["TypeAlias"] = "gt.pipe.flow.sensor.component.100"

    ######################################
    # MpSchemaError raised if primitive attributes do not have appropriate property_format
    ######################################

    gw_dict["ComponentId"] = "d4be12d5-33ba-4f1f-b9e5"
    with pytest.raises(MpSchemaError):
        Maker.dict_to_tuple(gw_dict)
    gw_dict["ComponentId"] = "dd5ac673-91a8-40e2-a233-b67479cec709"

    # End of Test
