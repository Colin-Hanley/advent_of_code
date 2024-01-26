import re


class CalibrationDocumentReader:
    def __init__(self, file_name: str):
        """"
        This class is responsible for helping the elves read their poorly written calcibration documents.

        The elves printer drivers are out of date and often print characters and extra numbers in the document.
        The elves need to extract the coordinates from the document, which are the first and last numbers in each line.
        Once they know the coordinates, they add them up to bill the head elf the cannon supplies used.

        Functions in this class:
        - read_in_file_lines: reads in the file lines and returns them as a list of strings
        - extract_numeric_values_from_string: extracts the numeric values from a string and returns them as a string
        - create_int_from_fist_and_last_number: creates an int from the first and last number in a string
        - extract_coordinate_from_string: extracts the coordinate from a string and returns it as an int
        - extract_coordinates_from_document: extracts the coordinates from the document and returns them as a list of ints

        Params:
            - file_name: the name of the file to read in
            :type file_name: str

        Example:
            >>> calibration_document = CalibrationDocumentReader("advent_of_code_1.txt")
            >>> calibration_document.extract_coordinates_from_document()
            [11, 11, 11]
            >>> print(sum(calibration_document.extract_coordinates_from_document()))
            33

        """
        self.file_name = file_name

    def read_in_file_lines(self) -> list[str]:
        """
        Reads in the file lines and returns them as a list of strings

        returns:
            - list[str]: the file lines as a list of strings

        """
        try:
            with open(self.file_name) as file:
                return file.read().split("\n")
        except FileNotFoundError as e:
            print(f"File not found: {e}")

    def extract_numeric_values_from_string(self, string_value: str) -> str:
        return "".join(re.findall(r"\d+\.\d+|\d+", string_value))

    def create_int_from_fist_and_last_number(self, string_cast_number: str) -> int:
        try:
            return int("".join([string_cast_number[0], string_cast_number[-1]]))
        except IndexError as e:
            print(f"Index error: {e}")

    def extract_coordinate_from_string(self, string_value: str) -> int:
        return self.create_int_from_fist_and_last_number(
            self.extract_numeric_values_from_string(string_value)
        )

    def extract_coordinates_from_document(self) -> list[int]:
        return [self.extract_coordinate_from_string(line) for line in self.read_in_file_lines()]


def __main__():
    calibration_document = CalibrationDocumentReader("advent_of_code_1.txt")
    coordinates = calibration_document.extract_coordinates_from_document()
    print("Sum:", sum(coordinates))


if __name__ == "__main__":
    __main__()
