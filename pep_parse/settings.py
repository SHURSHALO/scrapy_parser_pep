from datetime import datetime
from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


BASE_DIR = Path(__file__).resolve().parent.parent

ROBOTSTXT_OBEY = True

FILE_NAME = (
    f'status_summary_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
)


FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf8',
        'fields': ['number', 'name', 'status'],
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
