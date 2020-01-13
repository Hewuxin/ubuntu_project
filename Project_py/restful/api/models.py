from django.db import models


class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.IntegerField(default=1)

    def book_to_dict(self):
        book_list = {'id': self.id, 'b_name': self.b_name, 'b_price': self.b_price}
        return book_list

    class Meta:
        db_table = "book"
