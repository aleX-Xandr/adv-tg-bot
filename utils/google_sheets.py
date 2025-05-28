import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_SHEET_CREDS, SPREADSHEET_NAME

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_CREDS, scope)
client = gspread.authorize(creds)
def get_or_create_sheet():
    try:
        sheet = client.open(SPREADSHEET_NAME).sheet1
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(SPREADSHEET_NAME)
        sheet = spreadsheet.sheet1
        sheet.append_row(["Дата", "Накладная", "Бренд", "Производитель", "Количество фото", "Цена", "Ссылка"])

        spreadsheet.share("sashaua007@gmail.com", perm_type="user", role="writer")
        spreadsheet.share("magzhan369@gmail.com", perm_type="user", role="writer")
        print(f"https://docs.google.com/spreadsheets/d/{spreadsheet.id}")
    return sheet


def append_row(data: list):
    sheet = get_or_create_sheet()
    sheet.append_row(data)
