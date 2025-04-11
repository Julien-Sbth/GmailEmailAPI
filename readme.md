# Gmail API Email Processor 📧

A powerful tool to automate email processing via the Gmail API with advanced classification and tagging features.

![Gmail API](https://img.shields.io/badge/Gmail_API-1.0.0-blue)! [Python](https://img.shields.io/badge/Python-3.8%2B-green)

## ✨ Main features

- **Secure authentication** : 
  - OAuth2 integration with automatic token management
  
- **Intelligent email processing**:
  - Automatic classification by categories
  - Management of labels (creation, application, deletion)

## 📋 Prerequisites

- Python 3.8+
- Google account with API access enabled
- Project configured in [Google Cloud Console](https://console.cloud.google.com/)

## 🚀 Quick installation

### Clone the repository:
```bash
git clone https://github.com/your-repo/gmail-api-email-processor.git

cd gmail-api-email-processor
```
## Install dependencies:
```bash
pip install -r requirements.txt
```bash
### 🔐 Credentials

1. Go to [Google Cloud Console] (https://console.cloud.google.com/).
2. Creates a new project (or uses an existing one).
3. Enable the Gmail API for this project.
4. In the "Identifiers" menu, click on "Create identifiers" > OAuth 2.0 client ID":
   - Application type: select "Desktop Application"
5. Downloads the generated file (‘json’ file).
6. Rename this file to `credentials.json’.
7. Move it to the project root (in the same folder as your Python script).
```

## ✅ Run the script

Once the above steps are completed, you can run the main script:
```
python main.py
```
On the first launch, a window will open to log in to your Google account. A token.json file will be automatically generated for subsequent connections.