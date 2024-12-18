import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
from pypdf import PdfReader

# loggerを取得
logger: Logger = mylogger.get_logger("main")


def main():
    logger.info("hello, world.")
    print(mycredential.KEY)
    reader = PdfReader("./resources/気候変動対策.pdf")
    number_of_pages = len(reader.pages)
    page = reader.pages[0]

    text = page.extract_text()
    logger.info(text)


def add_one(number: int) -> int:
    return number + 1


if __name__ == "__main__":
    main()
