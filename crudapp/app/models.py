from django.db import models


# Create your models here.
class Item(models.Model):
    Item = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# create item
def make_item(title):
    Item = Item(title=title)
    Item.save()


# read all items
def read_all_items():
    return Item.objects.all()


# read filtered items
def item_filter(title):
    return Item.objects.filter(title=title)


# reads by unique identifier(title)
def read_item_by_title(title):
    return Item.objects.get(title=title)


# updates item name
def update_item(old_title, new_title):
    Item = Item.objects.get(title=old_title)
    Item.title = new_title
    Item.save()


# deletes item
def delete_item(title):
    D = Item.objects.filter(title=title)
    D.delete()
