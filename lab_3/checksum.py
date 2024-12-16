import json
import csv
import re
import hashlib
from typing import List
from path import *


def validate_row(row: List[str]) -> bool:
    return (
        re.match(VALID_EMAIL_REGEX, row[0]) and
        re.match(VALID_HEIGHT_REGEX, row[1]) and
        re.match(VALID_SNILS_REGEX, row[2]) and
        re.match(VALID_PASSPORT_REGEX, row[3]) and
        re.match(VALID_OCCUPATION_REGEX, row[4]) and
        re.match(VALID_LONGITUDE_REGEX, row[5]) and
        re.match(VALID_HEX_COLOR_REGEX, row[6]) and
        re.match(VALID_ISSN_REGEX, row[7]) and
        re.match(VALID_LOCALE_CODE_REGEX, row[8]) and
        re.match(VALID_TIME_REGEX, row[9])
    )


def process_csv(path: str) -> List[int]:
    invalid_rows: List[int] = []
    with open(path, newline='', encoding='utf-16') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        next(reader)

        for row_number, row in enumerate(reader, start=1):
            if not validate_row(list(row.values())):
                invalid_rows.append(row_number)
    return invalid_rows


def calculate_checksum(row_numbers: List[int]) -> str:
    row_numbers.sort()
    return hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()


def serialize_result(variant: int, checksum: str, path: str) -> None:
    result_data = {
        "variant": variant,
        "checksum": checksum
    }

    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(result_data, json_file, ensure_ascii=False, indent=4)


def main():
    # Вычисляем контрольную сумму
    checksum = calculate_checksum(process_csv(CVS_PATH))
    print(checksum)
    print(len(process_csv(CVS_PATH)))

    # Сериализуем результат в JSON файл
    serialize_result(variant=3, checksum=checksum, path=RESULT_PATH)


if __name__ == "__main__":
    main()
