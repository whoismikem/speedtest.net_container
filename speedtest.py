import argparse
import threading
import time

from influxspeedtest.InfluxdbSpeedtest import InfluxdbSpeedtest

parser = argparse.ArgumentParser(description="A tool to take network speed test and send the results to InfluxDB")
args = parser.parse_args()
collector = InfluxdbSpeedtest()



th = threading.Thread(target=collector.run)

th.start()

print('--- After thread ---')
for i in range(51):
       print('Hi from Main Thread')
       time.sleep(1)