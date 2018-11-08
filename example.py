import tsv_downloader
reload(tsv_downloader)
#from tsv_downloader import CourseSheetDownloader
import gspread
import json


url = "https://docs.google.com/spreadsheets/d/1aQRvvLLmPUfXui8OiGKeMQtKO6XIJr8zFiFw9fv26rU/edit#gid=1274671759"
download_to_dir = '/tmp/'
dir_prefix= "Course"

tsv_downloader.SheetDownloader(url,download_to_dir)

sheets=tsv_downloader.SheetDownloader(url,download_to_dir)
sheets.dump_sheets()

sheets2= tsv_downloader.CourseSheetDownloader(url,dir_prefix)
sheets2.get_all_sheets()

sheets_data = (self.Courses, self.Lessons, self.Media, self.Modules)

essential_fields_key_value = json.load(open('essential.json'))

for (essential_key, one_sheet_data) in zip(sorted(essential_fields_key_value), sheets_data):
    essential_values = essential_fields_key_value[essential_key]
    for one_essential_value in essential_values:
        index_of_essential_value = one_sheet_data[1].index(one_essential_value)
        for rows in range(2, len(one_sheet_data)):
            if one_sheet_data[rows][index_of_essential_value] == "":
                logging.critical(one_essential_value + " field is missing in " + essential_key + " sheet")
