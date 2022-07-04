"""Makes gt.boolean.actuator.cac.100 type"""
import json
from typing import Optional

from schema.gt.gt_boolean_actuator_cac.gt_boolean_actuator_cac import GtBooleanActuatorCac
from schema.errors import MpSchemaError
from schema.enums.make_model.make_model_map import (
    MakeModel,
    MakeModelMap,
)


class GtBooleanActuatorCac_Maker:
    type_alias = "gt.boolean.actuator.cac.100"

    def __init__(self,
                 make_model: MakeModel,
                 component_attribute_class_id: str,
                 typical_response_time_ms: int,
                 display_name: Optional[str]):

        gw_tuple = GtBooleanActuatorCac(
            MakeModel=make_model,
            ComponentAttributeClassId=component_attribute_class_id,
            TypicalResponseTimeMs=typical_response_time_ms,
            DisplayName=display_name,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtBooleanActuatorCac) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtBooleanActuatorCac:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtBooleanActuatorCac:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "MakeModelGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing MakeModelGtEnumSymbol")
        new_d["MakeModel"] = MakeModelMap.gt_to_local(new_d["MakeModelGtEnumSymbol"])
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "TypicalResponseTimeMs" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypicalResponseTimeMs")
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None

        gw_tuple = GtBooleanActuatorCac(
            TypeAlias=new_d["TypeAlias"],
            MakeModel=new_d["MakeModel"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            TypicalResponseTimeMs=new_d["TypicalResponseTimeMs"],
            DisplayName=new_d["DisplayName"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
