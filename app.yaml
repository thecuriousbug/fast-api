runtime: python39  # or the appropriate Python version

handlers:
- url: /.*
  script: auto

entrypoint: uvicorn main:app --host=0.0.0.0 --port=${PORT}
