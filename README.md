# myPyllant

[![PyPI](https://img.shields.io/pypi/v/myPyllant)](https://pypi.org/project/myPyllant/)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/signalkraft/myPyllant/build-test.yaml)

A Python library to interact with the API behind the myVAILLANT app ((and branded versions of it, such as the MiGo app from Saunier Duval). Needs at least Python 3.10.

Not affiliated with Vaillant, the developers take no responsibility for anything that happens to your devices because of this library.

![myPyllant](https://raw.githubusercontent.com/signalkraft/myPyllant/main/logo.png)

## Install and Test

> **Warning**
> 
> You need at least Python 3.10

```shell
pip install myPyllant
python3 -m myPyllant.export user password country brand
# See python3 -m myPyllant.export -h for more options and a list of countries
```

The `--data` argument exports historical data of the devices in your system.
Without this keyword, information about your system will be exported as JSON.

## Usage

```python
#!/usr/bin/env python3

import argparse
import asyncio
import logging
from datetime import datetime, timedelta

from myPyllant.api import MyPyllantAPI
from myPyllant.const import BRANDS, COUNTRIES, DEFAULT_BRAND

parser = argparse.ArgumentParser(description="Export data from myVaillant API   .")
parser.add_argument("user", help="Username (email address) for the myVaillant app")
parser.add_argument("password", help="Password for the myVaillant app")
parser.add_argument(
    "country",
    help="Country your account is registered in, i.e. 'germany'",
    choices=COUNTRIES[DEFAULT_BRAND].keys(),
)
parser.add_argument(
    "brand",
    help="Brand your account is registered in, i.e. 'vaillant'",
    default=DEFAULT_BRAND,
    choices=BRANDS.keys(),
)
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)


async def main(user, password, country, brand):
    async with MyPyllantAPI(user, password, country, brand) as api:
        async for system in api.get_systems():
            print(await api.get_time_zone(system))
            print(await api.set_holiday(system))
            print(
                await api.set_holiday(
                    system, datetime.now(), datetime.now() + timedelta(days=7)
                )
            )
            print(await api.get_time_zone(system))
            print(await api.cancel_holiday(system))
            print(await api.boost_domestic_hot_water(system.domestic_hot_water[0]))
            print(await api.cancel_hot_water_boost(system.domestic_hot_water[0]))
            print(
                await api.set_domestic_hot_water_temperature(
                    system.domestic_hot_water[0], 46
                )
            )
            print(await api.set_set_back_temperature(system.zones[0], 15.5))
            print(await api.quick_veto_zone_temperature(system.zones[0], 21, 5))
            print(await api.cancel_quick_veto_zone_temperature(system.zones[0]))


if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(args.user, args.password, args.country, args.brand))

```

### Tested Configurations

See https://github.com/signalkraft/mypyllant-component/blob/main/README.md#tested-setups

## Contributing

> **Warning**
> 
> You need at least Python 3.10

I'm happy to accept PRs, if you run the pre-commit checks and test your changes:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pre-commit install
pytest
```

### Supporting new Countries

The myVAILLANT app uses Keycloak and OIDC for authentication, with a realm for each country and brand.
There is a script to check which countries are supported:

```shell
python3 -m myPyllant.tests.find_countries
```

Copy the resulting dictionary into [src/myPyllant/const.py](src/myPyllant/const.py)

### Contributing Test Data

Because the myVAILLANT API isn't documented, you can help the development of this library by contributing test data:

```shell
python3 -m myPyllant.tests.generate_test_data username password country brand
```

Create a fork of this repository and create a PR with the newly created folder in `src/myPyllant/tests/json`.

## Notes

* Auth is loosely based on https://github.com/TA2k/ioBroker.vaillant
* Most API endpoints are reverse-engineered from the myVaillant app, using https://github.com/mitmproxy/mitmproxy
* Setting weekly time tables for heating and domestic hot water is still missing
* There is a home assistant component based on this library here: https://github.com/signalkraft/mypyllant-component

Logo based on [Hase Icons erstellt von Freepik - Flaticon](https://www.flaticon.com/de/kostenlose-icons/hase) & [Ouroboros Icons erstellt von Freepik - Flaticon](https://www.flaticon.com/de/kostenlose-icons/ouroboros).
