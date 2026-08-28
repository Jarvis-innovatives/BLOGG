from django.db import models
from django.utils.text import slugify

class AboutMe(models.Model):
    kicker = models.CharField(max_length=100, default='~ Chapter I ~')
    title = models.CharField(max_length=200, default='About Me')
    image = models.CharField(max_length=255, default='banner-network.jpg', blank=True)
    image_file = models.ImageField(upload_to='about_images/', blank=True, null=True, help_text="Upload photo from your device")
    paragraph_1 = models.TextField(
        default="My name is Jarvis Lameck Magira, an aspiring technology professional and digital innovator currently pursuing my studies at the Dar es Salaam Institute of Technology (DIT). I am passionate about information technology, networking, software development, and creating innovative digital solutions that address real-world challenges."
    )
    paragraph_2 = models.TextField(
        default="Throughout my academic and professional journey, I have gained valuable experience providing IT support and solving technical issues at the Tanzania Communications Regulatory Authority (TCRA), TRA, and other organizations — strengthening my skills in troubleshooting, network administration, and system support."
    )
    paragraph_3 = models.TextField(
        default="As a Cisco Certified Network Associate (CCNA), I have a strong foundation in computer networking, network security, and infrastructure management. I am also a mobile application developer dedicated to building solutions that improve efficiency, accessibility, and user experience."
    )
    paragraph_4 = models.TextField(
        default="I am the creator of CoverPage — a digital platform that helps students generate professional academic cover pages quickly and easily. My vision is to keep innovating, advance cybersecurity awareness, and contribute to the growth of the technology sector in Tanzania and beyond."
    )
    quote = models.CharField(
        max_length=255,
        default="“I believe technology has the power to transform lives.”"
    )

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    @property
    def get_image_url(self):
        if self.image_file:
            try:
                return self.image_file.url
            except Exception:
                pass
        if self.image:
            if self.image.startswith('/') or self.image.startswith('http'):
                return self.image
            return f"/static/images/{self.image}"
        return "/static/images/banner-network.jpg"

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    TAG_CHOICES = [
        ('Networking', 'Networking'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Mobile', 'Mobile Apps'),
        ('Career', 'Career & IT Support'),
        ('Projects', 'Projects'),
        ('Mindset', 'Mindset'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='Networking')
    date_display = models.CharField(max_length=50, default='May 2026')
    read_time = models.CharField(max_length=50, default='5 min read')
    summary = models.TextField()
    content_json = models.JSONField(
        default=list,
        help_text="Structured article content as list or dict uploaded by admin."
    )
    featured_image = models.CharField(max_length=255, default='banner-network.jpg', blank=True)
    image_file = models.ImageField(upload_to='blog_banners/', blank=True, null=True, help_text="Upload banner image from your device")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def get_image_url(self):
        if self.image_file:
            try:
                return self.image_file.url
            except Exception:
                pass
        if self.featured_image:
            if self.featured_image.startswith('/') or self.featured_image.startswith('http'):
                return self.featured_image
            return f"/static/images/{self.featured_image}"
        return "/static/images/banner-network.jpg"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.tag})"


class Certificate(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    image_file = models.ImageField(upload_to='cert_images/', blank=True, null=True, help_text="Upload certificate image from your device")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    @property
    def get_image_url(self):
        if self.image_file:
            try:
                return self.image_file.url
            except Exception:
                pass
        if self.image:
            if self.image.startswith('/') or self.image.startswith('http'):
                return self.image
            return f"/static/images/{self.image}"
        return "/static/images/ccna 1.png"

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, default='Core Skill')
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True)
    image_file = models.ImageField(upload_to='skills_images/', blank=True, null=True, help_text="Upload skill image from your device")
    accent = models.CharField(max_length=50, default='var(--color-burgundy)')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    @property
    def get_image_url(self):
        if self.image_file:
            try:
                return self.image_file.url
            except Exception:
                pass
        if self.image:
            if self.image.startswith('/') or self.image.startswith('http'):
                return self.image
            return f"/static/images/{self.image}"
        return "/static/images/banner-network.jpg"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    features = models.JSONField(default=list)
    image = models.CharField(max_length=255, blank=True)
    image_file = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="Upload project screenshot/image from your device")
    link = models.URLField(blank=True, null=True)

    @property
    def get_image_url(self):
        if self.image_file:
            try:
                return self.image_file.url
            except Exception:
                pass
        if self.image:
            if self.image.startswith('/') or self.image.startswith('http'):
                return self.image
            return f"/static/images/{self.image}"
        return "/static/images/coverpage-mockup.jpg"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
