import json
import uuid
import time
import os
from kafka import KafkaProducer
from Broker_dev import Broker_dev, get_ssl_context  #При необходимости заменить стенд


def load_notification_types(file_path='notification_type.json'):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")

    with open(file_path, 'r', encoding='utf-8') as f:
        notification_types = json.load(f)

    if not isinstance(notification_types, list) or not all(isinstance(ntype, str) for ntype in notification_types):
        raise ValueError("Некорректный формат данных в файле notification_type.json")

    return notification_types


def create_producer():
    config = Broker_dev.copy() #При необходимости заменить стенд
    config['ssl_context'] = get_ssl_context()
    return KafkaProducer(**config)


def main():
    try:
        notification_types = load_notification_types()
        print(f"Загружено {len(notification_types)} типов уведомлений")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return

    producer = create_producer()

    try:
        for ntype in notification_types:
            message = {
                "eventId": str(uuid.uuid4()),
                "serviceCode": "",         #Указать код сервиса соответствующий notificationType
                "userIds": [
                    ""                     #Указать список external_id для соответствующего стенда

                ],
                "notificationType": ntype,
                "data": {
                    "firstName": "Notification User",
                    "content": f"<html><body>Тип: <strong>{ntype}</strong></body></html>"
                }
            }

            # print("Отправка:", json.dumps(message, indent=2, ensure_ascii=False))

            # log_file.write(json.dumps(message, ensure_ascii=False) + '\n')

            producer.send('enterprise-integrations-notification.broadcast-event', value=message)
            print(f"Отправлено уведомление типа: {ntype}")
            time.sleep(1)

    finally:
        producer.flush()
        producer.close()
        print("Все сообщения отправлены!")


if __name__ == "__main__":
    main()