import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from my_pdf_reader import MyPdfReader

# loggerを取得
logger: Logger = mylogger.get_logger("main")

PDF_FILE_PATH = "./resources/気候変動対策.pdf"


def main():
    logger.info("hello, world.")
    print(mycredential.KEY)
    pdf_reader = MyPdfReader()
    logger.info("PDF読み込み開始")
    pdf_reader.read_pdf(PDF_FILE_PATH)
    logger.info("PDF読み込み終了")


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()
