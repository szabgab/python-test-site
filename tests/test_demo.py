import demo.demo
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.app = demo.demo.app.test_client()
        demo.demo.app.config['TESTING'] = True

    def test_main(self):
        rv = self.app.get('/')
        data = rv.data.decode("utf-8") 
        #print(data)
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in data
        self.assertRegexpMatches(data, r'<title>Python Test site</title>')
        self.assertRegexpMatches(data, r'<a href="/echo">Echo</a>')
        self.assertRegexpMatches(data, r'<a href="/other">Other</a>')

    def test_echo(self):
        rv = self.app.get('/echo')
        data = rv.data.decode("utf-8") 
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in data
        assert '<form id="getter" method="GET">' in data
        assert '<div id="get_response"></div>' in data
        assert 'You said:' not in data

        assert '<form id="postter" method="POST">' in data
        assert '<div id="post_response"></div>' in data
        assert 'You posted:' not in data


    def test_get_echo(self):
        rv = self.app.get('/echo?txt=Foo Bar')
        self.assertEqual(rv.status, '200 OK')
        data = rv.data.decode("utf-8") 
        assert '<!DOCTYPE html>' in data
        assert '<form id="getter" method="GET">' in data
        assert '<div id="get_response">You said: Foo Bar</div>' in data

        assert '<form id="postter" method="POST">' in data
        assert '<div id="post_response"></div>' in data
        assert 'You posted:' not in data

    def test_post_echo(self):
        rv = self.app.post('/echo', data=dict(
            msg='Hello World'
        ))
        self.assertEqual(rv.status, '200 OK')
        data = rv.data.decode("utf-8") 
        assert '<!DOCTYPE html>' in data
        assert '<form id="getter" method="GET">' in data
        assert '<div id="get_response"></div>' in data
        assert 'You said:' not in data

        assert '<form id="postter" method="POST">' in data
        assert '<div id="post_response">You posted: Hello World</div>' in data


    def test_account(self):
        rv = self.app.get('/account')
        self.assertEqual(rv.status, '401 UNAUTHORIZED')
        data = rv.data.decode("utf-8") 
        assert 'only accessible' in data
        #print(data)

    def test_failed_login(self):
        rv = self.app.get('/login')
        data = rv.data.decode("utf-8") 
        assert '<!DOCTYPE html>' in data
        assert '<form id="login" method="POST">' in data
        assert 'Invalid login' not in data
        assert 'Welcome' not in data
 
        rv = self.app.post('/login')
        data = rv.data.decode("utf-8") 
        #print(data)
        assert '<!DOCTYPE html>' in data
        assert '<form id="login" method="POST">' in data
        assert 'Invalid login' in data
        assert 'Welcome' not in data

        rv = self.app.post('/login', data=dict(
            username='user1',
            password='bad'
        ))
        assert '<!DOCTYPE html>' in data
        assert '<form id="login" method="POST">' in data
        assert 'Invalid login' in data
        assert 'Welcome' not in data

    def test_session(self):
        rv = self.app.post('/login', data=dict(
            username='user1',
            password='pw1'
        ))
        data = rv.data.decode("utf-8") 
        assert '<!DOCTYPE html>' in data
        #print(data)
        assert '<form id="login" method="POST">' not in data
        assert 'Invalid login' not in data
        assert 'Welcome user1' in data

        rv = self.app.get('/account')
        data = rv.data.decode("utf-8") 
        self.assertEqual(rv.status, '200 OK')
        data = rv.data.decode("utf-8") 
        assert 'only accessible' not in data
        assert '<title>Account of user1</title>' in data
        assert 'Welcome user1' in data

        rv = self.app.get('/logout')
        data = rv.data.decode("utf-8") 
        assert '<!DOCTYPE html>' in data
        assert 'Goodby' in data

        rv = self.app.get('/account')
        data = rv.data.decode("utf-8") 
        self.assertEqual(rv.status, '401 UNAUTHORIZED')
        assert 'only accessible' in data
 
    def test_other(self):
        rv = self.app.get('/other')
        #print(rv.status)
        self.assertEqual(rv.status, '404 NOT FOUND')

# vim: expandtab
