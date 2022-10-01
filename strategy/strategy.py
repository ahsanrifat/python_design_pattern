from abc import ABC, abstractclassmethod


class BaseFileProcessor(ABC):

    @abstractclassmethod
    def process_file(file):
        """Implement in the children classes"""


class ExcelFileProcessor(BaseFileProcessor):
    def process_file(file):
        print(f"{file} has been processed.(Excel)")


class PDFFileProcessor(BaseFileProcessor):
    def process_file(file):
        print(f"{file} has been processed.(PDF)")


class CSVFileProcessor(BaseFileProcessor):
    def process_file(file):
        print(f"{file} has been processed.(CSV)")


class MakeReport:
    def make_report(self, file, processor: BaseFileProcessor):
        processed_file = processor.process_file(file)
        print("Making report after processing file")


MakeReport().make_report("report.pdf", PDFFileProcessor)
MakeReport().make_report("report.excel", ExcelFileProcessor)
MakeReport().make_report("report.csv", CSVFileProcessor)
