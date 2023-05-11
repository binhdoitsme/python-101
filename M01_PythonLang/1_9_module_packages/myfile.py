# import ...
# from ... import ...

import weather_forecast # import only module
from weather_forecast import get_weather_forecast, locations # import name from module
# every functions, variables defined in global scope can be imported via from...import

forecast = weather_forecast.get_weather_forecast("Hanoi")
print(forecast)

forecast = get_weather_forecast("Hanoi")
print(forecast)

# import whole folder -> need __init__.py & fill in __init__.py
import services
# services.do_obscure_thing

# only import from a file within a folder -> need __init__.py
from services import obscure_service
obscure_service.do_obscure_thing()

# only import subset of a file within a folder -> NO NEED for __init__.py
from services.obscure_service import do_obscure_thing
do_obscure_thing()
