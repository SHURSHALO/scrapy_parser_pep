import csv
from pep_parse.settings import BASE_DIR, FILE_NAME


class PepParsePipeline:
    def __init__(self):
        self._status_counts = {}
        self._total_peps = 0

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        if status in self._status_counts:
            self._status_counts[status] += 1
        else:
            self._status_counts[status] = 1
        self._total_peps += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)
        file_path = result_dir / FILE_NAME
        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in self._status_counts.items():
                writer.writerow({'Статус': status, 'Количество': count})
            # Добавляем общее количество документов PEP в последнюю строку
            writer.writerow(
                {'Статус': 'Total', 'Количество': self._total_peps}
            )
