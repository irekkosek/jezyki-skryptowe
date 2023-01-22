import math
import sys
from datetime import datetime

class Algorithm():
    def solution(self, n):
        sum = math.sqrt(n + 1)
        output=""
        output+=f"numeric sum: {sum}\n"
        output+=f"symbolic sum: sqrt({n+1})\n"
        return output

if __name__ == "__main__":
    exitcode = 0
    htmlendl = "<br>\n"
    now = datetime.now()
    fulldate = now.strftime("%d-%m-%Y %H:%M:%S")

    file_input = open("input", "r")
    file_output = open("output", "w")
    file_html = open("output.html", "w")

    file_html.write("<html><body>")
    file_html.write(f"<h1>{fulldate}</h1>\n")

    calculate = Algorithm()

    for line in file_input:
        try:
            file_html.write(f"Enter n: {line}"+htmlendl)
            n = int(line)
            
            if n < 1:
                raise Exception("n must be greater than 0")
            
            output=calculate.solution(n)
            output_html=output.replace("\n", htmlendl)

            file_output.write(output)
            file_html.write(output_html)
        except ValueError:
            file_html.write("n must be a number"+htmlendl)
            exitcode = 1
        except Exception as e:
            file_html.write(str(e)+htmlendl)
            exitcode = 1
    file_html.write("</body></html>")

    file_input.close()
    file_output.close()
    file_html.close()

    sys.exit(exitcode)
