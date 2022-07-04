"""Makes gt.electric.heater.component.100 type"""
import json
from typing import Optional

from schema.gt.gt_electric_heater_component.gt_electric_heater_component import GtElectricHeaterComponent
from schema.errors import MpSchemaError


class GtElectricHeaterComponent_Maker:
    type_alias = "gt.electric.heater.component.100"

    def __init__(self,
                 component_id: str,
                 component_attribute_class_id: str,
                 hw_uid: Optional[str],
                 display_name: Optional[str]):

        gw_tuple = GtElectricHeaterComponent(
            HwUid=hw_uid,
            DisplayName=display_name,
            ComponentId=component_id,
            ComponentAttributeClassId=component_attribute_class_id,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtElectricHeaterComponent) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtElectricHeaterComponent:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtElectricHeaterComponent:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "HwUid" not in new_d.keys():
            new_d["HwUid"] = None
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "ComponentId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentId")
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")

        gw_tuple = GtElectricHeaterComponent(
            TypeAlias=new_d["TypeAlias"],
            HwUid=new_d["HwUid"],
            DisplayName=new_d["DisplayName"],
            ComponentId=new_d["ComponentId"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
