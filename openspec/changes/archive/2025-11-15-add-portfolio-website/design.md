## Context
Building a personal portfolio website from scratch that serves as a professional brand platform. The site needs to balance aesthetics with performance, be SEO-friendly, and provide a great user experience across all devices. The architecture must support easy content updates and future scalability.

## Goals / Non-Goals

### Goals
- Create a fast, SEO-optimized website with Lighthouse score >90
- Implement a clean, minimal UI with dark mode support
- Build a scalable architecture for easy content management
- Ensure excellent mobile experience and responsive design
- Provide smooth animations and transitions for engagement
- Enable easy blog content authoring with markdown
- Implement robust contact form with spam protection

### Non-Goals
- Not building a full CMS (content managed via code/files initially)
- Not implementing user authentication for visitors (only admin if needed)
- Not building a complex e-commerce system
- Not supporting multiple languages initially (can be added later)

## Technical Decisions

### Frontend Architecture
- **Decision**: Use Next.js 14+ with App Router and TypeScript
- **Why**: Server-side rendering for SEO, excellent performance, built-in optimization, strong TypeScript support
- **Alternatives considered**: 
  - Gatsby: Less flexible for dynamic content
  - Pure React SPA: Poor SEO without SSR
  - Astro: Good option but less ecosystem support for complex interactions

### Styling Approach
- **Decision**: Tailwind CSS with custom design system
- **Why**: Utility-first approach enables rapid development, excellent performance, built-in responsive design
- **Custom tokens**: Define color palette, typography scale, spacing system in `tailwind.config.ts`
- **Color Palette**:
  - Light mode background: `#f3ede5` (warm beige)
  - Dark mode background: `#092757` (deep navy blue)
  - Accent green 1: `#86e5a1` (mint green)
  - Accent green 2: `#c5ffbc` (light lime green)
  - Additional colors derived from this palette for consistency
- **Alternatives considered**:
  - CSS Modules: More verbose, harder to maintain consistency
  - Styled Components: Runtime overhead, larger bundle size

### Backend Structure
- **Decision**: Flask REST API with SQLAlchemy ORM
- **Why**: Lightweight, flexible, excellent for small to medium APIs, easy deployment
- **Database**: Start with SQLite for development, PostgreSQL for production
- **Alternatives considered**:
  - Next.js API Routes only: Limited for complex backend logic
  - Django: Overkill for this use case
  - Express.js: Keep Python ecosystem for backend consistency

### Content Management Strategy
- **Decision**: File-based content (markdown) with metadata frontmatter
- **Why**: Version controlled, easy to write, no database complexity for content
- **Blog**: MDX files in `/content/blog/` with gray-matter for metadata parsing
- **Projects**: JSON/markdown files in `/content/projects/`
- **Alternatives considered**:
  - Headless CMS (Contentful, Sanity): Adds complexity and cost
  - Database-only: Harder to version control and migrate

### Dark Mode Implementation
- **Decision**: CSS variables + localStorage + system preference detection
- **Why**: No flash of wrong theme, respects user preference, smooth transitions
- **Implementation**: `next-themes` library with Tailwind dark mode class strategy
- **Persistence**: Save preference in localStorage, fallback to system preference
- **Color System**:
  - Light mode: Background `#f3ede5`, text colors adjusted for contrast
  - Dark mode: Background `#092757`, text colors adjusted for contrast
  - Accent colors: `#86e5a1` and `#c5ffbc` with opacity variations for different states
  - Ensure WCAG AA contrast ratios in both modes

### SEO Strategy
- **Decision**: Next.js metadata API + static sitemap generation
- **Components**:
  - Meta tags: Use Next.js 14 Metadata API for each page
  - Structured data: JSON-LD for Person, WebSite, BlogPosting schemas
  - Sitemap: Auto-generated from routes and content
  - Open Graph: Custom OG images per page using `@vercel/og`
- **Performance**: Optimize Core Web Vitals (LCP <2.5s, FID <100ms, CLS <0.1)

### Form Handling & Email
- **Decision**: Flask endpoint + SendGrid/AWS SES for email delivery
- **Why**: Reliable delivery, spam management, tracking capabilities
- **Validation**: 
  - Frontend: React Hook Form with Zod schema validation
  - Backend: Flask-WTF for additional validation
  - Rate limiting: Flask-Limiter (5 submissions per IP per hour)
- **Spam protection**: Honeypot field + reCAPTCHA v3 (invisible)

### Image Optimization
- **Decision**: Next.js Image component + Cloudinary/Vercel Image Optimization
- **Why**: Automatic format selection (WebP/AVIF), responsive sizing, lazy loading
- **Strategy**: 
  - Store originals in `/public/images/`
  - Use `next/image` with priority for above-fold images
  - Lazy load below-fold content

### State Management
- **Decision**: React Context + Server Components (minimal client state)
- **Why**: Most state is server-rendered, minimal need for complex state management
- **Client state**: Theme preference, form state, UI interactions only
- **Alternatives considered**:
  - Zustand/Redux: Overkill for this use case
  - React Query: Good for data fetching but Next.js cache handles most needs

## Component Architecture

### Layout Structure
```
app/
├── layout.tsx              # Root layout with theme provider
├── page.tsx                # Home/About page
├── projects/
│   ├── page.tsx            # Projects listing
│   └── [slug]/page.tsx     # Project detail
├── blog/
│   ├── page.tsx            # Blog listing
│   └── [slug]/page.tsx     # Blog post
├── cv/page.tsx             # Resume page
└── contact/page.tsx        # Contact form
```

### Reusable Components
- `components/ui/`: Button, Card, Modal, Input, Badge
- `components/layout/`: Header, Footer, Navigation, Container
- `components/features/`: ProjectCard, BlogCard, SkillBadge, ContactForm
- `components/animations/`: FadeIn, SlideUp, PageTransition

## Database Schema

### Projects Table
```sql
id: UUID (primary key)
title: VARCHAR(200)
slug: VARCHAR(200) (unique)
description: TEXT
tech_stack: JSON
image_url: VARCHAR(500)
github_url: VARCHAR(500)
live_url: VARCHAR(500)
featured: BOOLEAN
created_at: TIMESTAMP
updated_at: TIMESTAMP
```

### Blog Posts Table
```sql
id: UUID (primary key)
title: VARCHAR(200)
slug: VARCHAR(200) (unique)
excerpt: TEXT
content: TEXT
author: VARCHAR(100)
category: VARCHAR(100)
tags: JSON
featured_image: VARCHAR(500)
published: BOOLEAN
published_at: TIMESTAMP
created_at: TIMESTAMP
updated_at: TIMESTAMP
```

### Contact Submissions Table
```sql
id: UUID (primary key)
name: VARCHAR(100)
email: VARCHAR(200)
subject: VARCHAR(200)
message: TEXT
ip_address: VARCHAR(45)
user_agent: VARCHAR(500)
status: VARCHAR(50) (pending/read/replied)
created_at: TIMESTAMP
```

## API Endpoints

### Backend API (Flask)
```
POST   /api/contact           # Submit contact form
GET    /api/projects          # Get all projects
GET    /api/projects/:slug    # Get single project
GET    /api/blog              # Get blog posts (with pagination)
GET    /api/blog/:slug        # Get single blog post
```

### Response Format
```json
{
  "success": true,
  "data": {},
  "message": "Success message",
  "errors": []
}
```

## Performance Targets

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: < 2.5s
- **FID (First Input Delay)**: < 100ms
- **CLS (Cumulative Layout Shift)**: < 0.1

### Lighthouse Scores (Mobile & Desktop)
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 95
- SEO: 100

### Bundle Size
- Initial JS: < 200KB (gzipped)
- First Load JS: < 300KB (gzipped)

## Deployment Strategy

### Frontend (Vercel)
- **Environment**: Production, Preview, Development
- **Build command**: `npm run build`
- **Environment variables**: API_URL, SITE_URL, CONTACT_EMAIL
- **Features**: Automatic deployments, preview URLs, edge functions

### Backend (Railway/Render/DigitalOcean)
- **Environment**: Production, Staging
- **Requirements**: `requirements.txt` with pinned versions
- **Database**: Managed PostgreSQL instance
- **Environment variables**: DATABASE_URL, SENDGRID_API_KEY, ALLOWED_ORIGINS
- **Health check**: `/health` endpoint

### CI/CD Pipeline
1. Push to branch → GitHub Actions trigger
2. Run linting (ESLint, Prettier)
3. Run type checking (TypeScript)
4. Run tests (Jest, Playwright)
5. Build frontend and backend
6. Deploy to preview/production

## Security Considerations

### Frontend
- Input sanitization for all user inputs
- XSS prevention (React automatic escaping)
- HTTPS only
- Content Security Policy headers
- CORS configuration

### Backend
- Rate limiting on all endpoints
- SQL injection prevention (SQLAlchemy ORM)
- CSRF protection on forms
- Email validation and sanitization
- Secure headers (Flask-Talisman)

## Accessibility Requirements

### WCAG 2.1 AA Compliance
- Semantic HTML structure
- Proper heading hierarchy (h1 → h6)
- ARIA labels where needed
- Keyboard navigation support
- Focus indicators
- Color contrast ratio > 4.5:1
- Alt text for all images
- Skip to main content link

## Monitoring & Analytics

### Analytics
- Google Analytics 4 (privacy-compliant)
- Vercel Analytics for performance
- Custom event tracking (project views, downloads, form submissions)

### Error Tracking
- Sentry for error monitoring
- Backend logging (Python logging module)
- Frontend error boundaries

### Performance Monitoring
- Vercel Speed Insights
- Real User Monitoring (RUM)
- Lighthouse CI in GitHub Actions

## Migration Plan

### Phase 1: Setup (Week 1)
1. Initialize Next.js and Flask projects
2. Set up development environment
3. Configure Tailwind and base components
4. Create database schema and migrations

### Phase 2: Core Pages (Week 2-3)
1. Build layout and navigation
2. Implement home/about page
3. Create projects showcase
4. Build blog system

### Phase 3: Features (Week 4)
1. Implement CV page
2. Add contact form
3. Implement dark mode
4. Add animations

### Phase 4: Optimization (Week 5)
1. SEO implementation
2. Performance optimization
3. Accessibility audit
4. Testing

### Phase 5: Deployment (Week 6)
1. Set up hosting
2. Configure CI/CD
3. Deploy to production
4. Monitoring setup

## Risks / Trade-offs

### Risk: SEO Performance on Client-Heavy Interactions
- **Mitigation**: Use Next.js Server Components for content, minimize client-side JavaScript

### Risk: Email Delivery Reliability
- **Mitigation**: Use established service (SendGrid/AWS SES), implement retry logic, log failures

### Risk: Form Spam
- **Mitigation**: Multiple layers (rate limiting, honeypot, reCAPTCHA, email verification)

### Trade-off: File-based vs Database Content
- **Chosen**: File-based (markdown) for blog
- **Trade-off**: Easier version control but harder for non-technical content updates
- **Future**: Can migrate to headless CMS if needed

### Trade-off: Separate Backend vs API Routes
- **Chosen**: Separate Flask backend
- **Why**: Better separation of concerns, easier to scale independently, Python ecosystem benefits
- **Cost**: Additional deployment and CORS configuration

## Open Questions

1. **Blog comment system**: Add comments? (Disqus, giscus, or none)
   - Recommendation: Start without, can add giscus (GitHub discussions) later

2. **Analytics provider**: GA4 vs Plausible vs Fathom?
   - Recommendation: Start with Vercel Analytics + GA4

3. **Newsletter integration**: Add email subscription?
   - Recommendation: Add in Phase 2 if needed (Mailchimp/ConvertKit)

4. **Admin panel**: Build custom admin or use external tool?
   - Recommendation: Start without, add later if managing content via files becomes cumbersome

5. **Multilingual support**: Add i18n from the start?
   - Recommendation: No, add later using next-intl if needed
