import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from lxml import etree

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'


class WorkshiftXML:
    """
    Класс для работы с XML и вычисления пребывания общего времени на сменах всех людей по дням
    Args:
        path(str): Местоположение файла XML со сменами работников

    Returns:
        DataFrame(columns=['day','workshift_minute']): Список дней и общее время пребывания всех сотрудников в минутах

    Examples:
        >>> workshift = WorkshiftXML('test.xml')
        >>> result = workshift.workshifts(start_date='02-03-2015', logins='b.testobject,a.stepanova')
        >>> result
        day              workshift_minutes
        21-12-2011       1027.333333
        22-12-2011        619.083333
    """

    def __init__(self, path):
        self.path = path

    def _read_xml(self):
        context = etree.iterparse(self.path, events=('end',), tag='person')
        for event, elem in context:
            yield elem

    def workshifts(self, filter_start_date='01-01-1970 00:00:00', filter_end_date='31-12-2999 00:00:00', logins=None):
        """
        Получение общего времени пребывания на смене по дням
        :param filter_start_date: фильтр для начальной даты
        :param filter_end_date: фильтр для конечной даты
        :param logins: список сотрудников через запятую
        :return: список дней и общее время пребывания всех сотрудников в минутах в формате DataFrame
        """
        result = pd.DataFrame()
        filter_start_date = parse(filter_start_date)
        filter_end_date = parse(filter_end_date)

        if logins:
            logins = [i.replace(' ', '') for i in logins.split(',')]

        for elem in self._read_xml():
            start_date = datetime.strptime(elem.find('start').text, DATETIME_FORMAT)
            end_date = datetime.strptime(elem.find('end').text, DATETIME_FORMAT)
            login = elem.get('full_name')

            if filter_start_date <= start_date <= filter_end_date \
                    and (not logins or login in logins):
                result = result.append({
                    'login': login,
                    'day': start_date.strftime("%d-%m-%Y"),
                    'workshift_minutes': (end_date - start_date).seconds / 60
                }, ignore_index=True)

            # очистка элемента, чтобы в памяти не строилось дерево структуры xml
            elem.clear()

        return result.groupby('day').sum() if len(result.index) > 0 else None
