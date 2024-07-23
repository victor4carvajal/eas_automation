import sys,os
from bs4 import BeautifulSoup
from optparse import OptionParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def parse_html_report(html_file):
    try:
        with open(html_file,'r') as f:
            soup = BeautifulSoup(f,'html.parser')
            filters_div = soup.find('div',class_='filters')
            if filters_div:
                summary_text = filters_div.get_text(separator=', ').strip()
                return summary_text.replace(',','').strip().replace('\n', '').replace('  ', ',')
            else:
                summary_text = "No test run summary found"
                return summary_text
    except Exception as FileNotFoundError:
        return "Test Run HTML report file not found"

if __name__=="__main__":
    parser=OptionParser()
    parser.add_option("-f","--file_name",dest="report",help="report file name",default="report.html")
    (options,args) = parser.parse_args()
    html_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'tests_results',f'{options.report}')
    summary = parse_html_report(html_file_path)
    if summary:
        print(summary)
    else:
        print("print no summary found")