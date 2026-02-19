#pip install -r requirements.txt    directory to be where the folder is and run from console
import random
import time
import uuid
from datetime import datetime
from pymongo import MongoClient

class WaterSensor:
    def __init__(self, device_ids):
        self.device_ids = device_ids
        self.mongo_client = MongoClient("*************************")# Change connection string as needed
        self.db = self.mongo_client["iotdatadb"]
        self.collection = self.db["sensor_data_prd"]

    def generate_data(self):
        unique_id = str(uuid.uuid4())
        device_id = random.choice(self.device_ids)
        message_type = random.choice([47, 79])
        water_level = random.randint(190, 1289)
        battery_level = random.randint(18, 98)
        timestamp_utc = datetime.utcnow()

        data = {
            "_id": unique_id,
            "time": timestamp_utc,
            "Messagetype": message_type,
            "Level": water_level,
            "Battery": battery_level,
            "device": device_id
        }
        return data

    def write_to_mongodb(self, data):
        self.collection.insert_one(data)

def main():
    device_ids = ["1FA1185", "1FA1A01"]
    sensor = WaterSensor(device_ids)

    while True:
        data = sensor.generate_data()
        print("Sending data:", data)
        sensor.write_to_mongodb(data)
        # Sleep for a random interval between 600 to 900 seconds
        sleep_duration = random.randint(540, 900)
        time.sleep(sleep_duration)  # Simulate sending data every 5 seconds

if __name__ == "__main__":
    main()




