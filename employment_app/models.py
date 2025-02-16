from django.db import models
from django.conf import settings

class JobOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobSearch(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    searcher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# Informations professionnelles et éducatives:
#     Emploi actuel
#     Entreprises précédentes
#     Secteur d'activité
#     Formation (écoles, universités, diplômes)


# User = get_user_model()


# CANDIDATS
class CandidateProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="candidate_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)  # Courte description du profil
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    visibility = models.BooleanField(default=True)  # Profil public ou privé
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Experience(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="experiences")
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Null si encore en poste
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="educations")
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.school}"

class Skill(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(1, "Beginner"), (2, "Intermediate"), (3, "Advanced"), (4, "Expert")])

    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"

class Language(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="languages")
    name = models.CharField(max_length=100)
    level = models.IntegerField(choices=[(1, "Basic"), (2, "Intermediate"), (3, "Fluent"), (4, "Native")])

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"

class Certification(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} from {self.organization}"

class Reference(models.Model):
    candidate = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name="references")
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.relationship})"

# # EMPLOYERS


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    headquarters = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class JobOpportunity(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
    ]

    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="job_offers")
    location = models.CharField(max_length=255)
    remote = models.BooleanField(default=False)
    job_type = models.CharField(max_length=50, choices=[("full_time", "Full Time"), ("part_time", "Part Time"), ("contract", "Contract"), ("internship", "Internship")])
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, default="USD")
    benefits = models.TextField(blank=True, null=True)  # Ex: Assurance, Bonus, etc.
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="posted_jobs")  # L'utilisateur qui a posté l'offre
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class RequiredSkill(models.Model):
    job = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, related_name="required_skills")
    skill_name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(1, "Basic"), (2, "Intermediate"), (3, "Advanced"), (4, "Expert")])

    def __str__(self):
        return f"{self.skill_name} ({self.get_proficiency_display()})"

class RequiredLanguage(models.Model):
    job = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, related_name="required_languages")
    language_name = models.CharField(max_length=100)
    level = models.IntegerField(choices=[(1, "Basic"), (2, "Intermediate"), (3, "Fluent"), (4, "Native")])

    def __str__(self):
        return f"{self.language_name} ({self.get_level_display()})"

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, related_name="applications")
    candidate = models.ForeignKey("CandidateProfile", on_delete=models.CASCADE, related_name="job_applications")
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    cover_letter = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.user.username} applied for {self.job.title}"