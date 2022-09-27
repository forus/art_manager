from rest_framework.test import APITestCase
from rest_framework import status

janneke = {'username': 'janneke', 'password': 'janneke!12345'}
sjoerd = {'username': 'sjoerd', 'password': 'sjoerd!12345'}
admin = {'username': 'admin', 'password': 'admin!12345'}

class UsersTests(APITestCase):
  """
   Test for Anonymous user
  """

  def test_list_users_as_anonymous(self):
    response = self.client.get('/inventory/api/users/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_post_user_as_anonymous(self):
    response = self.client.post('/inventory/api/users/',
      { 'username': 'test', 'email': 'test@example.com' }, format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_user_as_anonymous(self):
    response = self.client.delete('/inventory/api/users/1/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_list_art_locations_as_anonymous(self):
    response = self.client.get('/inventory/api/art-locations/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_post_art_locations_as_anonymous(self):
    response = self.client.post('/inventory/api/art-locations/',
                                {'art_item': 'http://testserver/inventory/api/art-items/1/',
                                 'spot': 'http://testserver/inventory/api/spots/1/',
                                 'start_date': '2025-01-01',
                                 'responsible_person': 'http://testserver/inventory/api/users/1/'},
                                 format='json')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_delete_art_locations_as_anonymous(self):
    response = self.client.delete('/inventory/api/art-locations/1/')
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  """
   Test for a Municipality worker
  """

  def test_list_users_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.get('/inventory/api/users/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_user_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.post('/inventory/api/users/',
      {'username': 'test', 'email': 'test@example.com' }, format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_delete_user_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.delete('/inventory/api/users/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_list_art_locations_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.get('/inventory/api/art-locations/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_art_locations_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.post('/inventory/api/art-locations/',
                                {'art_item': 'http://testserver/inventory/api/art-items/1/',
                                 'spot': 'http://testserver/inventory/api/spots/1/',
                                 'start_date': '2025-01-01',
                                 'responsible_person': 'http://testserver/inventory/api/users/1/'},
                                format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_delete_art_locations_as_municipality_worker(self):
    self.client.login(username=janneke['username'], password=janneke['password'])
    response = self.client.delete('/inventory/api/art-locations/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  """
   Test for a Art manager
  """

  def test_list_users_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.get('/inventory/api/users/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_user_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.post('/inventory/api/users/',
                                {'username': 'test', 'email': 'test@example.com'}, format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_delete_user_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.delete('/inventory/api/users/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_list_art_locations_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.get('/inventory/api/art-locations/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_art_locations_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.post('/inventory/api/art-locations/',
                                {'art_item': 'http://testserver/inventory/api/art-items/1/',
                                 'spot': 'http://testserver/inventory/api/spots/1/',
                                 'start_date': '2025-01-01',
                                 'responsible_person': 'http://testserver/inventory/api/users/1/'},
                                format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_delete_art_locations_as_art_manager(self):
    self.client.login(
        username=sjoerd['username'], password=sjoerd['password'])
    response = self.client.delete('/inventory/api/art-locations/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  """
   Test for an Admin
  """

  def test_list_users_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.get('/inventory/api/users/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_user_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.post('/inventory/api/users/',
                                {'username': 'test', 'email': 'test@example.com'}, format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_delete_user_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.delete('/inventory/api/users/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_list_art_locations_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.get('/inventory/api/art-locations/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post_art_locations_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.post('/inventory/api/art-locations/',
                                {'art_item': 'http://testserver/inventory/api/art-items/1/',
                                 'spot': 'http://testserver/inventory/api/spots/1/',
                                 'start_date': '2025-01-01',
                                 'responsible_person': 'http://testserver/inventory/api/users/1/'},
                                format='json')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_delete_art_locations_as_admin(self):
    self.client.login(
        username=admin['username'], password=admin['password'])
    response = self.client.delete('/inventory/api/art-locations/1/')
    self.client.logout()
    self.assertEqual(response.status_code, status.HTTP_200_OK)
