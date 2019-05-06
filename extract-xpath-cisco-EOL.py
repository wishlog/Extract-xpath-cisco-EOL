import requests
from lxml import html

urls = ["https://www.cisco.com/c/en/us/products/collateral/routers/1700-series-modular-access-routers/prod_end-of-life_notice0900aecd8044473f.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/1800-series-integrated-services-routers-isr/eol_c51-625662.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/1800-series-integrated-services-routers-isr/eol_c51_597946.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/1800-series-integrated-services-routers-isr/eol_c51_598758.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/1900-series-integrated-services-routers-isr/eos-eol-notice-c51-740520.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/2600-series-multiservice-platforms/prod_end-of-life_notice0900aecd804446da.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/2800-series-integrated-services-routers-isr/end_of_life_notice_c51-728143.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/2800-series-integrated-services-routers-isr/eol_c51-655336.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/2900-series-integrated-services-routers-isr/eos-eol-notice-c51-737831.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/3800-series-integrated-services-routers-isr/eol_c51-696796.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/3900-series-integrated-services-routers-isr/eos-eol-notice-c51-737830.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/800-series-routers/eos-eol-notice-c51-730680.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/800-series-routers/eos-eol-notice-c51-730681.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/800-series-routers/prod_end-of-life_notice0900aecd805b174f.html",
"https://www.cisco.com/c/en/us/products/collateral/routers/asr-1000-series-aggregation-services-routers/eos-eol-notice-c51-734572.html",
"https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eol_C51-727283.html",
"https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eol_C51-727284.html",
"https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eos-eol-notice-c51-738644.html",
"https://www.cisco.com/c/en/us/products/collateral/security/asa-5500-series-next-generation-firewalls/eos-eol-notice-c51-741287.html",
"https://www.cisco.com/c/en/us/products/collateral/security/asa-5505-adaptive-security-appliance/eos-eol-notice-c51-738642.html",
"https://www.cisco.com/c/en/us/products/collateral/security/firepower-7000-series-appliances/eos-eol-notice-c51-739207.html",
"https://www.cisco.com/c/en/us/products/collateral/security/identity-services-engine/eos-eol-notice-c51-737032.html",
#//"https://www.cisco.com/c/en/us/products/collateral/security/identity-services-engine/eos-eol-notice-c51-742122.pdf",
"https://www.cisco.com/c/en/us/products/collateral/security/ips-4200-series-sensors/eos-eol-notice-c51-733186.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2950-series-switches/prod_end-of-life_notice0900aecd806ea1da.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-series-switches/end_of_life_c51-674040.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-series-switches/eos-eol-notice-c51-730121.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-2960-series-switches/eos-eol-notice-c51-733348.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3560-x-series-switches/eos-eol-notice-c51-736139.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3750-series-switches/eol_c51-696372.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3750-series-switches/eos-eol-notice-c51-730227.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/prod_end-of-life_notice0900aecd8035ece4.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/nexus-3000-series-switches/eos-eol-notice-c51-737069.html",
"https://www.cisco.com/c/en/us/products/collateral/switches/nexus-7000-series-switches/end_of_life_notice_c51-729278.html",
"https://www.cisco.com/c/en/us/products/collateral/wireless/aironet-1600-series/eos-eol-notice-c51-737506.html"]

for url in urls:
	resp = requests.get(url)
	tree = html.fromstring(str(resp.content,'utf-8'))
	inputs = tree.xpath(".//*[@id='eot-doc-wrapper']/div/div[1]/table/tbody/tr/td[3]/p/text()")
	try:
		print(url + "\t" + inputs[-1])
	except:
		print(url + "\t" + 'failed')
