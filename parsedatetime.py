from datetime import datetime
date_string ="%d %b %Y"
input=input()
date_object=datetime.strptime(input,date_string)
print(date_object)
