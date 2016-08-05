import demo.demo
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.app = demo.demo.app.test_client()
        demo.demo.app.config['TESTING'] = True

    def test_main(self):
        rv = self.app.get('/')
        #print(rv.data)
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in rv.data
        self.assertRegexpMatches(rv.data, r'<title>Python Test site</title>')
        self.assertRegexpMatches(rv.data, r'<a href="/echo">Echo</a>')
        self.assertRegexpMatches(rv.data, r'<a href="/other">Other</a>')

    def test_echo(self):
        rv = self.app.get('/echo')
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="getter" method="GET">' in rv.data
        assert '<div id="get_response"></div>' in rv.data
        assert 'You said:' not in rv.data

    def test_echo(self):
        rv = self.app.get('/echo?txt=Foo Bar')
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="getter" method="GET">' in rv.data
        assert '<div id="get_response">You said: Foo Bar</div>' in rv.data

    def test_other(self):
        rv = self.app.get('/other')
        #print(rv.status)
        self.assertEqual(rv.status, '404 NOT FOUND')

# vim: expandtab
