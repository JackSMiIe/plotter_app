from django.db import models

class Order(models.Model):
    PHONE_CHOICES = [
        ('iPhone', 'iPhone'),
        ('Samsung', 'Samsung'),
        ('Xiaomi', 'Xiaomi'),
        ('Other', 'Other'),
    ]

    SERVICE_CHOICES = [
        ('screen', 'Экран'),
        ('case', 'Корпус'),
        ('kit', 'Комплект'),
        ('repair', 'Ремонт'),
    ]

    full_name = models.CharField("ФИО", max_length=255)
    phone_number = models.CharField("Номер телефона", max_length=20)  # убрали primary_key
    phone_model = models.CharField("Модель телефона", max_length=50, choices=PHONE_CHOICES)
    service = models.CharField("Услуга", max_length=20, choices=SERVICE_CHOICES)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"

