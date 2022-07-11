# S3_bucketLogs
Downloading the Logs from s3 from the both the servers

## DESCRIPTION
This utility helps you to fetch the logs from the s3 bucket. In search-aprodssist logs there are two categories, 1.pilot  2.prod. Currently pilot server- logs are accessible. There is flexibility to choose the logTypes and preferred date so that you can able to get the logs as per your desired logtype and date. These logs will be stored in in the local. The final merged and sorted log file will be opened and stored in the finalServerLogs folder. 

## PREREQUISITE
s3cmd credintials should be configured

## SOFTWARE REQUIREMENTS
1. Python

## HOW TO DOWNLOAD 

#### STEP1:
   Download the files from Github and store them on the home directory.
   
#### STEP2:
   Run the getlog file (if any issue,give previlige to the file --> chmod u+x ./getlog , later run the file).
   command :  ./getlog        ("Press Enter")
   
#### STEP3:
   -> Types of servers will be displayed. Enter the number you desired.(1 0r 2) If you wanted to continue without entering number, 
      the default pilot will be considered._
   -> Types of logs will be displayed. Enter the number you desired.(1, 2, 3, 4) If you wanted to continue without entering number, 
      the default services will be considered._
   -> choosing of date will be displayed. Enter the negative number you desired.(-1, indicates yesterday logs.-2, indicates day before yesterday logs) upto       before 7days. If you wanted to continue without entering number default today's date will be considered._
   -> File choosing will be displayed. Enter the number you desired.(1, 2) If you wanted to continue without entering number, 
      all the existing files will be downloaded._
      
   >The Requested Files will be opened to view.
   
 
   
   
