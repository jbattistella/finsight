from app.client.client import ClientConfigs
import unittest



class TestClientConfigs(unittest.TestCase):

    configs = ClientConfigs()
    assert configs.args == "test-config"
    
    