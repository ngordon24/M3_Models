from django.test import TestCase
from django.test import TestCase
from .models import Item
from app import models

# Create your tests here.


# Create your tests here.
class TestItem_test_cases(TestCase):
    def test_item_creation(self):
        item1 = models.make_item("Vase")
        item1.save()
        self.assertEqual(Item.objects.count(), 1)

    def test_read_all_items(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()

        items = models.read_all_items()
        title = [items.title for items in items]
        self.assertEqual(len(title), 1)

    def test_delete_item(self):
        D = Item(title="Vase")
        D.save()

        models.delete_item("Vase")
        items = Item.objects.all()
        self.assertEqual(len(items), 0)

    def test_update_item(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        models.update_item(Item.title, "Vase: Blue")
        Item1.save()

        self.assertEqual(Item1.title, "Vase: Blue")

    def test_read_by_title(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        Item_return = models.read_item_by_title("Vase")
        self.assertEqual(Item_return.title, "Vase")

    def test_filtered_search(self):
        Item1 = Item.objects.create(title="Vase")
        Item1.save()
        Item_return = models.item_filter("Vase")
        self.assertEqual(Item_return[0].title, "Vase")
