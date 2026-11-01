FROM python:3.12-slim

WORKDIR /app
COPY reference-app /app/reference-app

ENV PANELFORGE_ENV=production
ENV PANELFORGE_DB=/var/lib/panelforge/reference.sqlite3
RUN useradd --create-home --uid 10001 panelforge \
    && mkdir -p /var/lib/panelforge \
    && chown -R panelforge:panelforge /app /var/lib/panelforge
USER panelforge

EXPOSE 4173
VOLUME ["/var/lib/panelforge"]
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:4173/api/health', timeout=3)"
CMD ["python", "reference-app/server.py"]
