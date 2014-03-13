from tastypie import fields
from tastypie.resources import ModelResource
from finalapp.models import Employer, MainUser, Worker, Category, Tag, JobPost, Status, Job, WorkerReview, \
    EmployerReview


class UserResource(ModelResource):
    class Meta:
        queryset = MainUser.objects.all()
        #name of the route/url:
        resource_name = "user"

class EmployerResource(ModelResource):
    #full=true gives me all the detail as well of the user
    user = fields.ToOneField(UserResource, 'user', full=True)
    class Meta:
        queryset = Employer.objects.all()
        #name of the route/url:
        resource_name = "employer"

class WorkerResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', full=True)
    class Meta:
        queryset = Worker.objects.all()
        #name of the route/url:
        resource_name = "worker"

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        #name of the route/url:
        resource_name = "category"

class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        #name of the route/url:
        resource_name = "tag"

class JobPostResource(ModelResource):
    category = fields.ToManyField(CategoryResource, 'category', full=True)
    tag = fields.ManyToManyField(TagResource, 'tag', full=True)
    employer = fields.ToManyField(EmployerResource, 'employer', full=True)
    workers = fields.ManyToManyField(WorkerResource, 'workers', full=True)

    class Meta:
        queryset = JobPost.objects.all()
        #name of the route/url:
        resource_name = "ad"

class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        #name of the route/url:
        resource_name = "status"

class JobResource(ModelResource):
    status = fields.ToManyField(StatusResource, 'status', full=True)

    class Meta:
        queryset = Job.objects.all()
        #name of the route/url:
        resource_name = "job"

class WorkerReviewResource(ModelResource):
    job = fields.ToOneField(JobResource, 'job', full=True)
    class Meta:
        queryset = WorkerReview.objects.all()
        #name of the route/url:
        resource_name = "workerfeeback"


class EmployerReviewResource(ModelResource):
    job = fields.ToOneField(JobResource, 'job', full=True)

    class Meta:
        queryset = EmployerReview.objects.all()
        #name of the route/url:
        resource_name = "employerfeedback"

