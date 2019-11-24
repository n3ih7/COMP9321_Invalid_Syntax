## Deployment
Assumed environment:


Debian 9 x64 with root permission and desktop version


apt update


apt install wget git python3 python3-pip


wget https://github.com/n3ih7/COMP9321_Invalid_Syntax/releases/download/1.0/submit.tar


tar xvf file.tar


pip3 install -r requirements.txt


cd swagger-ui


nohup python3 -m http.server &


cd . .


python3 stable.py




## API USE CASE
#### api_usage
/api/api_usage?APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### weather
/api/weather?cityName=Sydney&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### cause_of_fire
/api/cause_of_fire?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### severity_rating
/api/severity_rating?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### severity_rating
/api/severity_rating?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### cause_analysis
/api/cause_analysis?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### fire_factors
/api/fire_factors?start_date=2012-10-1&city_name=New%20York&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### happened_times
/api/happened_times?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
#### state_and_fire
/api/state_and_fire?start_date=2012-10-1&end_date=2017-9-1&APPID=2db16d2a-c3b7-4d60-9bec-66f9996a91d1
