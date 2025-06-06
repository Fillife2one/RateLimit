import ssl
import json


Broker_test = {
    'bootstrap_servers': [''],        #Взять из Vault для test стенда
    'security_protocol': 'SASL_SSL',
    'sasl_mechanism': 'SCRAM-SHA-512',
    'sasl_plain_username': '',        #Взять из Vault для test стенда
    'sasl_plain_password': '',        #Взять из Vault для test стенда
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'key_serializer': lambda k: k.encode('utf-8') if k else None
}

def get_ssl_context():
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations(r'C:\MyPytonProjects\CA.pem') # Указать путь к расположению CA.pem
    return ssl_context