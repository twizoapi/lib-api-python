![Twizo](http://www.twizo.com/online/logo/logo.png) 


# Twizo Python API

Connect to the Twizo API using the python 3 library. This API includes functions to send verifications (2FA), SMS and Number Lookup.

## Requirements
* [Python 3.4 +](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)

## Get application secret and api host
To use the Twizo API client, the following things are required:

* Create a [Twizo account](https://register.twizo.com/)
* Login on the Twizo portal
* Find your [application](https://portal.twizo.com/applications/) secret
* Find your nearest [api node](https://www.twizo.com/developers/documentation/#introduction_api-url)

## Installation ##

[pip](#Link-to-PyPi-Package) -- Link needs to be added

    $ pip install twizo-lib-python
    
## Getting started ##

Initialize the Twizo API with your api host and api key

``` python
from twizo import Twizo

twizo = Twizo(api_key="<Your api key here>",
              api_host="<Your desired api host here>")
``` 


Create a new verification

``` python
    params = VerificationParams('12345000000')
    response =  twizo.verification_controller.create(params)
```

Verify token

``` python
    verify_result =  twizo.verification_controller.verify_token(
        response.messageId, "012345"
    )
```


Send sms

``` python

    params = SmsParams(
        recipients='60123456789',
        body="Hey Alice, how are you doing?", 
        sender='John')
    response = twizo.sms_controller.send_simple(params)
```

## Examples ##

In the examples directory you can find some examples of how to use the api.

## License ##
[The MIT License](https://opensource.org/licenses/mit-license.php).
Copyright (c) 2016-2017 Twizo

## Support ##
Contact: [www.twizo.com](http://www.twizo.com/) — support@twizo.com