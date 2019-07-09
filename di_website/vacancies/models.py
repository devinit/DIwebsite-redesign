from di_website.common.base import StandardPage


class VacanciesPage(StandardPage):
    class Meta:
        db_table = 'vacancies_page'
        verbose_name = 'Vacancies Page'

    parent_page_types = [
        'home.HomePage'
    ]
