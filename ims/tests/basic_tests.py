#!/usr/bin/python
from flaskext.testing import TestCase

def create_app():
    from ims import app
    return app 

class BasicTestCase(TestCase):
    def create_app(self):
        return create_app()
        
    def test_sample(self):
        assert(1 == 1)

    def test_index(self): 
        response = self.client.get("/")
        self.assert200(response)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        """Make sure login and logout works"""
        '''
        rv = self.login(flaskr.app.config['USERNAME'],
                        flaskr.app.config['PASSWORD'])
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login(flaskr.app.config['USERNAME'] + 'x',
                        flaskr.app.config['PASSWORD'])
        assert 'Invalid username' in rv.data
        rv = self.login(flaskr.app.config['USERNAME'],
                        flaskr.app.config['PASSWORD'] + 'x')
        assert 'Invalid password' in rv.data
        '''
        pass

    def test_register(self):
        pass
