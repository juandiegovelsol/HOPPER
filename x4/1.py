import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('./creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Inventario").sheet1

articulo = ["Camiseta", 50, 20.0, "2023-10-01", "Ingreso nuevo stock"]
sheet.append_row(articulo)