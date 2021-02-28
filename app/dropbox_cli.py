import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import yaml
import logging


with open('data.yml') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)
	access_token = config['dropbox']['token']

dbx = dropbox.Dropbox(access_token)


def upload_file(file: str, upload_file_path: str):
	try:
		with open(file, 'rb') as f:
			dbx.files_upload(f.read(), upload_file_path, mode=WriteMode('overwrite'))
	except ApiError as api_err:
		logging.error(f'Got error when uploading {file}: {api_err}')
