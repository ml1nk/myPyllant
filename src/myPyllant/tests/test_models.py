import pytest
from dacite import WrongTypeError

from ..models import Claim, System, ZoneHeating, ZoneHeatingOperatingMode
from .test_api import list_test_data


@pytest.mark.parametrize("test_data", list_test_data())
async def test_systems(mypyllant_aioresponses, mocked_api, test_data) -> None:
    with mypyllant_aioresponses(test_data) as _:
        system = await anext(mocked_api.get_systems())

        assert isinstance(system, System), "Expected System return type"
        assert isinstance(system.claim, Claim)
        assert isinstance(system.claim.system_id, str)


async def test_type_validation() -> None:
    with pytest.raises(WrongTypeError):
        ZoneHeating.from_api(
            manual_mode_setpoint_heating="15.0",
            operation_mode_heating=ZoneHeatingOperatingMode.MANUAL,
            time_program_heating={},
            set_back_temperature=15.0,
        )
    with pytest.raises(ValueError):
        ZoneHeating.from_api(
            manual_mode_setpoint_heating=15.0,
            operation_mode_heating="INVALID",
            time_program_heating={},
            set_back_temperature=15.0,
        )
