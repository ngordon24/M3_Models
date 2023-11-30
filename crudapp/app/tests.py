from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Item


# Create your tests here.
class TestItem_test_cases(TestCase):
    def test_item_creation(self):
        item1 = Item(title="Vase")
        item1.save()
        self.assertEqual(Item.objects.count(), 1)

    def test_read_all_items(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()

        items = Item.objects.all()
        title = [items.title for items in items]
        self.assertEqual(len(title), 1)

    def test_delete_item(self):
        D = Item(title="Vase")
        D.save()

        D.delete()
        items = Item.objects.all()
        self.assertEqual(len(items), 0)

    def test_update_item(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        Item1.title = "Vase: Blue"
        Item1.save()

        self.assertEqual(Item1.title, "Vase: Blue")

    def test_read_by_title(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        Item_return = Item.objects.get(title="Vase")
        self.assertEqual(Item_return.title, "Vase")

    def test_filtered_search(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        Item_return = Item.objects.filter(title="Vase")
        self.assertEqual(Item_return[0].title, "Vase")
