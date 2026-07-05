# EduGenie: AI-Powered Learning Assistant

EduGenie is a web application built using **FastAPI**, **Jinja2 Templates**, and **Vanilla HTML/CSS** with asynchronous processing. It provisions customized academic assistance by orchestrating **Google Gemini 1.5 Pro** for large-scale cognitive workflows and local **LaMini-Flan-T5** pipelines for quick text transformations.

## 🛠️ System Pre-requisites
* **Python**: `Version 3.10` or higher required.
* **API Credentials**: Valid `GEMINI_API_KEY` obtained via [Google AI Studio](https://aistudio.google.com/).

## 🚀 Step-by-Step Local Deployment

1. **Clone or Navigate to the Directory**:
   ```bash
   cd EDUGENIE
   ```

2. **Establish Isolated Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Environment**:
   * **Windows**: `venv\Scripts\activate`
   * **Mac/Linux**: `source venv/bin/activate`

4. **Install System Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Expose Environment Credentials**:
   * **Windows (CMD)**: `set GEMINI_API_KEY=your_actual_api_key_here`
   * **Windows (PowerShell)**: `$env:GEMINI_API_KEY="your_actual_api_key_here"`
   * **Mac/Linux**: `export GEMINI_API_KEY="your_actual_api_key_here"`

6. **Initialize Asynchronous Application Server**:
   ```bash
   uvicorn main:app --reload
   ```

7. **Access Interface Workspace**:
   Open browser environment and navigate to: `http://127.0.0.1:8000`
