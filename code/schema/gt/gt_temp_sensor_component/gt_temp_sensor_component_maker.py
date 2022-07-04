"""Makes gt.temp.sensor.component.100 type"""
import json
from typing import Optional

from schema.gt.gt_temp_sensor_component.gt_temp_sensor_component import GtTempSensorComponent
from schema.errors import MpSchemaError


class GtTempSensorComponent_Maker:
    type_alias = "gt.temp.sensor.component.100"

    def __init__(self,
                 component_id: str,
                 component_attribute_class_id: str,
                 display_name: Optional[str],
                 hw_uid: Optional[str]):

        gw_tuple = GtTempSensorComponent(
            DisplayName=display_name,
            ComponentId=component_id,
            ComponentAttributeClassId=component_attribute_class_id,
            HwUid=hw_uid,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtTempSensorComponent) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtTempSensorComponent:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtTempSensorComponent:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "ComponentId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentId")
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "HwUid" not in new_d.keys():
            new_d["HwUid"] = None

        gw_tuple = GtTempSensorComponent(
            TypeAlias=new_d["TypeAlias"],
            DisplayName=new_d["DisplayName"],
            ComponentId=new_d["ComponentId"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            HwUid=new_d["HwUid"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
