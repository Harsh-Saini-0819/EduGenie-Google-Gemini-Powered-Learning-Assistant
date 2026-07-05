FROM python:3.10-slim

# Set up environment variables
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONUNBUFFERED=1

# Create Hugging Face user profile
RUN useradd -m -u 1000 user
USER user
WORKDIR $HOME/app

# Copy dependencies and install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your modules (main.py, qna.py, static, templates, etc.)
COPY --chown=user . .

# Expose Hugging Face web port
EXPOSE 7860

# Run Uvicorn pointing to your app instance inside main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]