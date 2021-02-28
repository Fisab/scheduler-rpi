from crontab import CronTab

my_cron = CronTab(user='pi')

job = my_cron.new(command='python3 /home/pi/rpi-services/scheduler-rpi/app/ip-changer.py')
job.every(1).hours()
my_cron.write()

job = my_cron.new(command='python3 /home/pi/rpi-services/scheduler-rpi/app/backup.py')
job.every(24).hours()
my_cron.write()
