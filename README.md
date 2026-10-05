This is just a basic PDF to Excel convertor using python

I have used python to convert the undetectable PDF tables to actually detectable excel

Mostly, i needed this software to actually rank the data and actually do analysis on how the data was

Hence this project
-------------------------------------------------------------------------------------
To use it we can just run the extracter.py

We used two packages:
1. PDFPlumber
2. CSV

The thing i done is mostly

Take the pdf -> Open it using pdfplumber in python

make an object : writer using csv.writer

And then added x0,y0 and x1,y1 coords, to limit from which pixel to which pixel i have to take informatation from
-------------------------------------------------------------------------------------

There is also a ranker.py
It uses pandas and openpyxl

It is just used to rank the whole excel sheet using the cet percentiles

its optional 
