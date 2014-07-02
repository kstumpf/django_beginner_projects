from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404
from django.test import TestCase

from ..models import Post
# It is slower to create instances of your View class from tests.


class BlogViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.live_post = self.create_post()
        self.draft_post = self.create_post(title='Draft Post',
            published=False)

    def create_post(self, title='Test Blog Post', published=True):
        return Post.objects.create(
            title=title,
            author=self.user,
            published=published
        )
    
    def test_list_view(self):
        # blog:list is our url route name.
        url = reverse('blog:list')
        req = self.client.get(url)
#        post_url = reverse('blog:detail',
#            kwargs={'slug': self.live_post.slug})
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'blog/post_list.html')
        self.assertIn(self.live_post.title, req.rendered_content)
        self.assertIn(self.live_post.get_absolute_url(), 
            req.rendered_content)

    def test_detail_view(self):
        url = reverse('blog:detail', 
            kwargs={'slug': self.live_post.slug})
        req = self.client.get(url)
        self.assertEqual(req.status_code, 200)
        self.assertTemplateUsed(req, 'blog/post_detail.html')
        self.assertIn(self.live_post.title, req.rendered_content)
        self.assertIn(reverse('blog:list'), req.rendered_content)
        
    # We're expecting this one to fail!
    def test_draft_view(self):
        url = self.draft_post.get_absolute_url()
        # Tests run with debug equal to false, so it expects to find a 404 template.
#        with self.assertRaises(Http404):
#            self.client.get(url)
        req = self.client.get(url)
        # We still haven't created our template.
        self.assertEqual(req.status_code, 404)
