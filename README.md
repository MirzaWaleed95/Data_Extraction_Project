# OCR based Medical Data Extraction Project

## Problem statement
There are a lot of procedures needs to followed by the health insurance companies as per the government regulation to issue the claims, for that the insurance company has to process the images of patient details and prescription sent by hospitals or induvial doctors and extract useful data from them. For these process, the most insurance companies outsource workforce from companies like “Mr. X data Analytics” to extract the information from images manually.

Mr. X data Analytics uses a software, which will show the scanned images of patient details or prescription, the person needs to type the information by seeing the image manually in the the right side column and select the type of information . As it is a manual process, error will be common and dealing with the huge set of images like in the pandemic time, will not be possible with the same amount of workforce. As well the Insurance companies has requested to send the data within 24hrs when it is send for extraction. All of these constraints forced, Mr. X data Analytics to consider for a software upgrade from their old software.

## Solution approach
To solve all these problems, we are building a program which can do the extraction of data from images automatically. As always, machines can not replace humans. A person will recheck the extracted data and submit. So, that it will save a tremendous amount which was taken to type the data manually.

Here, we are using the Python programming language and pytesseract google library for extracting the data and Regex module to process the data and get distilled desired output.

## Technologies used
* Python <br />
* oops <br />
* Pdf2image module <br />
* Opencv <br />
* pytesseract <br />
* Regular expression <br />
* pytest <br />
* Postman <br />
* FastApi <br />
* Workflow

## Workflow
![workflow](https://user-images.githubusercontent.com/108637079/188907761-18938235-c9f4-42b5-945b-83279bebcb8c.jpg)

## PDF to Image
For converting PDF to image, we have used pdf2image library.

## Without preprocessing extracting data
Tried extracting data from source files without any processing, as they are not in proper format to be extracted, the extracted data was not as expected.

![dark_image](https://user-images.githubusercontent.com/108637079/188908642-2c7a5a18-1d0d-4b99-ada3-8aa3e501a14b.jpg)

## Extracted data from the above image
    

      Dr John Smith, M.D
      2 Non-Important Street,
      New York, Phone (000)-111-2222

      Name: Maria Sharapova Date: 5/11/2022

      Address: 9 tennis court, new Russia, DC

      —momennannenncmneneunnmnnnnninsissiyoinnitnahaadaanih issn earnttneenrenen:

      Prednisone 20 mg
      Lialda 2.4 gram

      3 days,

      or 1 month

## Image processing
we decided to preprocess the image using opencv module, before extracting data from them. For that we have first used normal thresholding and checked, which resulted in below image

![filter_dark](https://user-images.githubusercontent.com/108637079/188912143-09f9894c-4553-4396-bd48-0cfd21206e7c.jpg)

So, if there is any shadow or some noise, the normal thresholding fade out the area. which will result in loss of data.

In the search of better approach of this problem, we have decided to use adaptive thresholding technique. In this technique, the image will be divided into sub image and the thresholding value will be different for all sub regions. And the end result of adaptive thresholding is much better compared to normal thresholding.

![adaptive_filter_dark](https://user-images.githubusercontent.com/108637079/188912282-4bc8fde3-81e0-401c-b75c-557e990e2d01.jpg)

<img src="https://your-image-url.type](https://user-images.githubusercontent.com/108637079/188912282-4bc8fde3-81e0-401c-b75c-557e990e2d01.jpg" width="500" height="500">


## After preprocessing the image data extraction

      Dr John Smith, M.D
      2 Non-Important Street,
      New York, Phone (000)-111-2222
      
      Name: Marta Sharapova Date: 5/11/2022
      
      Address: 9 tennis court, new Russia, DC
      
      K
      
      Prednisone 20 mg
      Lialda 2.4 gram
      
      Directions:
      
      Prednisone, Taper 5 mg every 3 days,
      Finish in 2.5 weeks a
      Lialda - take 2 pill everyday for 1 month
      
## Notebook
For all these above trials, used jupyter books and developed the small bits of the functionalities., which can be used later while designing the class.

      


