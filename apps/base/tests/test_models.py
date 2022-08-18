from django.test import TestCase

from apps.base.models import Post, KeyWord


class PostTestCase(TestCase):

    def setUp(self):
        KeyWord.objects.create(name="key1")

        Post.objects.create(
            title="name1",
            subtitle="sub1",
            type_post=1,
            content="long big content",
            status=2,
        )

    def test_name_object(self):
        p = Post.objects.get(title="name1")
        k = KeyWord.objects.get(name="key1")
        self.assertEqual(p.__str__(), "name1")
        self.assertEqual(k.__str__(), "key1")


    def test_add_keywork_to_post_object(self):
        p = Post.objects.get(title="name1")
        k = KeyWord.objects.get(name="key1")
        p.keyword.add(k)