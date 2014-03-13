from django.contrib.auth.models import User
from django.db import models


#need to review MainUser
class MainUser(User):
    def is_employer(self):
        return self.employer.exists()

    def is_worker(self):
        return self.worker.exists()


class Employer(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    company_name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField(blank=False, unique=True)

    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=30)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30)

    latitude = models.PositiveSmallIntegerField(null=True, blank=True)
    longitude = models.PositiveSmallIntegerField(null=True, blank=True)

    description = models.TextField(blank=True)

    company_logo = models.ImageField(upload_to="company_logos", null=True, blank=True)
    profile_photo = models.ImageField(upload_to="employer_images", null=True, blank=True)

    user = models.OneToOneField(User, related_name="employer")

    def __unicode__(self):
        return self.username




class Worker(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    phone_number = models.PositiveIntegerField(blank=False, unique=True)

    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip = models.CharField(max_length=30)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30)

    latitude = models.PositiveSmallIntegerField(null=True, blank=True)
    longitude = models.PositiveSmallIntegerField(null=True, blank=True)

    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    date_of_birth = models.DateField(blank=True)

    bio = models.TextField(blank=True)

    profile_photo = models.ImageField(upload_to="worker_images", null=True, blank=True)

    user = models.OneToOneField(User, related_name="worker")

    def __unicode__(self):
        return self.username



class Category(models.Model):
    HOSPITALITY = 'HO'
    RETAIL_SALES = 'RE'
    EVENT_MGMT_PROMO = 'EV'
    OFFICE = 'OF'
    CATEGORY_CHOICES = (
        ('HO', 'Hospitality'),
        ('RE', 'Retail/Sales'),
        ('EV', 'Event Mgmt/Promo'),
        ('OF', 'Office'),
    )

    name = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    POPULAR = 'PO'
    TAG_CHOICES = (
        ('PO', 'Popular'),
    )

    name = models.CharField(max_length=2, choices=TAG_CHOICES)

    def __unicode__(self):
        return self.name



class JobPost(models.Model):
    active = models.BooleanField(default=True)

    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, null=True)
    employer = models.ForeignKey(Employer)
    workers = models.ManyToManyField(Worker, through='Job', null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=40)
    hourly_rate = models.PositiveSmallIntegerField()
    weekly_hours = models.PositiveSmallIntegerField()

    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    state = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30)

    latitude = models.PositiveSmallIntegerField(blank=True)
    longitude = models.PositiveSmallIntegerField(blank=True)

    people_needed = models.PositiveSmallIntegerField()

    description = models.TextField()
    requirements = models.TextField() #TODO replace by tags for ratings, analytics and reco

    def __unicode__(self):
        return self.title


class Status(models.Model):
    APPLIED = 'AP'
    CONFIRMED = 'CF'
    COMPLETED = 'CT'
    REVIEWED_BY_WORKER = 'RW'
    REVIEWED_BY_EMPLOYER = 'RE'

    STATUS_CHOICES = (
        ('AP', 'Applied'),
        ('CF', 'Confirmed'),
        ('CT', 'Completed'),
        ('RW', 'Reviewed by worker'),
        ('RE', 'Reviewed by employer'),
    )

    name = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    status = models.ForeignKey(Status)

    worker = models.ForeignKey(Worker)
    job_post = models.ForeignKey(JobPost)

    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)




class WorkerReview(models.Model):
    job = models.OneToOneField(Job)

    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    WSHOW = (
        ('SH', 'Show'),
        ('NS', 'No show'),
    )

    worker_show = models.CharField(max_length=2, choices=WSHOW)
    worker_24hnotice = models.BooleanField(default=False)
    worker_job_completed = models.BooleanField(default=False)
    worker_hours_worked = models.PositiveSmallIntegerField()
    worker_responsiveness = models.PositiveSmallIntegerField()
    worker_performance_quality = models.PositiveSmallIntegerField()
    worker_performance_speed = models.PositiveSmallIntegerField()
    worker_punctuality = models.PositiveSmallIntegerField()
    worker_language = models.PositiveSmallIntegerField()
    worker_friendliness = models.PositiveSmallIntegerField()
    worker_team_interaction = models.PositiveSmallIntegerField()
    worker_presentation = models.PositiveSmallIntegerField()
    worker_notes = models.TextField()



class EmployerReview(models.Model):
    job = models.OneToOneField(Job)

    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    ESHOW = (
        ('SH', 'Job went ahead as planned'),
        ('NS', 'Sent home/no-one at location'),
    )
    employer_show = models.CharField(max_length=2, choices=ESHOW)
    employer_24hnotice = models.BooleanField(default=False)
    employer_confirm_job_completed = models.BooleanField(default=False)
    employer_responsiveness = models.PositiveSmallIntegerField()
    employer_friendliness = models.PositiveSmallIntegerField()
    employer_accurate_jobdescription = models.PositiveSmallIntegerField()
    employer_punctual_payment = models.BooleanField(default=True)
    employer_notes = models.TextField()
