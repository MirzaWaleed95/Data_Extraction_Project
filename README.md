# OCR based Medical Data Extraction Project

## Problem statement
There are a lot of procedures needs to followed by the health insurance companies as per the government regulation to issue the claims, for that the insurance company has to process the images of patient details and prescription sent by hospitals or induvial doctors and extract useful data from them. For these process, the most insurance companies outsource workforce from companies like “Mr. X data Analytics” to extract the information from images manually.

Mr. X data Analytics uses a software, which will show the scanned images of patient details or prescription, the person needs to type the information by seeing the image manually in the the right side column and select the type of information . As it is a manual process, error will be common and dealing with the huge set of images like in the pandemic time, will not be possible with the same amount of workforce. As well the Insurance companies has requested to send the data within 24hrs when it is send for extraction. All of these constraints forced, Mr. X data Analytics to consider for a software upgrade from their old software.

## Solution approach
To solve all these problems, we are building a program which can do the extraction of data from images automatically. As always, machines can not replace humans. A person will recheck the extracted data and submit. So, that it will save a tremendous amount which was taken to type the data manually.

Here, we are using the Python programming language and pytesseract google library for extracting the data and Regex module to process the data and get distilled desired output.

## Technologies used
*Python
oops
Pdf2image module
Opencv
pytesseract
Regular expression
pytest
Postman
FastApi
Workflow
