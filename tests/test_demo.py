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

        assert '<form id="postter" method="POST">' in rv.data
        assert '<div id="post_response"></div>' in rv.data
        assert 'You posted:' not in rv.data


    def test_get_echo(self):
        rv = self.app.get('/echo?txt=Foo Bar')
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="getter" method="GET">' in rv.data
        assert '<div id="get_response">You said: Foo Bar</div>' in rv.data

        assert '<form id="postter" method="POST">' in rv.data
        assert '<div id="post_response"></div>' in rv.data
        assert 'You posted:' not in rv.data

    def test_post_echo(self):
        rv = self.app.post('/echo', data=dict(
            msg='Hello World'
        ))
        self.assertEqual(rv.status, '200 OK')
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="getter" method="GET">' in rv.data
        assert '<div id="get_response"></div>' in rv.data
        assert 'You said:' not in rv.data

        assert '<form id="postter" method="POST">' in rv.data
        assert '<div id="post_response">You posted: Hello World</div>' in rv.data


    def test_account(self):
        rv = self.app.get('/account')
        self.assertEqual(rv.status, '401 UNAUTHORIZED')
        assert 'only accessible' in rv.data
        #print(rv.data)

    def test_failed_login(self):
        rv = self.app.get('/login')
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="login" method="POST">' in rv.data
        assert 'Invalid login' not in rv.data
        assert 'Welcome' not in rv.data
 
        rv = self.app.post('/login')
        #print(rv.data)
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="login" method="POST">' in rv.data
        assert 'Invalid login' in rv.data
        assert 'Welcome' not in rv.data

        rv = self.app.post('/login', data=dict(
            username='user1',
            password='bad'
        ))
        assert '<!DOCTYPE html>' in rv.data
        assert '<form id="login" method="POST">' in rv.data
        assert 'Invalid login' in rv.data
        assert 'Welcome' not in rv.data

    def test_session(self):
        rv = self.app.post('/login', data=dict(
            username='user1',
            password='pw1'
        ))
        assert '<!DOCTYPE html>' in rv.data
        #print(rv.data)
        assert '<form id="login" method="POST">' not in rv.data
        assert 'Invalid login' not in rv.data
        assert 'Welcome user1' in rv.data

        rv = self.app.get('/account')
        self.assertEqual(rv.status, '200 OK')
        assert 'only accessible' not in rv.data
        assert '<title>Account of user1</title>' in rv.data
        assert 'Welcome user1' in rv.data

        rv = self.app.get('/logout')
        assert '<!DOCTYPE html>' in rv.data
        assert 'Goodby' in rv.data

        rv = self.app.get('/account')
        self.assertEqual(rv.status, '401 UNAUTHORIZED')
        assert 'only accessible' in rv.data
 
    def test_other(self):
        rv = self.app.get('/other')
        #print(rv.status)
        self.assertEqual(rv.status, '404 NOT FOUND')

# vim: expandtab
