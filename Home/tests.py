from django.test import TestCase
from Home.models import BannerCards, Cards

class BannerCardsTestCase(TestCase):
    def setUp(self):
        BannerCards.objects.create(title="Test BannerCards", category="Test Category", content="Test Content", imageurl="Test Image URL", targetUrl="Test Target URL")

    def test_banner_cards(self):
        banner_card = BannerCards.objects.get(title="Test BannerCards")
        self.assertEqual(banner_card.category, "Test Category")
        self.assertEqual(banner_card.content, "Test Content")
        self.assertEqual(banner_card.imageurl, "Test Image URL")
        self.assertEqual(banner_card.targetUrl, "Test Target URL")


class CardsTestCase(TestCase):
    def setUp(self):
        Cards.objects.create(title="Test Cards", category="Test Category", imageurl="Test Image URL", targetUrl="Test Target URL")

    def test_cards(self):
        card = Cards.objects.get(title="Test Cards")
        self.assertEqual(card.category, "Test Category")
        self.assertEqual(card.imageurl, "Test Image URL")
        self.assertEqual(card.targetUrl, "Test Target URL")