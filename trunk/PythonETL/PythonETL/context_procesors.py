def count_pendings(request,id1):
    badge_pendings=Job.objects.filter(status='TO_REVIEW').count()
    return badge_pendings