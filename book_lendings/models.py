from django.db import models
from django.utils import timezone
from book_copies.models import BookCopy


class BookLending(models.Model):
    STATUS_CHOICES = [
        ('avtive', 'Active'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]

    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='book_lending')
    borrower_name = models.CharField(max_length=100)
    borrower_email = models.EmailField()
    borrower_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now)
    returned_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    def __str__(self):
        return f"{self.borrower_name} book: {self.book_copy}"
