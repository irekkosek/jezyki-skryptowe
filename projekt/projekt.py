import math
import sys
from datetime import date, datetime
class Algorithm():
    def solution(self, n):
        sum = math.sqrt(n + 1)
        output=""
        output+="numeric sum: {0}\n".format(sum)
        output+="symbolic sum: sqrt({0})\n".format(n + 1)
        return output

if __name__ == "__main__":
    now = datetime.now()
    fulldate = now.strftime("%d-%m-%Y %H:%M:%S")
    with open("input", "r") as file_input:
        with open("output", "w") as file_output:
            with open("index.html", "w") as file_html:
                file_html.write("<html><body>")
                file_html.write("<h1>{0}</h1>".format(fulldate))
                calculate = Algorithm()
                try:
                    for line in file_input:
                        n = int(line)
                        print("Enter n:{0}".format(n))
                        if n < 1:
                            raise Exception("n must be greater than 0")
                        output=calculate.solution(n)
                        output_html=output.replace("\n", "<br>")
                        file_output.write(output)
                        file_html.write(output_html)
                except ValueError:
                    print("n must be a number")
                    sys.exit(1)
                except Exception as e:
                    print(e)
                    sys.exit(1)
                file_html.write("</body></html>")






    
    
