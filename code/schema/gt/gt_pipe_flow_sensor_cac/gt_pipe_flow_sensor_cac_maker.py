"""Makes gt.pipe.flow.sensor.cac.100 type"""
import json
from typing import Optional

from schema.gt.gt_pipe_flow_sensor_cac.gt_pipe_flow_sensor_cac import GtPipeFlowSensorCac
from schema.errors import MpSchemaError
from schema.enums.make_model.make_model_map import (
    MakeModel,
    MakeModelMap,
)


class GtPipeFlowSensorCac_Maker:
    type_alias = "gt.pipe.flow.sensor.cac.100"

    def __init__(self,
                 component_attribute_class_id: str,
                 make_model: MakeModel,
                 display_name: Optional[str],
                 comms_method: Optional[str]):

        gw_tuple = GtPipeFlowSensorCac(
            DisplayName=display_name,
            ComponentAttributeClassId=component_attribute_class_id,
            CommsMethod=comms_method,
            MakeModel=make_model,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtPipeFlowSensorCac) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtPipeFlowSensorCac:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtPipeFlowSensorCac:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "CommsMethod" not in new_d.keys():
            new_d["CommsMethod"] = None
        if "MakeModelGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing MakeModelGtEnumSymbol")
        new_d["MakeModel"] = MakeModelMap.gt_to_local(new_d["MakeModelGtEnumSymbol"])

        gw_tuple = GtPipeFlowSensorCac(
            TypeAlias=new_d["TypeAlias"],
            DisplayName=new_d["DisplayName"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            CommsMethod=new_d["CommsMethod"],
            MakeModel=new_d["MakeModel"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
