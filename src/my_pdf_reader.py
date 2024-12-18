import application_setting.my_logger as mylogger
from logging import Logger
from pypdf import PdfReader
from langchain_community.document_loaders import PyPDFLoader

logger: Logger = mylogger.get_logger("my_pdf_reader")


class MyPdfReader:

    def read_pdf(self, filepath: str) -> None:

        # pypdfをシンプルに利用する
        logger.info("pypdfをシンプルに利用してPDF読み込み")
        reader = PdfReader(filepath)
        number_of_pages = len(reader.pages)
        page = reader.pages[1]

        text = page.extract_text()
        logger.info(text)
        logger.info("========================")

        # langchainを利用する
        logger.info("langchainを利用してPDF読み込み")
        loader = PyPDFLoader(filepath)
        docs = loader.load()
        logger.info(docs[1])
