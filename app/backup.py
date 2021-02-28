import dropbox_cli
import yaml
import os


with open('data.yml') as file:
	config = yaml.load(file, Loader=yaml.FullLoader)


def ignore_this(path: str) -> bool:
	"""
	:param path:
	:return: True if need ignore this path
	"""
	for ignore_substr in config['backup']['ignore']:
		if path.find(ignore_substr) != -1:
			return True
	return False


def main():
	for directory in config['backup']['dirs']:
		dir_name = directory.split('/')[-1] if directory[-1] != '/' else directory.split('/')[-2]
		upload_path = f'{config["backup"]["upload_dir"]}/{dir_name.split("/")[-1]}'
		for root, _, files in os.walk(directory):
			root = root if root[-1] != '/' else root[:-1]
			if ignore_this(root):
				continue

			for file in files:
				file_path = f'{root}/{file}'
				upload_file_path = f'{upload_path}/{file_path.replace(directory, "")}'

				# print(file_path, upload_file_path)

				dropbox_cli.upload_file(file_path, upload_file_path)


if __name__ == '__main__':
	main()



