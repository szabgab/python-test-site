import demo.demo
import unittest
import json

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.app = demo.demo.app.test_client()
        demo.demo.app.config['TESTING'] = True

    def test_static(self):
        rv = self.app.get('/api/static')
        self.assertEqual(rv.status, '200 OK')
        #print(rv.data)
        d = json.loads(rv.data)
        assert d['text'] == 'Hello World'

# vim: expandtab
