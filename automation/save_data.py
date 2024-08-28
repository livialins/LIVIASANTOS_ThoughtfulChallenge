from datetime import datetime
from RPA.Excel.Files import Files
import os


class SaveData:
    def __init__(self, challenge):
        self.challenge = challenge
        self.excel = Files()

    def create_excel_file(self, data, search_phrase: str):
        try:
            logger = self.challenge.logger
            logger.info("Creating Excel file")
            output_path = self.challenge.output_path
            
            todays_date = datetime.now().strftime("%Y-%m-%d")
            output_path = os.path.join(output_path, todays_date, search_phrase.lower())
            filename = "result.xlsx"

            # Verificação de caracteres inválidos no caminho do arquivo
            if any(char in r'\/:*?"<>|' for char in output_path):
                raise OSError(f"Invalid character in file path: {output_path}")

            # Check if output_path exists, if not create it
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # Cria o workbook Excel e salva
            self.excel.create_workbook(os.path.join(output_path, filename))
            self.excel.create_worksheet("news", content=data, header=True)
            self.excel.save_workbook()

        except Exception as e:
            logger.exception("Error creating Excel file")  # Correção no log de exceção
            raise Exception(f"Error creating Excel file: {e}")

        logger.info("Saved Excel file")





























# from datetime import datetime
# from RPA.Excel.Files import Files

# import os


# class SaveData:
#     def __init__(self, challenge):
#         self.challenge = challenge
#         self.excel = Files()
        

#     def create_excel_file(self, data, search_phrase: str):
#         try:
#             logger = self.challenge.logger
#             logger.info("Creating Excel file")
#             output_path = self.challenge.output_path
            
#             todays_date = datetime.now().strftime("%Y-%m-%d")

#             #output_path = os.path.join(output_path, todays_date, search_phrase.lower())  
#             filename = f"result.xlsx"

#             # Check if output_path exists, if not create it
#             if not os.path.exists(output_path):
#                 os.makedirs(output_path)

#             self.excel.create_workbook(os.path.join(output_path, filename))
#             self.excel.create_worksheet("news", content=data, header=True)
#             self.excel.save_workbook()
#         except Exception as e:
#             logger.exception(f"Error creating Excel file:", e)
#             raise Exception(f"Error creating Excel file:", e)

#         logger.info("Saved Excel file")









