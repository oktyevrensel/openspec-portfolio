## ADDED Requirements

### Requirement: SEO Meta Tags
The application SHALL implement comprehensive meta tags for search engine optimization.

#### Scenario: Basic meta tags
- **WHEN** rendering any page
- **THEN** include title tag (50-60 characters)
- **AND** include meta description (150-160 characters)
- **AND** include canonical URL
- **AND** include language and locale tags
- **AND** include viewport meta tag

#### Scenario: Page-specific titles
- **WHEN** viewing different pages
- **THEN** use descriptive, unique title for each page
- **AND** follow pattern: "Page Title | Site Name"
- **AND** keep titles concise and keyword-rich
- **AND** update document title on navigation

#### Scenario: Dynamic meta descriptions
- **WHEN** viewing content pages (blog, projects)
- **THEN** generate meta description from content excerpt
- **AND** limit to 160 characters
- **AND** include relevant keywords naturally
- **AND** make description compelling for click-through

### Requirement: Open Graph Tags
The application SHALL implement Open Graph protocol for social media sharing.

#### Scenario: Basic OG tags
- **WHEN** page is shared on social media
- **THEN** include og:title with page title
- **AND** include og:description with page description
- **AND** include og:url with canonical URL
- **AND** include og:type (website, article, profile)
- **AND** include og:site_name

#### Scenario: OG images
- **WHEN** page is shared
- **THEN** include og:image with optimized image (1200x630px)
- **AND** use page-specific image for blog posts and projects
- **AND** include og:image:alt for accessibility
- **AND** include og:image:width and og:image:height
- **AND** fall back to default site image if no specific image

#### Scenario: Twitter Card tags
- **WHEN** shared on Twitter/X
- **THEN** include twitter:card (summary_large_image)
- **AND** include twitter:title and twitter:description
- **AND** include twitter:image
- **AND** include twitter:creator handle (if applicable)

### Requirement: Structured Data
The application SHALL implement JSON-LD structured data for rich search results.

#### Scenario: Website schema
- **WHEN** on homepage
- **THEN** include WebSite schema with name, url, description
- **AND** include potentialAction for search functionality (if applicable)

#### Scenario: Person schema
- **WHEN** on about/homepage
- **THEN** include Person schema with name, jobTitle, description
- **AND** include social media profiles (sameAs)
- **AND** include email and address (if public)
- **AND** include image URL

#### Scenario: Blog post schema
- **WHEN** viewing blog post
- **THEN** include BlogPosting schema
- **AND** include headline, author, datePublished, dateModified
- **AND** include article body or description
- **AND** include image and publisher information
- **AND** include keywords/tags

#### Scenario: Breadcrumb schema
- **WHEN** on nested pages
- **THEN** include BreadcrumbList schema
- **AND** list all navigation levels
- **AND** include URLs for each breadcrumb item

### Requirement: XML Sitemap
The application SHALL generate an XML sitemap for search engine crawling.

#### Scenario: Sitemap generation
- **WHEN** building the application
- **THEN** generate sitemap.xml at root
- **AND** include all public pages
- **AND** include blog posts and projects
- **AND** set appropriate priority values (0.0-1.0)
- **AND** include lastmod dates from content
- **AND** update automatically when content changes

#### Scenario: Sitemap submission
- **WHEN** sitemap is accessible
- **THEN** serve at `/sitemap.xml`
- **AND** reference in robots.txt
- **AND** submit to Google Search Console
- **AND** submit to Bing Webmaster Tools

### Requirement: Robots.txt
The application SHALL provide a robots.txt file for crawler directives.

#### Scenario: Robots.txt configuration
- **WHEN** accessing `/robots.txt`
- **THEN** allow all crawlers (User-agent: *)
- **AND** reference sitemap location
- **AND** disallow crawling of admin/private paths (if any)
- **AND** set crawl-delay if needed

### Requirement: URL Structure
The application SHALL use SEO-friendly URL patterns.

#### Scenario: Clean URLs
- **WHEN** creating page URLs
- **THEN** use descriptive, readable slugs
- **AND** use hyphens for word separation
- **AND** keep URLs concise and keyword-rich
- **AND** avoid unnecessary parameters

#### Scenario: Blog post URLs
- **WHEN** generating blog URLs
- **THEN** use pattern `/blog/[slug]`
- **AND** derive slug from post title
- **AND** ensure slug uniqueness
- **AND** use lowercase characters

#### Scenario: Project URLs
- **WHEN** generating project URLs
- **THEN** use pattern `/projects/[slug]`
- **AND** derive slug from project title
- **AND** ensure slug uniqueness

### Requirement: Performance Optimization for SEO
The application SHALL meet Core Web Vitals metrics for better search rankings.

#### Scenario: Largest Contentful Paint (LCP)
- **WHEN** measuring page load performance
- **THEN** achieve LCP < 2.5 seconds
- **AND** optimize above-fold images
- **AND** prioritize critical CSS
- **AND** minimize render-blocking resources

#### Scenario: First Input Delay (FID)
- **WHEN** measuring interactivity
- **THEN** achieve FID < 100 milliseconds
- **AND** minimize JavaScript execution time
- **AND** use code splitting
- **AND** defer non-critical scripts

#### Scenario: Cumulative Layout Shift (CLS)
- **WHEN** measuring visual stability
- **THEN** achieve CLS < 0.1
- **AND** specify image dimensions
- **AND** reserve space for dynamic content
- **AND** avoid inserting content above existing content

### Requirement: Mobile SEO
The application SHALL be optimized for mobile search rankings.

#### Scenario: Mobile-friendly design
- **WHEN** testing on mobile devices
- **THEN** pass Google Mobile-Friendly Test
- **AND** use responsive design
- **AND** ensure text is readable without zooming
- **AND** ensure tap targets are appropriately sized (min 48x48px)
- **AND** avoid horizontal scrolling

#### Scenario: Mobile performance
- **WHEN** testing mobile performance
- **THEN** achieve good Lighthouse mobile scores
- **AND** optimize for slower network connections
- **AND** minimize mobile data usage
- **AND** prioritize mobile viewport loading

### Requirement: Content Accessibility for SEO
The application SHALL implement accessibility features that benefit SEO.

#### Scenario: Semantic HTML
- **WHEN** structuring content
- **THEN** use proper heading hierarchy (h1-h6)
- **AND** use semantic elements (article, section, nav, etc.)
- **AND** use descriptive link text (avoid "click here")
- **AND** include alt text for all images

#### Scenario: Internal linking
- **WHEN** creating content
- **THEN** include relevant internal links
- **AND** use descriptive anchor text
- **AND** ensure all pages are reachable within 3 clicks
- **AND** fix broken links automatically

### Requirement: Analytics and Search Console Integration
The application SHALL integrate with analytics and webmaster tools for SEO monitoring.

#### Scenario: Google Analytics setup
- **WHEN** tracking site usage
- **THEN** include Google Analytics 4 tracking code
- **AND** track page views and custom events
- **AND** respect user privacy preferences (GDPR)
- **AND** use cookie consent if required

#### Scenario: Search Console verification
- **WHEN** verifying site ownership
- **THEN** include Google Search Console meta tag or HTML file
- **AND** submit sitemap via Search Console
- **AND** monitor search performance
- **AND** fix crawl errors reported

#### Scenario: SEO monitoring
- **WHEN** monitoring SEO performance
- **THEN** track keyword rankings
- **AND** monitor Core Web Vitals
- **AND** track organic traffic
- **AND** identify and fix SEO issues

### Requirement: RSS Feed
The application SHALL provide an RSS feed for blog content syndication.

#### Scenario: RSS feed generation
- **WHEN** accessing `/feed.xml` or `/rss.xml`
- **THEN** serve valid RSS 2.0 feed
- **AND** include recent blog posts (last 20)
- **AND** include post title, description, link, pubDate
- **AND** include full content or excerpt
- **AND** update automatically when new posts published

#### Scenario: RSS discovery
- **WHEN** on blog pages
- **THEN** include RSS feed link in HTML head
- **AND** make feed discoverable by feed readers
