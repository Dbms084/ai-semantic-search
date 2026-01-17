from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/documents.readonly"
]

def get_credentials():
    return service_account.Credentials.from_service_account_file(
        "service_account.json",
        scopes=SCOPES
    )

def list_google_docs():
    creds = get_credentials()
    drive_service = build("drive", "v3", credentials=creds)

    results = drive_service.files().list(
        q="mimeType='application/vnd.google-apps.document'",
        fields="files(id, name)"
    ).execute()

    return results.get("files", [])

def read_google_doc(doc_id):
    creds = get_credentials()
    docs_service = build("docs", "v1", credentials=creds)

    document = docs_service.documents().get(documentId=doc_id).execute()

    text = ""
    for element in document.get("body", {}).get("content", []):
        if "paragraph" in element:
            for run in element["paragraph"].get("elements", []):
                if "textRun" in run:
                    text += run["textRun"].get("content", "")

    return text
