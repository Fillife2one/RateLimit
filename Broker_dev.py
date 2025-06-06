import ssl
import json

Broker_dev = {
    'bootstrap_servers': [
        'rc1a-ba5c25fm7u9it8hp.mdb.yandexcloud.net:9091',
        'rc1b-1krcdm1ruusegflu.mdb.yandexcloud.net:9091',
        'rc1d-7cqjebgji7rdp6id.mdb.yandexcloud.net:9091'
    ],
    'security_protocol': 'SASL_SSL',
    'sasl_mechanism': 'SCRAM-SHA-512',
    'sasl_plain_username': 'enterprise-integrations-notification-atom-notification-service',
    'sasl_plain_password': 'chaiL1bah6ge9cei',
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'key_serializer': lambda k: k.encode('utf-8') if k else None
}

def get_ssl_context():
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(r'C:\MyPytonProjects\CA.pem') # Указать путь к расположению CA.pem
    return ssl_context