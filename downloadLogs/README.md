This folder is to hold the Data_Download_Verbose_*.out files where the * is the date and time. These files help keep track of what data has been downloaded and when.

This folder only contains text files for the users reference. But is necessary in the Forecast Search Wizard file structure as retrieve.py is creating the Data_Download_Verbose 
file and expects to place it in this folder. If users set up a cron job to excute download_data.py regularly, they may also want to create a cronLogs folder within 
Forecast_Search_Wizard to track the output and error files. These files do not serve any higher purpose.
