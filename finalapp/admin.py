from django.contrib import admin
from finalapp.models import Employer, Worker, Category, Tag, Status, Job, JobPost, WorkerReview, EmployerReview

admin.site.register(Employer)
admin.site.register(Worker)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Status)
admin.site.register(JobPost)
admin.site.register(Job)
admin.site.register(WorkerReview)
admin.site.register(EmployerReview)
