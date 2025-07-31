# Django HTTPS and Security Configuration

## Implemented Security Settings in `settings.py`

- `SECURE_SSL_REDIRECT`: Forces all HTTP requests to redirect to HTTPS.
- `SECURE_HSTS_SECONDS`: Enables HTTP Strict Transport Security for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD`: Enables preloading of HSTS.
- `SESSION_COOKIE_SECURE`: Ensures session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE`: Ensures CSRF cookies are only sent over HTTPS.
- `X_FRAME_OPTIONS = 'DENY'`: Protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables the browser’s XSS filter.

## Deployment Notes

- HTTPS is enforced via Nginx and SSL certificates from Let's Encrypt.
- HTTP traffic is redirected to HTTPS using Nginx `301` redirect.

## Potential Areas for Improvement

- Implement Content Security Policy (CSP).
- Use `django-csp` for stricter header management.
- Rotate and manage SSL certificates automatically with Certbot.
