from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    branch = models.CharField(max_length=50, choices=[
        ('Adayar', 'Adayar'),
        ('Alwarpet', 'Alwarpet'),
        ('Ambattur', 'Ambattur'),
        ('Anna Nagar', 'Anna Nagar'),
        ('Ashok Nagar', 'Ashok Nagar'),
        ('Avadi', 'Avadi'),
        ('Ayanavaram', 'Ayanavaram'),
        ('Bazullah Road', 'Bazullah Road'),
        ('Besant Nagar', 'Besant Nagar'),
        ('Chrompet', 'Chrompet'),
        ('Egmore', 'Egmore'),
        ('Kanchipuram', 'Kanchipuram'),
        ('Kanchi Gandhi Road', 'Kanchi Gandhi Road'),
        ('Karapakkam', 'Karapakkam'),
        ('Kathipara', 'Kathipara'),
        ('Kelambakkam', 'Kelambakkam'),
        ('Korattur', 'Korattur'),
        ('Luz New', 'Luz New'),
        ('Madipakkam', 'Madipakkam'),
        ('Medavakkam', 'Medavakkam'),
        ('Mogappair', 'Mogappair'),
        ('Mylapore', 'Mylapore'),
        ('Nanganallur', 'Nanganallur'),
        ('Nanganallur West', 'Nanganallur West'),
        ('Nungambakkam', 'Nungambakkam'),
        ('Perambur', 'Perambur'),
        ('Porur', 'Porur'),
        ('Pondicherry', 'Pondicherry'),
        ('Purasai Palace', 'Purasai Palace'),
        ('Saidapet', 'Saidapet'),
        ('Tambaram West', 'Tambaram West'),
        ('Thiruvallur', 'Thiruvallur'),
        ('Thiruvanmiyur', 'Thiruvanmiyur'),
        ('Thiruvannamalai', 'Thiruvannamalai'),
        ('Thuraipakkam', 'Thuraipakkam'),
        ('Triplicane', 'Triplicane'),
        ('Usman Road', 'Usman Road'),
        ('Vadapalani', 'Vadapalani'),
        ('Valasaravakkam', 'Valasaravakkam'),
        ('Velachery', 'Velachery'),
        ('Villivakkam', 'Villivakkam'),
        ('VN Road T.Nagar', 'VN Road T.Nagar'),
        ('Venus Colony', 'Venus Colony'),
        ('West Mambalam', 'West Mambalam'),
        ('Chennai Airport', 'Chennai Airport'),
    ])
    value_for_money = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Satisfied', 'Satisfied'),
        ('To be improved', 'To be improved')
    ])
    packaging = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Satisfied', 'Satisfied'),
        ('To be improved', 'To be improved')
    ])
    quality = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Satisfied', 'Satisfied'),
        ('To be improved', 'To be improved')
    ])
    display = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Satisfied', 'Satisfied'),
        ('To be improved', 'To be improved')
    ])
    variety = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Satisfied', 'Satisfied'),
        ('To be improved', 'To be improved')
    ])
    comments = models.TextField(blank=True, null=True)
    employee_name_id = models.CharField(max_length=100)
    voice_message_base64 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
