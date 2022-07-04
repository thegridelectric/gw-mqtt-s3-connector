"""Makes gt.electric.meter.cac.100 type"""
import json
from typing import Optional

from schema.gt.gt_electric_meter_cac.gt_electric_meter_cac import GtElectricMeterCac
from schema.errors import MpSchemaError
from schema.enums.local_comm_interface.local_comm_interface_map import (
    LocalCommInterface,
    LocalCommInterfaceMap,
)
from schema.enums.make_model.make_model_map import (
    MakeModel,
    MakeModelMap,
)


class GtElectricMeterCac_Maker:
    type_alias = "gt.electric.meter.cac.100"

    def __init__(self,
                 component_attribute_class_id: str,
                 local_comm_interface: LocalCommInterface,
                 make_model: MakeModel,
                 display_name: Optional[str],
                 default_baud: Optional[int],
                 update_period_ms: Optional[int]):

        gw_tuple = GtElectricMeterCac(
            ComponentAttributeClassId=component_attribute_class_id,
            LocalCommInterface=local_comm_interface,
            MakeModel=make_model,
            DisplayName=display_name,
            DefaultBaud=default_baud,
            UpdatePeriodMs=update_period_ms,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtElectricMeterCac) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtElectricMeterCac:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtElectricMeterCac:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "LocalCommInterfaceGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing LocalCommInterfaceGtEnumSymbol")
        new_d["LocalCommInterface"] = LocalCommInterfaceMap.gt_to_local(new_d["LocalCommInterfaceGtEnumSymbol"])
        if "MakeModelGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing MakeModelGtEnumSymbol")
        new_d["MakeModel"] = MakeModelMap.gt_to_local(new_d["MakeModelGtEnumSymbol"])
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "DefaultBaud" not in new_d.keys():
            new_d["DefaultBaud"] = None
        if "UpdatePeriodMs" not in new_d.keys():
            new_d["UpdatePeriodMs"] = None

        gw_tuple = GtElectricMeterCac(
            TypeAlias=new_d["TypeAlias"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            LocalCommInterface=new_d["LocalCommInterface"],
            MakeModel=new_d["MakeModel"],
            DisplayName=new_d["DisplayName"],
            DefaultBaud=new_d["DefaultBaud"],
            UpdatePeriodMs=new_d["UpdatePeriodMs"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
