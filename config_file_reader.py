import configparser
import os
thisfolder = os.path.dirname(os.path.abspath(__file__))
execution_environment = 'STAGING'

if execution_environment == 'STAGING':
    print("Selected environment is : ",execution_environment)
    initfile = os.path.join(thisfolder, 'staging.properties')
elif execution_environment == 'QA':
    print("Selected environment is : ", execution_environment)
    pass
elif execution_environment == 'PRODUCTION':
    print("Selected environment is : ", execution_environment)
    pass
else:
    pass


config = configparser.RawConfigParser()
res = config.read(initfile)

price_fetch_url = config.get('DetailSection1', 'price_fetch_url')
print(price_fetch_url)
