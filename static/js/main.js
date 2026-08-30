document.addEventListener('DOMContentLoaded', function () {
  // Mobile Off-Canvas Drawer Navigation
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const mobileOverlay = document.getElementById('mobile-drawer-overlay');
  const mobileClose = document.getElementById('mobile-drawer-close');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');

  function openMobileDrawer() {
    if (mobileDrawer) mobileDrawer.classList.add('active');
    if (mobileOverlay) mobileOverlay.classList.add('active');
    if (mobileToggle) mobileToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileDrawer() {
    if (mobileDrawer) mobileDrawer.classList.remove('active');
    if (mobileOverlay) mobileOverlay.classList.remove('active');
    if (mobileToggle) mobileToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openMobileDrawer);
  if (mobileClose) mobileClose.addEventListener('click', closeMobileDrawer);
  if (mobileOverlay) mobileOverlay.addEventListener('click', closeMobileDrawer);

  mobileLinks.forEach((link) => {
    link.addEventListener('click', function () {
      closeMobileDrawer();
    });
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('active')) {
      closeMobileDrawer();
    }
  });

  // Auto-close mobile menu on window resize to desktop
  window.addEventListener('resize', function () {
    if (window.innerWidth >= 768 && mobileDrawer && mobileDrawer.classList.contains('active')) {
      closeMobileDrawer();
    }
  });

  // Header Scroll State & Scroll-to-Top Button (Mobile Only)
  const mainHeader = document.getElementById('main-header');
  const scrollToTopBtn = document.getElementById('scroll-to-top');

  window.addEventListener('scroll', function () {
    const currentScroll = window.scrollY;

    if (mainHeader) {
      if (currentScroll > 20) {
        mainHeader.classList.add('scrolled');
      } else {
        mainHeader.classList.remove('scrolled');
      }
    }

    if (scrollToTopBtn) {
      if (currentScroll > 300 && window.innerWidth < 768) {
        scrollToTopBtn.classList.add('visible');
      } else {
        scrollToTopBtn.classList.remove('visible');
      }
    }
  });

  if (scrollToTopBtn) {
    scrollToTopBtn.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      });
    });
  }

  // IntersectionObserver ScrollSpy for Desktop Section Highlight
  const desktopNavLinks = document.querySelectorAll('#desktop-nav .nav-link');
  const sections = document.querySelectorAll('section[id]');

  if (sections.length > 0 && desktopNavLinks.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '-25% 0px -55% 0px',
      threshold: 0,
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const currentId = entry.target.getAttribute('id');
          desktopNavLinks.forEach((link) => {
            const href = link.getAttribute('href') || '';
            const sectionTarget = link.getAttribute('data-section') || (href.includes('#') ? href.split('#')[1] : '');
            if (sectionTarget === currentId) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
        }
      });
    }, observerOptions);

    sections.forEach((section) => observer.observe(section));
  }

  // Blog Page Functionality (Filter, Search, Sort)
  const tagButtons = document.querySelectorAll('.tag-btn');
  const searchInput = document.getElementById('blog-search');
  const sortSelect = document.getElementById('blog-sort');
  const blogGrid = document.getElementById('blog-posts-grid');

  let currentTag = 'All';
  let currentSearch = '';
  let currentSort = 'latest';

  function fetchPosts() {
    if (!blogGrid) return;

    const url = new URL(window.location.href);
    url.pathname = '/blog/';
    url.searchParams.set('tag', currentTag);
    url.searchParams.set('q', currentSearch);
    url.searchParams.set('sort', currentSort);
    url.searchParams.set('format', 'json');

    fetch(url, {
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
      .then((res) => res.json())
      .then((data) => {
        renderBlogPosts(data.posts);
      })
      .catch((err) => console.error('Error fetching posts:', err));
  }

  function renderBlogPosts(posts) {
    if (!blogGrid) return;

    if (!posts || posts.length === 0) {
      blogGrid.innerHTML = `
        <div class="col-span-full py-12 text-center">
          <p class="font-serif text-2xl text-stone-600">No journal entries match your criteria.</p>
          <button id="reset-filter-btn" class="mt-4 btn-secondary">Reset Filters</button>
        </div>
      `;
      const resetBtn = document.getElementById('reset-filter-btn');
      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          currentTag = 'All';
          currentSearch = '';
          currentSort = 'latest';
          if (searchInput) searchInput.value = '';
          tagButtons.forEach((b) => b.classList.remove('active'));
          if (tagButtons[0]) tagButtons[0].classList.add('active');
          fetchPosts();
        });
      }
      return;
    }

    blogGrid.innerHTML = posts
      .map(
        (post) => `
      <article class="group flex flex-col rounded-md overflow-hidden border border-[var(--color-gilded)]/40 bg-white/70 hover:shadow-xl transition duration-500">
        <div class="overflow-hidden h-52 relative">
          <img src="${post.img}" alt="${post.title}" loading="lazy" class="h-full w-full object-cover group-hover:scale-110 transition duration-700" />
          <span class="absolute top-3 left-3 rounded-full bg-[var(--color-burgundy)] px-3 py-1 text-xs font-serif text-[var(--color-parchment)] shadow">
            ${post.tag}
          </span>
        </div>
        <div class="flex flex-1 flex-col p-6">
          <div class="flex items-center gap-3 font-serif text-sm text-stone-600">
            <span>📅 ${post.date}</span>
            <span>•</span>
            <span>⏱️ ${post.read_time}</span>
          </div>
          <h2 class="font-display text-2xl font-bold mt-2 text-[var(--color-ink)] leading-snug">${post.title}</h2>
          <p class="font-serif mt-2 flex-1 text-stone-700 leading-relaxed text-[17px]">${post.summary}</p>
          <div class="mt-6 flex items-center justify-between">
            <a href="/blog/${post.slug}/" class="inline-flex items-center gap-2 font-serif italic text-[var(--color-burgundy)] font-semibold hover:underline">
              Read more &rarr;
            </a>
            <button class="quick-read-btn text-sm font-serif italic text-stone-600 hover:text-[var(--color-burgundy)]" data-slug="${post.slug}">
              ⚡ Quick Read
            </button>
          </div>
        </div>
      </article>
    `
      )
      .join('');

    // Attach Quick Read click handlers
    document.querySelectorAll('.quick-read-btn').forEach((btn) => {
      btn.addEventListener('click', function () {
        const slug = this.dataset.slug;
        const post = posts.find((p) => p.slug === slug);
        if (post) openBlogModal(post);
      });
    });
  }

  // Tag filter handler
  tagButtons.forEach((btn) => {
    btn.addEventListener('click', function () {
      tagButtons.forEach((b) => b.classList.remove('active'));
      this.classList.add('active');
      currentTag = this.dataset.tag || 'All';
      fetchPosts();
    });
  });

  // Search input handler with debounce
  let searchTimeout;
  if (searchInput) {
    searchInput.addEventListener('input', function () {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        currentSearch = this.value.trim();
        fetchPosts();
      }, 300);
    });
  }

  // Sort select handler
  if (sortSelect) {
    sortSelect.addEventListener('change', function () {
      currentSort = this.value;
      fetchPosts();
    });
  }

  // Modal Reader Logic
  const modalOverlay = document.getElementById('blog-modal-overlay');
  const modalBody = document.getElementById('blog-modal-body');
  const modalClose = document.getElementById('blog-modal-close');

  function renderContentHtml(content) {
    if (!content) return '';
    if (typeof content === 'object' && content !== null && Array.isArray(content.topics)) {
      return content.topics.map(t => `
        <div class="mb-6">
          <h3 class="font-display text-2xl font-bold text-[var(--color-burgundy)] mb-3">${t.topic}</h3>
          ${(t.subtopics || []).map(s => `
            <div class="mb-4 bg-white/70 p-4 rounded border border-[var(--color-gilded)]/30">
              <h4 class="font-display text-lg font-bold text-[var(--color-ink)] mb-1">✦ ${s.title}</h4>
              <p class="font-serif text-base text-stone-800 leading-relaxed">${s.explanation || s.text || ''}</p>
            </div>
          `).join('')}
        </div>
      `).join('');
    }
    if (Array.isArray(content)) {
      return content.map(block => {
        if (typeof block === 'string') return `<p class="font-serif text-lg leading-relaxed text-stone-800 mb-4">${block}</p>`;
        if (block.topic && Array.isArray(block.subtopics)) {
          return `
            <div class="mb-6">
              <h3 class="font-display text-2xl font-bold text-[var(--color-burgundy)] mb-3">${block.topic}</h3>
              ${block.subtopics.map(s => `
                <div class="mb-4 bg-white/70 p-4 rounded border border-[var(--color-gilded)]/30">
                  <h4 class="font-display text-lg font-bold text-[var(--color-ink)] mb-1">✦ ${s.title}</h4>
                  <p class="font-serif text-base text-stone-800 leading-relaxed">${s.explanation || s.text || ''}</p>
                </div>
              `).join('')}
            </div>
          `;
        }
        if (block.type === 'heading') return `<h3 class="font-display text-2xl font-bold text-[var(--color-burgundy)] mt-6 mb-2">${block.text}</h3>`;
        if (block.type === 'paragraph') return `<p class="font-serif text-lg leading-relaxed text-stone-800 mb-4">${block.text}</p>`;
        if (block.type === 'quote') return `<blockquote class="rounded-md border-l-4 border-[var(--color-gilded)] bg-stone-100 p-4 italic text-stone-800 my-4">“${block.text}”</blockquote>`;
        if (block.type === 'list' && block.items) {
          return `
            <div class="my-4">
              <p class="font-semibold text-stone-900 mb-2 font-serif text-lg">${block.text}</p>
              <ul class="list-disc ml-6 space-y-1 font-serif text-lg text-stone-800">
                ${block.items.map((it) => `<li>${it}</li>`).join('')}
              </ul>
            </div>
          `;
        }
        if (block.heading || block.title) return `<h3 class="font-display text-xl font-bold text-[var(--color-burgundy)] mt-4 mb-1">${block.heading || block.title}</h3><p class="font-serif text-lg leading-relaxed text-stone-800 mb-4">${block.text || block.explanation || ''}</p>`;
        return '';
      }).join('');
    }
    return '';
  }

  function openBlogModal(post) {
    if (!modalOverlay || !modalBody) return;

    let contentHtml = renderContentHtml(post.content);

    modalBody.innerHTML = `
      <div class="mb-6 overflow-hidden rounded-md border border-[var(--color-gilded)]/40 shadow-lg">
        <img src="${post.img}" alt="${post.title}" class="w-full h-64 object-cover" />
      </div>
      <div class="flex items-center gap-3 font-serif text-sm text-[var(--color-burgundy)]">
        <span class="rounded-full bg-[var(--color-burgundy)]/10 px-3 py-1 font-semibold">${post.tag}</span>
        <span>📅 ${post.date}</span>
        <span>⏱️ ${post.read_time}</span>
      </div>
      <h1 class="font-display text-4xl font-bold text-[var(--color-ink)] mt-3 leading-tight">${post.title}</h1>
      <div class="ornate-divider my-4"><span>✦</span></div>
      <p class="font-serif text-xl italic text-stone-600 mb-6">${post.summary}</p>
      <div class="article-body font-serif text-lg leading-relaxed">
        ${contentHtml}
      </div>
    `;

    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  if (modalClose) {
    modalClose.addEventListener('click', function () {
      if (modalOverlay) modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    });
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', function (e) {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  // Contact Form AJAX Handling
  const contactForm = document.getElementById('contact-form');
  const formFeedback = document.getElementById('contact-form-feedback');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const name = document.getElementById('contact-name')?.value;
      const email = document.getElementById('contact-email')?.value;
      const message = document.getElementById('contact-message')?.value;

      if (!name || !email || !message) {
        if (formFeedback) {
          formFeedback.innerHTML = '<span class="text-rose-400">Please fill out all fields.</span>';
        }
        return;
      }

      fetch('/api/contact/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, message }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === 'success') {
            if (formFeedback) {
              formFeedback.innerHTML = `<span class="text-emerald-400">✨ ${data.message}</span>`;
            }
            contactForm.reset();
          } else {
            if (formFeedback) {
              formFeedback.innerHTML = `<span class="text-rose-400">⚠️ ${data.message}</span>`;
            }
          }
        })
        .catch((err) => {
          if (formFeedback) {
            formFeedback.innerHTML = '<span class="text-rose-400">An unexpected error occurred.</span>';
          }
        });
    });
  }
});
