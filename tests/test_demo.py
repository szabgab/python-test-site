import demo.demo
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.app = demo.demo.app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        #print(rv.data)
        self.assertEqual(rv.status, '200 OK')
        self.assertRegexpMatches(rv.data, r'<title>Python Test site</title>')
        self.assertRegexpMatches(rv.data, r'<a href="/echo">Echo</a>')

    def test_ech(self):
        rv = self.app.get('/echo')
        #print(rv.status)
        self.assertEqual(rv.status, '404 NOT FOUND')

# vim: expandtab
