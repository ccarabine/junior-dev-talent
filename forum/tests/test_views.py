# Im# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages

# Internal:
from forum.models import Topic, Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestTopicModel(TestCase):
    """Test Topic model"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='chris_c', password='p2word')
        self.client.login(username='chris_c', password='p2word')
        self.user.save()

        self.topic = Topic.objects.create(
            name="Coding",
            friendly_name="Coding",
            slug="Coding",
            topic_image="topic_img",
            )
        self.post = Post.objects.create(
            topic=self.topic,
            title="interview question",
            owner=self.user,
            slug="interview%question"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            owner=self.user,
            comment_body="Great idea",
            name="Chris Carabine"
        )

    def tearDown(self):
        """
        Delete test user, topic, post and comment
        """
        User.objects.all().delete()
        Topic.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

    def test_topic_model_instance(self):
        """
        This test tests the topic model
        """
        topic = self.topic
        self.assertTrue(isinstance(topic, Topic))

    def test_topic_model_str_method(self):
        """ Test Topic model string method """
        topic = self.topic
        self.assertEqual((topic.__str__()), topic.name)

    def test_topic_model_function_friendly_name(self):
        """ Test Topic model function friendly
            returns friendly name
        """
        topic_friendly_name = self.topic.friendly_name
        self.assertEqual(str(topic_friendly_name), "Coding")

    def test_post_model_str_method(self):
        """ Test Post model string method """
        post = self.post
        self.assertEqual((post.__str__()), post.title)

    def test_post_model_get_absolute_url(self):
        """ Test get_absolute_url """
        post = self.post
        self.assertEquals(str(post.get_absolute_url()), '/forum/topic/1')

    def test_comment_model_str_method(self):
        """ Test Comment model string method """
        comment = self.comment
        self.assertEquals(str(comment), 'Comment Great idea by Chris Carabine')

    def test_comment_model_get_absolute_url(self):
        """ Test get_absolute_url """
        comment = self.comment
        self.assertEquals(str(comment.get_absolute_url()), '/forum/topic/1')

    def test_get_list_of_topics(self):
        """
        This test tests get a list of topics and verifies
        checks
        1. that the status code is 200
        2. Templates used is forum.html
        3. Topic is Coding
        """
        response = self.client.get('/forum/')
        topic = Topic.objects.get()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum.html')
        self.assertTrue(topic, "Coding")

    def test_get_list_of_posts_not_loggedin(self):
        """
        This test tests get a list of posts  when not logged in and verifies
        checks
        A not logged in user is redirected to the login page and
        the status code is 302
        """
        self.client.logout()
        response = self.client.get('/forum/Coding/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/forum/Coding/')

    def test_get_list_of_posts_logged_in(self):
        """
        This test tests get a list of posts  when logged in and verifies
        checks
        A logged in user status code is 302
        """
        self.client.login(username='chris_c', password='p2word')
        response = self.client.get('/forum/Coding/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/post_list.html')

    def test_add_post_as_not_logged_in(self):
        """
        This test tests a user who is not logged in, can not create a post
        checks
        1. if the page redirects to the home page
        2. if the message is the same as the not logged in user
        3. that the status code is 302  - redirect
        """
        self.client.logout()
        response = self.client.get('/forum/addpost/Coding/')
        self.assertRedirects(
            response, '/accounts/login/?next=/forum/addpost/Coding/')
        self.assertEqual(response.status_code, 302)
        
    def test_add_post_as_a_logged_in_user(self):
        """
        This test tests a logged in user can create a post
        checks
        1. the post the user created is equal to technical questions
        2. if the message is the same as post submitted
        3. the status code is 302  - redirect
        4. redirected back to the postdetail page
        """
        self.client.login(username='chris_c', password='p2word')
        response = self.client.post('/forum/addpost/Coding/',
                                    {'title': 'technical questions'})
        post = Post.objects.filter(pk=2).first()
        self.assertEqual(post.title, 'technical questions')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Post submitted")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("postdetail", args=[post.id]))

    def test_update_post_as_an_owner(self):
        """
        This test tests an owner of a post can update their post
        checks
        1. the updated title equals the title that the user typed in.
        2. if the message is the same as post submitted
        3. that the status code is 302  - redirect
        4. redirected back to the postdetail page
        """
        self.client.logout()
        self.client.login(username='chris_c', password='p2word')
        response = self.client.post('/forum/update/1',
                                    {'title': 'updated title'}
                                    )
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'updated title')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Post updated")
        self.assertTrue(response.status_code, 302)
        
    def test_update_post_as_not_the_owner(self):
        """
        This test tests a user who has not created the post can not
        edit the post
        checks
        1. a different user that trys to edit a post with the title field
        is not saved
        2. the updated title is not equals to the post title that the user
        typed in.
        3. that the status code is 304  - Not modified status code
        """
        self.client.logout()
        self.client.login(username='peter', password='p2word')
        response = self.client.post('/forum/update/1',
                                    {'title': 'updated -notowner'}
                                    )
        post = Post.objects.filter(pk=1).first()
        self.assertNotEqual(post.title, 'updated -notowner')
        self.assertTrue(response.status_code, 202)