import argparse
import sys
from workshifts import WorkshiftXML


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--xml_path', help='Путь до XML-файла со сменами')
    parser.add_argument('--start_date', help='Начальный срез смен, по которому будет идти поиск', default='01-01-1970 00:00:00')
    parser.add_argument('--end_date', help='Конечный срез смен, по которому будет идти поиск', default='31-12-2999 00:00:00')
    parser.add_argument('--logins', help='Список логинов через запятую', default=[])
    args = parser.parse_args()
    if not args.xml_path:
        raise ValueError("Путь до XML-файла со сменами должен быть указан в аргументе xml_path")
    
    workshift = WorkshiftXML(args.xml_path)
    sys.stdout.write(str(workshift.workshifts(args.start_date, args.end_date, args.logins)))