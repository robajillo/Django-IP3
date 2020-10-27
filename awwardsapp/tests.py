from django.test import TestCase
from .models import *

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(is_superuser='saphira',groups='group',user_permissions='adad',password='access',last_login= '2020-10-27 14:59:55.739608+00',username='saphira',email='saphira@gmail.com',is_active='active',first_name='saphira',last_name='saphira',is_staff='satt',date_joined= '2020-10-27 14:59:55.739608+00')
        self.user.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create( is_superuser='saphira',groups='group',user_permissions='adad',password='access',last_login= '2020-10-27 14:59:55.739608+00',username='saphira',email='saphira@gmail.com',is_active='active',first_name='saphira',last_name='saphira',is_staff='satt',date_joined= '2020-10-27 14:59:55.739608+00')
        self.profile = Profile.objects.create(user = self.user,bio = 'my bio',name='saphira',location='gigiri',contact=  'saphira@gmail.com',)

        self.post = Post.objects.create(user = self.user,
                                          profile = self.profile,
                                          title = 'insta',
                                          project_link= 'https://roba-awwards.herokuapp.com/',
                                          description='description',
                                          created_date='2020-10-27 14:59:55.739608+00'
                                          )

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        post = Post.get_posts()
        self.assertTrue(len(post) == 1)

    def test_find_post(self):
        self.post.save()
        post = Post.search_post('insta')
        self.assertTrue(len(post) > 0)

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create( is_superuser='saphira',groups='group',user_permissions='adad',password='access',last_login= '2020-10-27 14:59:55.739608+00',username='saphira',email='saphira@gmail.com',is_active='active',first_name='saphira',last_name='saphira',is_staff='satt',date_joined= '2020-10-27 14:59:55.739608+00')
        self.post = Post.objects.create(user = self.user,
                                          profile = self.profile,
                                          title = 'insta',
                                          project_link= 'https://roba-awwards.herokuapp.com/',
                                          description='description',
                                          created_date='2020-10-27 14:59:55.739608+00'
                                          )
        self.rating = Rating.objects.create(user=self.user,post=self.post, design=6, usability=7, content=9,comment='comment')


    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_ratings(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)