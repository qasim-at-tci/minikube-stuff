FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
ENV FLASK_APP=./src/app.py
ENV FLASK_ENV=development
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
                                        CMD curl -f http://localhost:5000/health || exit 1
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]