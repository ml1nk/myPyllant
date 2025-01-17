from datetime import datetime

from myPyllant.utils import datetime_parse


async def test_invalid_country() -> None:
    assert isinstance(datetime_parse("2022-03-28T19:37:12.27334Z"), datetime)
    assert isinstance(datetime_parse("2022-03-28T19:37:12Z"), datetime)
