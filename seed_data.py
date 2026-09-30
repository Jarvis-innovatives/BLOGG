import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio_app.models import AboutMe, BlogPost, Certificate, Skill, Project

def seed():
    print("Seeding database...")

    # Create Superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'jarvismagira@gmail.com', 'admin123')
        print("Created superuser: admin / admin123")
    else:
        print("Superuser admin already exists.")

    # Seed About Me
    AboutMe.objects.all().delete()
    AboutMe.objects.create(
        kicker="~ Chapter I ~",
        title="About Me",
        image="banner-network.jpg",
        paragraph_1="My name is Jarvis Lameck Magira, an aspiring technology professional and digital innovator currently pursuing my studies at the Dar es Salaam Institute of Technology (DIT). I am passionate about information technology, networking, software development, and creating innovative digital solutions that address real-world challenges.",
        paragraph_2="Throughout my academic and professional journey, I have gained valuable experience providing IT support and solving technical issues at the Tanzania Communications Regulatory Authority (TCRA), TRA, and other organizations — strengthening my skills in troubleshooting, network administration, and system support.",
        paragraph_3="As a Cisco Certified Network Associate (CCNA), I have a strong foundation in computer networking, network security, and infrastructure management. I am also a mobile application developer dedicated to building solutions that improve efficiency, accessibility, and user experience.",
        paragraph_4="I am the creator of CoverPage — a digital platform that helps students generate professional academic cover pages quickly and easily. My vision is to keep innovating, advance cybersecurity awareness, and contribute to the growth of the technology sector in Tanzania and beyond.",
        quote="“I believe technology has the power to transform lives.”"
    )
    print("Seeded About Me.")

    # Seed Certificates
    Certificate.objects.all().delete()
    Certificate.objects.create(
        title="Cisco CCNA",
        subtitle="Routing, switching & network fundamentals",
        image="ccna 1.png",
        order=1
    )
    Certificate.objects.create(
        title="Cisco Certified Network Associate",
        subtitle="Validated knowledge for modern enterprise networks",
        image="cisco 1.png",
        order=2
    )
    print("Seeded CCNA Certificates.")

    # Seed Project
    Project.objects.all().delete()
    Project.objects.create(
        title="CoverPage",
        subtitle="Digital Cover Page Generator",
        description="CoverPage is a modern digital platform designed to simplify and automate the process of creating academic cover pages for students across universities.",
        features=[
            "Fast & automated cover page generation",
            "Clean, professional academic formatting",
            "User-friendly interface for students",
            "Trusted across multiple universities"
        ],
        image="Create Coverpage Online Free – Coverpage Maker - Google Chrome 25_06_2026 12_16_05.png",
        link="https://coverpage.co.tz"
    )
    print("Seeded CoverPage Project.")

    # Seed Expanded Skills
    Skill.objects.all().delete()
    skills_data = [
        ("Software Development", "Full-Stack & Web", "Building robust, user-centric web and mobile applications with Python, Django, React, TypeScript, and modern REST APIs.", "banner-mobile.jpg", "var(--color-royal)", 1),
        ("Networking & Routing", "Cisco CCNA", "Configuring, troubleshooting, and securing enterprise network infrastructure (CCNA).", "banner-network.jpg", "var(--color-emerald)", 2),
        ("Cybersecurity Shield", "Cyber Defense", "Hardening systems, threat mitigation, security policy implementation, and security awareness.", "banner-cyber.jpg", "var(--color-burgundy)", 3),
        ("Mobile Solutions", "Mobile Development", "Crafting accessible Android applications that solve real student and business problems.", "banner-mobile.jpg", "var(--color-gilded-deep)", 4),
        ("IT Infrastructure & Support", "TCRA & TRA Experience", "Hands-on IT technical support, hardware troubleshooting, and system administration.", "banner-server.jpg", "var(--color-burgundy)", 5),
        ("Database & Data Systems", "Database & Data", "Relational database design, SQL optimization, data integrity, and automated backups.", "banner-server.jpg", "var(--color-royal)", 6),
    ]
    for title, cat, desc, img, accent, order in skills_data:
        Skill.objects.create(
            title=title,
            category=cat,
            description=desc,
            image=img,
            accent=accent,
            order=order
        )
    print("Seeded Expanded Skills.")

    # Seed Blog Posts
    BlogPost.objects.all().delete()
    posts_data = [
        {
            "slug": "subnetting-without-tears",
            "tag": "Networking",
            "title": "Subnetting Without Tears",
            "date_display": "May 2026",
            "read_time": "7 min read",
            "featured_image": "banner-network.jpg",
            "summary": "A CCNA-inspired walkthrough that turns subnetting from a nightmare into a five-minute calculation you can do in your head.",
            "content_json": [
                {"type": "paragraph", "text": "Subnetting is the skill that separates network technicians from network engineers. Yet, for most students, it is the single scariest topic in the CCNA syllabus. The good news? With a few simple patterns, subnetting becomes almost mechanical."},
                {"type": "heading", "text": "Why subnetting matters"},
                {"type": "paragraph", "text": "Every device on an IP network needs a unique address, but addresses alone are not enough. We also need a way to divide a network into smaller, manageable broadcast domains. That is exactly what subnetting does."},
                {"type": "heading", "text": "The magic of the powers of two"},
                {"type": "paragraph", "text": "At its heart, subnetting is about binary. Borrowing one host bit doubles the number of networks and halves the hosts per network. Borrowing two bits gives four networks, three bits gives eight, and so on. Memorize 2, 4, 8, 16, 32, 64, 128, 256 and you already own half the exam."},
                {"type": "quote", "text": "Subnetting is not math. It is pattern recognition dressed up as math."},
                {"type": "heading", "text": "A practical example"},
                {"type": "paragraph", "text": "Suppose you are given 192.168.1.0/24 and asked to create four subnets. You need to borrow two bits, giving you a /26 mask. The block size in the interesting octet is 256 - 192 = 64."},
                {"type": "heading", "text": "My daily advice"},
                {"type": "list", "text": "Quick habits that make subnetting faster", "items": [
                    "Practice with a subnetting app for five minutes every morning.",
                    "Always write the mask, block size, and network addresses before answering.",
                    "Use real-world scenarios — VLANs, branch offices, wireless guest networks.",
                    "Teach someone else; teaching exposes the gaps in your own understanding."
                ]},
            ]
        },
        {
            "slug": "five-habits-that-keep-you-safe-online",
            "tag": "Cybersecurity",
            "title": "Five Habits That Keep You Safe Online",
            "date_display": "Apr 2026",
            "read_time": "5 min read",
            "featured_image": "banner-cyber.jpg",
            "summary": "No fancy tools required. These five everyday habits protect your digital life from the majority of modern cyberattacks.",
            "content_json": [
                {"type": "paragraph", "text": "Cybersecurity is often painted as a world of hackers in hoodies and complex code. In reality, most breaches happen because of simple, preventable mistakes. Here are five habits that will keep you safer than most."},
                {"type": "heading", "text": "1. Use a password manager"},
                {"type": "paragraph", "text": "Reusing passwords is like using one key for every lock in your life. A password manager generates unique, strong passwords and remembers them so you do not have to."},
                {"type": "heading", "text": "2. Enable two-factor authentication"},
                {"type": "paragraph", "text": "Passwords can be stolen. A second factor — an app code, a hardware key, or a biometric check — makes stolen passwords far less useful."},
                {"type": "heading", "text": "3. Think before you click"},
                {"type": "paragraph", "text": "Phishing emails are getting smarter. Before clicking a link, check the sender address, hover to inspect the URL, and when in doubt, open the site directly."},
                {"type": "heading", "text": "4. Keep software updated"},
                {"type": "paragraph", "text": "Updates patch security holes. Enable automatic updates on your phone, laptop, and browsers."},
                {"type": "heading", "text": "5. Back up your data"},
                {"type": "paragraph", "text": "Follow the 3-2-1 rule: three copies of your data, on two different media, with one stored offsite or in the cloud."},
                {"type": "quote", "text": "Security is not a product; it is a process. The best firewall is a careful mind."}
            ]
        },
        {
            "slug": "designing-apps-users-actually-open",
            "tag": "Mobile",
            "title": "Designing Apps Users Actually Open",
            "date_display": "Mar 2026",
            "read_time": "6 min read",
            "featured_image": "banner-mobile.jpg",
            "summary": "Building a great app is only half the battle. Here is how to make users want to return to it every day.",
            "content_json": [
                {"type": "paragraph", "text": "Thousands of mobile apps are published every month, but only a handful become part of someone's daily routine. The difference is rarely the technology; it is the design. Here is what I have learned from building CoverPage."},
                {"type": "heading", "text": "Solve one problem clearly"},
                {"type": "paragraph", "text": "Users do not download apps for features. They download them to solve problems. If your app can remove a single frustration in under a minute, people will remember it."},
                {"type": "heading", "text": "Respect the user's time"},
                {"type": "paragraph", "text": "Every screen should ask for the minimum information needed. Every loading state should be short."},
                {"type": "quote", "text": "The best app is not the one with the most features. It is the one the user cannot imagine living without."}
            ]
        },
        {
            "slug": "from-it-intern-to-network-professional",
            "tag": "Career",
            "title": "From IT Intern to Network Professional",
            "date_display": "Feb 2026",
            "read_time": "8 min read",
            "featured_image": "banner-server.jpg",
            "summary": "Lessons from my internships at TCRA, TRA, and beyond — and how hands-on experience beats classroom theory.",
            "content_json": [
                {"type": "paragraph", "text": "Classroom theory gives you the vocabulary, but internships give you the story. My time at the Tanzania Communications Regulatory Authority (TCRA) and Tanzania Revenue Authority (TRA) taught me more about real-world IT than any textbook could."},
                {"type": "heading", "text": "What TCRA taught me"},
                {"type": "paragraph", "text": "At TCRA, I saw how national communication infrastructure is monitored, maintained, and protected. I learned that uptime is not a feature; it is a promise."},
                {"type": "heading", "text": "What TRA taught me"},
                {"type": "paragraph", "text": "At TRA, I worked alongside IT support teams handling real users with real deadlines. The biggest lesson? People do not remember the technical fix; they remember how you treated them while fixing it."},
                {"type": "quote", "text": "Your degree opens the door. Your attitude and experience keep you in the room."}
            ]
        },
        {
            "slug": "building-coverpage-one-student-at-a-time",
            "tag": "Projects",
            "title": "Building CoverPage, One Student at a Time",
            "date_display": "Jan 2026",
            "read_time": "6 min read",
            "featured_image": "coverpage-mockup.jpg",
            "summary": "The story behind CoverPage — from a simple idea to a platform used by students in multiple universities.",
            "content_json": [
                {"type": "paragraph", "text": "CoverPage started as a frustration. I saw students wasting time formatting academic cover pages instead of focusing on their actual work. I believed there had to be a faster, cleaner way."},
                {"type": "heading", "text": "The growth"},
                {"type": "paragraph", "text": "What began as a tool for my classmates spread to other universities. Today, CoverPage is used by students at DIT, UDSM, and beyond."},
                {"type": "quote", "text": "Build something that solves your own problem. If it works for you, it will probably work for others."}
            ]
        },
        {
            "slug": "manifestation-and-the-tech-journey",
            "tag": "Mindset",
            "title": "Manifestation and the Tech Journey",
            "date_display": "Dec 2025",
            "read_time": "4 min read",
            "featured_image": "hero-portrait.jpg",
            "summary": "Why patience, preparation, and trust in the process matter more than chasing every opportunity.",
            "content_json": [
                {"type": "paragraph", "text": "In the tech world, it is easy to feel like you are always behind. New frameworks, new certifications, new opportunities. The pressure to chase everything can be overwhelming."},
                {"type": "heading", "text": "Stop chasing, start becoming"},
                {"type": "paragraph", "text": "Manifestation is not magic. It is the quiet work of becoming ready for what you want. If you want better opportunities, build better skills."},
                {"type": "quote", "text": "The thing happens at the point you stop chasing it."}
            ]
        }
    ]

    for p_data in posts_data:
        BlogPost.objects.create(**p_data)

    print("Seeded Blog Posts successfully!")

if __name__ == '__main__':
    seed()
