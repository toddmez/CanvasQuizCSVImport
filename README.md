# CanvasQuizCSVImport
<iframe src="https://player.vimeo.com/video/532334035?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="1920" height="1080" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Canvas Quiz Generation"></iframe>

This is a script I created with the help of canvasapi wrapper to create MC quizzes in Instructure Canvas. 
Here is what you need: 
1. Canvas tolken. Place this in a text file called apikeyinfo.txt in the same directory as the ExamView py script.
2. Google Sheet. Found here: "https://docs.google.com/spreadsheets/d/1KDlf25mfIDE4CgJ2XBRBzDH0OPCe6WMGEW2hIHhDW10/edit?usp=sharing". Make a copy of this and customize this and export your csv file. Place the csv in the same directory as above. Name it quizcontent.csv
3. The following fields in green need to be edited before exporting ![image](https://user-images.githubusercontent.com/43012426/114895767-613e4d80-9dd5-11eb-8fd3-6d9ee4873c1c.png)
4. Multiple choice questions with A,B,C and D answers are supported. The fields in yellow indicate the answer. If any questions are left blank the spreadsheet will need to adjusted. ![image](https://user-images.githubusercontent.com/43012426/114896362-e32e7680-9dd5-11eb-9828-205f826eeca5.png)
5. The ExamView.py script. Run this to create your quiz!
