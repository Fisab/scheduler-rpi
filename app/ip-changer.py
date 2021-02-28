import requests
import yaml
import json

with open('data.yml') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)
	access_token = config['cloudflare']['token']


def get_actual_ip():
	r = requests.get('https://api.myip.com/')
	return r.json().get('ip')


def _query_cloudflare(endpoint, method, data=None):
	if data is None:
		data = {}
	headers = {
		'Authorization': f'Bearer {access_token}',
		'Content-Type': 'application/json'
	}

	url = f'https://api.cloudflare.com/client/v4/{endpoint}'
	return requests.request(
		method=method,
		url=url,
		headers=headers,
		data=json.dumps(data)
	)


def get_zones():
	return _query_cloudflare(
		'zones',
		'GET'
	)


def get_dns(zone=None):
	if zone is None:
		zone = config['ip-changer']['zone']
	r = _query_cloudflare(
		f'zones/{zone}/dns_records',
		'GET'
	)
	return r.json()


def update_records(new_ip, zone=None):
	if zone is None:
		zone = config['ip-changer']['zone']
	records = get_dns()
	for record in records.get('result', []):
		if record['name'] not in config['ip-changer']['names']:
			continue

		data = {
			'type': record['type'],
			'name': record['name'],
			'proxied': record['proxied'],
			'ttl': record['ttl'],
			'content': new_ip
		}
		r = _query_cloudflare(
			endpoint=f'zones/{zone}/dns_records/{record["id"]}',
			method='PUT',
			data=data
		)
		# print(r.json())


if __name__ == '__main__':
	actual_ip = get_actual_ip()
	update_records(actual_ip)

