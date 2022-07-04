"""Makes gt.temp.sensor.cac.100 type"""
import json
from typing import Optional

from schema.gt.gt_temp_sensor_cac.gt_temp_sensor_cac import GtTempSensorCac
from schema.errors import MpSchemaError
from schema.enums.telemetry_name.telemetry_name_map import (
    TelemetryName,
    TelemetryNameMap,
)
from schema.enums.unit.unit_map import (
    Unit,
    UnitMap,
)
from schema.enums.make_model.make_model_map import (
    MakeModel,
    MakeModelMap,
)


class GtTempSensorCac_Maker:
    type_alias = "gt.temp.sensor.cac.100"

    def __init__(self,
                 telemetry_name: TelemetryName,
                 temp_unit: Unit,
                 make_model: MakeModel,
                 component_attribute_class_id: str,
                 exponent: int,
                 typical_response_time_ms: int,
                 display_name: Optional[str],
                 comms_method: Optional[str]):

        gw_tuple = GtTempSensorCac(
            TelemetryName=telemetry_name,
            DisplayName=display_name,
            TempUnit=temp_unit,
            MakeModel=make_model,
            ComponentAttributeClassId=component_attribute_class_id,
            Exponent=exponent,
            CommsMethod=comms_method,
            TypicalResponseTimeMs=typical_response_time_ms,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtTempSensorCac) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtTempSensorCac:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtTempSensorCac:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "TelemetryNameGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TelemetryNameGtEnumSymbol")
        new_d["TelemetryName"] = TelemetryNameMap.gt_to_local(new_d["TelemetryNameGtEnumSymbol"])
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "TempUnitGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TempUnitGtEnumSymbol")
        new_d["TempUnit"] = UnitMap.gt_to_local(new_d["TempUnitGtEnumSymbol"])
        if "MakeModelGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing MakeModelGtEnumSymbol")
        new_d["MakeModel"] = MakeModelMap.gt_to_local(new_d["MakeModelGtEnumSymbol"])
        if "ComponentAttributeClassId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ComponentAttributeClassId")
        if "Exponent" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing Exponent")
        if "CommsMethod" not in new_d.keys():
            new_d["CommsMethod"] = None
        if "TypicalResponseTimeMs" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypicalResponseTimeMs")

        gw_tuple = GtTempSensorCac(
            TypeAlias=new_d["TypeAlias"],
            TelemetryName=new_d["TelemetryName"],
            DisplayName=new_d["DisplayName"],
            TempUnit=new_d["TempUnit"],
            MakeModel=new_d["MakeModel"],
            ComponentAttributeClassId=new_d["ComponentAttributeClassId"],
            Exponent=new_d["Exponent"],
            CommsMethod=new_d["CommsMethod"],
            TypicalResponseTimeMs=new_d["TypicalResponseTimeMs"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
