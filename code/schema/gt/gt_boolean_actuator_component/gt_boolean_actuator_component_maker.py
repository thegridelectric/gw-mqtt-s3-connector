"""Makes gt.boolean.actuator.component.100 type"""
import json
from typing import Optional

from schema.gt.gt_boolean_actuator_component.gt_boolean_actuator_component import GtBooleanActuatorComponent
from schema.errors import MpSchemaError


class GtBooleanActuatorComponent_Maker:
    type_alias = "gt.boolean.actuator.component.100"

    def __init__(self,
                 component_attribute_class_id: str,
                 component_id: str,
                 display_name: Optional[str],
                 gpio: Optional[int],
                 hw_uid: Optional[str]):

        gw_tuple = GtBooleanActuatorComponent(
            DisplayName=display_name,
            ComponentAttributeClassId=component_attribute_class_id,
            ComponentId=component_id,
            Gpio=gpio,
            HwUid=hw_uid,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtBooleanActuatorComponent) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtBooleanActuatorComponent:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtBooleanActuatorComponent:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "ComponentId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentId")
        if "Gpio" not in new_d.keys():
            new_d["Gpio"] = None
        if "HwUid" not in new_d.keys():
            new_d["HwUid"] = None

        gw_tuple = GtBooleanActuatorComponent(
            TypeAlias=new_d["TypeAlias"],
            DisplayName=new_d["DisplayName"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            ComponentId=new_d["ComponentId"],
            Gpio=new_d["Gpio"],
            HwUid=new_d["HwUid"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
