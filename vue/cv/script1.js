const app = Vue.createApp({
  el: "#curriculum-vitae",
  data() {
    return {
      searchInput: "",
      dataColumns: ["certification", "date", "institution", "percentage"],
      dataset: 
[{"\n

\n \n Certification\n
\n ":"\n

\n Master Go (Golang) Programming:The Complete Go Bootcamp 2022\n
\n ","\n

\n Date\n
\n ":"\n

\n 20th April, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Andrei Dumitrescu, Crystal Mind Academy \n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Building Modern Web Applications with Go (Golang)\n
\n ","\n

\n Date\n
\n ":"\n

\n 27th March, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Trevor Sawler\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Vue - The Complete Guide (incl. Router & Composition API)\n
\n ","\n

\n Date\n
\n ":"\n

\n 24th March, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Maximilian Schwarzmüller\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Degree Certificate\n
\n ","\n

\n Date\n
\n ":"\n

\n 1st March, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Mumbai University\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Bachelor of Engineering\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Introduction to Microservices\n
\n ","\n

\n Date\n
\n ":"\n

\n 30th January, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n EdYoda Digital University\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n MongoDB - The Complete Developer's Guide\n
\n ","\n

\n Date\n
\n ":"\n

\n 22nd January, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Academind\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n AWS for Solutions Architect\n
\n ","\n

\n Date\n
\n ":"\n

\n 17th January, 2022\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n EdYoda Digital University\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n \n \n 2nd Covaxin Dose\n \n
\n ","\n

\n Date\n
\n ":"\n

\n 6th Sept, 2021\n
\n ","\n

\n Institution\n
\n ":"\n \n
\n

\n District Hospital, Aundh, Pune\n
\n \n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n COVID-19 Vaccination\n \n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n \n \n 1st Covaxin Dose\n \n
\n ","\n

\n Date\n
\n ":"\n

\n 5th Aug, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n COVID-19 Vaccination\n \n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n \n

\n सुभाषितं संस्कृतम्\n
\n

\n ","\n

\n Date\n
\n ":"\n

\n 2nd Aug, 2021\n
\n ","\n

\n Institution\n
\n ":"\n \n \n

\n भारतीय प्रोद्योगिकी संस्थानस्य (रूडकी) संस्कृतभारत्याः\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n

\n उत्तमश्रेण्याम्\n
\n \n \n \n

\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Bachelor of Engineering Semester 8\n
\n ","\n

\n Date\n
\n ":"\n

\n 28th July, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n University
of
Mumbai\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n \n \n SGPI: 9.75\n \n \n
\n \n Aggregate: 68.87%\n \n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n 12th, 15th and 16th Adhyāy Recitation\n
\n ","\n

\n Date\n
\n ":"\n

\n 27th July, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n Gītā Parivār\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n \n Marksheet\n \n
\n \n Certificate\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n AWS Summit India\n
\n ","\n

\n Date\n
\n ":"\n

\n 9th July, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n Amazon\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Attendance\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Scrum Fundamentals\n
\n ","\n

\n Date\n
\n ":"\n

\n 27th June, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n GenMan Solutions\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Subhāśitaṁ Saṁskr̥taṁ Specialization\n
\n ","\n

\n Date\n
\n ":"\n

\n
21th June, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n
\n SanskritBhāratī\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Course 5 marks: 45/50
Oral: 18/20\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Scripting in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 20th June, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n
\n Edcorner Learning\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Hands-On ML & AI\n
\n ","\n

\n Date\n
\n ":"\n

\n 13th June, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n EdYoda Digital University\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Certificate of Completion\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n 1st Place in Project Presentation Competition\n
\n ","\n

\n Date\n
\n ":"\n

\n


19th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n
\n SAKEC\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n First Prize Winner\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Create Amazing Vue Apps with JavaScript\n
\n ","\n

\n Date\n
\n ":"\n

\n \n
\n Mamoth Interactive\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n Certificate of Completing 6.5 Hours\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Importing Data in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 13th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n



\n Data
Camp\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n Statement of Accomplishment\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Advanced NLP with spaCy\n
\n ","\n

\n Date\n
\n ":"\n

\n 11th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n Statement of Accomplishment\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Natural Language Processing in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 9th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Writing Functions in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 7th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n BE 8th Semester's 2nd Internal Assessment\n
\n ","\n

\n Date\n
\n ":"\n

\n 6th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n SAKEC\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n 82.5%\n Report Card\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Feature Engineering for NLP in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 5th May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n
\n Data
Camp\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Spoken Language Processing in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 3rd May, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Android app using Kotlin\n
\n ","\n

\n Date\n
\n ":"\n

\n \n \n
\n

\n 28th Apr, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n
\n

\n Spoken Tutorial by IIT Bombay\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n 72.5%\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Java Training
\n ","\n

\n Date\n
\n ":"\n

70%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Arduino Training
\n ","\n

\n Date\n
\n ":"\n

75%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

PHP and MySQL
\n ","\n

\n Date\n
\n ":"\n

61.1%\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n English Word Play\n
\n ","\n

\n Date\n
\n ":"\n

\n 27th Apr, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n Speaker's Club\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n Passing\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Python Data Science Toolbox Part 2\n
\n ","\n

\n Date\n
\n ":"\n

\n 25th Apr, 2021\n
\n

\n \n \n
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n
\n
\n

\n Data \n
\n

\n Camp\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Sentiment Analysis in Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 24th Apr, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

\n \n Statement\n of Accomplishment\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Python\n
\n ","\n

\n Date\n
\n ":"\n

\n 31st Mar, 2021\n
\n ","\n

\n Institution\n
\n ":"\n

Hacker Rank
\n ","\n

\n Verification Link\n \n
\n ":"\n

Cleared\n assessment
\n "},{"\n

\n \n Certification\n
\n ":"\n

Software Project Competition
\n ","\n

\n Date\n
\n ":"\n

30th Mar, 2021
\n ","\n

\n Institution\n
\n ":"\n

IEEE-CRCE & WIE-CRCE
\n ","\n

\n Verification Link\n \n
\n ":"\n

Sentiment\n Analysis of the Mahābhārata Parvas
\n "},{"\n

\n \n Certification\n
\n ":"\n

BE Electronics and Telecommunication Engineering Semester 7\n
\n ","\n

\n Date\n
\n ":"\n

13th Mar, 2021
\n ","\n

\n Institution\n
\n ":"\n

Shah and Anchor Kutchhi Engineering College
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n \n 9.73 SGPI\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Examination on 12th & 15th Chapters of the\n Bhagavad-gītā
\n ","\n

\n Date\n
\n ":"\n

28th Feb, 2021
\n ","\n

\n Institution\n
\n ":"\n

Gītā Parivār
\n ","\n

\n Verification Link\n \n
\n ":"\n

Gītā\n Guñjan
\n "},{"\n

\n \n Certification\n
\n ":"\n

International Poetry Competition on International Mother Language\n Day
\n ","\n

\n Date\n
\n ":"\n

20th Feb, 2021
\n ","\n

\n Institution\n
\n ":"\n

Russian State University for the Humanities
\n ","\n

\n Verification Link\n \n
\n ":"\n

Recited\n Marathi Poem Translated into Russian
\n "},{"\n

\n \n Certification\n
\n ":"\n

Course 4 in Spoken Sanskrit
\n ","\n

\n Date\n
\n ":"\n

3rd Feb,2021
\n ","\n

\n Institution\n
\n ":"\n

SanskritBharati and
\n

IIT Roorkee
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n 90 marks
\n "},{"\n

\n \n Certification\n
\n ":"\n

Third Year Electronics and Telecommunication Engineering Semester\n 6
\n ","\n

\n Date\n
\n ":"\n

26th Dec, 2020
\n ","\n

\n Institution\n
\n ":"\n

\n

\n

Shah and Anchor Kutchhi Engineering College
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n 7.92 SGPI (updated, increased)\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Third Year Electronics and Telecommunication Engineering Semester\n 5
\n ","\n

\n Date\n
\n ":"\n

23rd Dec, 2020
\n ","\n

\n Institution\n
\n ":"\n

\n \n 7.93 SGPI\n \n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Course 3 in Spoken Sanskrit
\n ","\n

\n Date\n
\n ":"\n

13th Dec, 2020
\n ","\n

\n Institution\n
\n ":"\n

SanskritBharati and
\n

IIT Roorkee
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n 92 marks
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Data Analysis with Python [60 hours]\n
\n ","\n

\n Date\n
\n ":"\n

\n 14\n th\n  Oct, 2020\n
\n ","\n

\n Institution\n
\n ":"\n

\n Jovian and FreeCodeCamp\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Accomplishment
\n "},{"\n

\n \n Certification\n
\n ":"\n

Reinforced Machine Learning in Python
\n ","\n

\n Date\n
\n ":"\n

12th Oct,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Great Learning
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Completion
\n "},{"\n

\n \n Certification\n
\n ":"\n

Git for Version Control
\n ","\n

\n Date\n
\n ":"\n

11th Oct,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Data Camp
\n ","\n

\n Verification Link\n \n
\n ":"\n

Statement\n of Accomplishment
\n "},{"\n

\n \n Certification\n
\n ":"\n

Sergey Yesenin Poem Presentation
\n ","\n

\n Date\n
\n ":"\n

3rd Oct,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Russian State University
\n

for the Humanities
\n ","\n

\n Verification Link\n \n
\n ":"\n

Presented\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Course 2 in Spoken Sanskrit
\n ","\n

\n Date\n
\n ":"\n

23rd Sept,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

SanskritBharati and
\n

IIT Roorkee
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n 95 marks
\n "},{"\n

\n \n Certification\n
\n ":"\n

Statistical Learning
\n ","\n

\n Date\n
\n ":"\n

31st Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Great Learning
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Completion
\n "},{"\n

\n \n Certification\n
\n ":"\n

Traditional Face Detection with Python
\n ","\n

\n Date\n
\n ":"\n

26th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

 
\n

Real Python
\n

\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Achievement
\n "},{"\n

\n \n Certification\n
\n ":"\n

New Features in Python version 3.8
\n ","\n

\n Date\n
\n ":"\n

25th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Certificate\n of Achievement
\n "},{"\n

\n \n Certification\n
\n ":"\n

Functional Programing in Python
\n ","\n

\n Date\n
\n ":"\n

24th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Certificate\n of Achievement
\n "},{"\n

\n \n Certification\n
\n ":"\n

Semester 6 of Electronics and Telecommunications\n Engineering
\n ","\n

\n Date\n
\n ":"\n

21st Aug,2020
\n ","\n

\n Institution\n
\n ":"\n

Shah and Anchor Kutchhi Engineering College
\n ","\n

\n Verification Link\n \n
\n ":"\n

7.76\n SGPI
\n "},{"\n

\n \n Certification\n
\n ":"\n

Python 3.4.3 Training
\n ","\n

\n Date\n
\n ":"\n

\n

\n

19th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

\n

SpokenTutorial
\n

by
\n

IIT Bombay
\n ","\n

\n Verification Link\n \n
\n ":"\n

85%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Linux Training
\n ","\n

\n Date\n
\n ":"\n

70%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

RDBMS PostgreSQL Training
\n ","\n

\n Date\n
\n ":"\n

57.5%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

C++ Training
\n ","\n

\n Date\n
\n ":"\n

70%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Java Training
\n ","\n

\n Date\n
\n ":"\n

57.5%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Course 1 in Spoken Sanskrit
\n ","\n

\n Date\n
\n ":"\n

13th Aug, 2020
\n ","\n

\n Institution\n
\n ":"\n

SanskritBharati
\n

and IIT Roorkee
\n ","\n

\n Verification Link\n \n
\n ":"\n

Distinction. Written exam: 61/80\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Deep Learning with Python
\n ","\n

\n Date\n
\n ":"\n

8th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Great Learning
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Completion
\n "},{"\n

\n \n Certification\n
\n ":"\n

Natural Language Processing
\n ","\n

\n Date\n
\n ":"\n

6th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

SAKEC IT
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Machine Learning
\n ","\n

\n Date\n
\n ":"\n

4th Aug,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Solo
\n

Learn
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Data Science with Python
\n ","\n

\n Date\n
\n ":"\n

29th July, 2020
\n ","\n

\n Institution\n
\n ":"\n

Certificate\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Statistics for Data Science
\n ","\n

\n Date\n
\n ":"\n

27th July,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Great Learning
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Completion
\n "},{"\n

\n \n Certification\n
\n ":"\n

Python version 3 Tutorial
\n ","\n

\n Date\n
\n ":"\n

21st July,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Solo Learn
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Russian poem translated into Sanskrit
\n

\n ","\n

\n Date\n
\n ":"\n

6th June, 2020\n
\n ","\n

\n Institution\n
\n ":"\n

Russian State University
\n

for the Humanities
\n ","\n

\n Verification Link\n \n
\n ":"\n

 Presented in front of students from 16 universities in 9 countries
\n "},{"\n

\n \n Certification\n
\n ":"\n

International Recitation of Alexander Puskhkin’s Poetry\n
\n ","\n

\n Date\n
\n ":"\n

6th June,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Russian Center for Science and Culture
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Russian Language for Foreigners Competition
\n ","\n

\n Date\n
\n ":"\n

3rd Feb,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

Russian State University for the Humanities
\n ","\n

\n Verification Link\n \n
\n ":"\n

Secured\n Third Place
\n "},{"\n

\n \n Certification\n
\n ":"\n

RedHat Linux
\n ","\n

\n Date\n
\n ":"\n

18th Jan,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

SAKEC ACM
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Natural Language Processing
\n ","\n

\n Date\n
\n ":"\n

\n 8th Jan, 2020\n
\n ","\n

\n Institution\n
\n ":"\n

\n ISTE SAKEC\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n Certificate\n of Participation\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Made a Digital Lock during Winter Internship
\n ","\n

\n Date\n
\n ":"\n

2nd Jan,\n 2020
\n ","\n

\n Institution\n
\n ":"\n

SAKEC EXTC
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

First Year Engineering Semester 2
\n ","\n

\n Date\n
\n ":"\n

4th Feb,\n 2019
\n ","\n

\n Institution\n
\n ":"\n

Shah & Anchor Kutchhi Engineering College
\n ","\n

\n Verification Link\n \n
\n ":"\n

6.26\n SGPI
\n "},{"\n

\n \n Certification\n
\n ":"\n

Worked as Freelance Russian Interpreter
\n ","\n

\n Date\n
\n ":"\n

23rd Dec, 2019
\n ","\n

\n Institution\n
\n ":"\n

Ashish Life Sciences Private Limited
\n ","\n

\n Verification Link\n \n
\n ":"\n

Negotiated terms of a JV-partnership
\n "},{"\n

\n \n Certification\n
\n ":"\n

Microcontroller Programing
\n ","\n

\n Date\n
\n ":"\n

14th Dec, 2019
\n ","\n

\n Institution\n
\n ":"\n

IETE SAKEC
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Diploma in Russian Language
\n

(536 hour practical course)
\n ","\n

\n Date\n
\n ":"\n

31st May,\n 2019
\n ","\n

\n Institution\n
\n ":"\n

Pushkin Institute,
\n

Moscow, Russia
\n ","\n

\n Verification Link\n \n
\n ":"\n

Spoken\n test: 5/5
\n

Written\n test: 79/100
\n "},{"\n

\n \n Certification\n
\n ":"\n

Python Training
\n ","\n

\n Date\n
\n ":"\n

29th Aug, 2018
\n ","\n

\n Institution\n
\n ":"\n

SpokenTutorial by IIT Bombay
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Total Dictation in Russian
\n ","\n

\n Date\n
\n ":"\n

14th Apr, 2018
\n ","\n

\n Institution\n
\n ":"\n

TRUD and Russian Center
\n

for Science and Culture
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n of Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Basic Training Course in Air Rifle and Air Pistol
\n ","\n

\n Date\n
\n ":"\n

16th Mar, 2018
\n ","\n

\n Institution\n
\n ":"\n

Swatantrya Veer Savarkar
\n

Air Rifle Club
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certification 
\n "},{"\n

\n \n Certification\n
\n ":"\n

First Year Engineering Semester 1
\n ","\n

\n Date\n
\n ":"\n

12th Feb, 2018
\n ","\n

\n Institution\n
\n ":"\n

\n

Shah & Anchor Kutchhi Engineering College
\n ","\n

\n Verification Link\n \n
\n ":"\n

6.33\n SGPI
\n "},{"\n

\n \n Certification\n
\n ":"\n

Second Year Electronics and Telecommunication Engineering\n Semester 3
\n ","\n

\n Date\n
\n ":"\n

23rd Jan, 2018
\n ","\n

\n Institution\n
\n ":"\n

\n \n \n 6.08\n CGPI\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Data Analytics with Python and R\n
\n ","\n

\n Date\n
\n ":"\n

6\n th\n  Jan, 2018\n
\n ","\n

\n Institution\n
\n ":"\n

\n ISTE SAKEC\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n \n Certificate\n \n \n
\n

\n of\n Participation\n \n
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Second Year Electronics and Telecommunication Engineering Semester 4\n
\n ","\n

\n Date\n
\n ":"\n

\n 20\n th\n  July, 2017\n
\n ","\n

\n Institution\n
\n ":"\n

\n Shah & Anchor Kutchhi Engineering College\n
\n ","\n

\n Verification Link\n \n
\n ":"\n

6.25\n SGPI
\n "},{"\n

\n \n Certification\n
\n ":"\n

\n Hands-On Python Programing\n
\n ","\n

\n Date\n
\n ":"\n

7\n th July, 2017\n
\n ","\n

\n Institution\n
\n ":"\n

SAKEC ACM
\n ","\n

\n Verification Link\n \n
\n ":"\n

\n Certificate\n \n
\n

\n of\n Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

A1, A2 and B1 Levels of the Russian Language
\n ","\n

\n Date\n
\n ":"\n

2017
\n ","\n

\n Institution\n
\n ":"\n

Russian Center for Science and Culture
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificates:
\n

A1, A2 , B1\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

LibreOffice Suite Writer
\n ","\n

\n Date\n
\n ":"\n

17th Oct, 2016
\n ","\n

\n Institution\n
\n ":"\n

\n

SpokenTutorial by IIT Bombay
\n ","\n

\n Verification Link\n \n
\n ":"\n

Certificate\n
\n

of\n Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

LibreOffice Suite Calc
\n ","\n

\n Date\n
\n ":"\n

17th Oct, 2016
\n ","\n

\n Institution\n
\n ":"\n

Certificate\n
\n

of\n Participation
\n "},{"\n

\n \n Certification\n
\n ":"\n

Higher Secondary Certificate (12th)
\n ","\n

\n Date\n
\n ":"\n

2015
\n ","\n

\n Institution\n
\n ":"\n

Kirti M. Doongursee College, Dadar West
\n ","\n

\n Verification Link\n \n
\n ":"\n

69.38%\n
\n "},{"\n

\n \n Certification\n
\n ":"\n

Secondary School Certificate (10th)
\n ","\n

\n Date\n
\n ":"\n

2013
\n ","\n

\n Institution\n
\n ":"\n




St Stanislaus’ High\n School, Bandra West
\n ","\n

\n Verification Link\n \n
\n ":"\n

86.2% 
\n

Science: 99/100
\n "},{"\n

\n \n Certification\n
\n ":"\n

High School Scholarship Examination
\n ","\n

\n Date\n
\n ":"\n

\n

2010
\n ","\n

\n Institution\n
\n ":"\n

Scholarship awarded
\n "},{"\n

\n \n Certification\n
\n ":"\n

Intermediate Grade Drawing Examination
\n ","\n

\n Date\n
\n ":"\n

C
\n "},{"\n

\n \n Certification\n
\n ":"\n

Elementary Grade Drawing Examination
\n ","\n

\n Date\n
\n ":"\n

2009
\n ","\n

\n Institution\n
\n ":"\n

B
\n "},{"\n

\n \n Certification\n
\n ":"\n

Middle School Scholarship Examination
\n ","\n

\n Date\n
\n ":"\n

2007
\n ","\n

\n Institution\n
\n ":"\n

Passed 
\n

Language: 90/100
\n "}],
      // dataSet,
      dataset1:  [
        {
          certification: "Bachelor of Engineering in Electronics & Telecommunication", 
          date: "15th June, 2021",
          institution: "University of Mumbai",
          percentage: 62.05},

        {certification: 'Android app using Kotlin', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 72.5},
        {certification: 'Java', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'Arduino', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 75},
        {certification: 'PHP and MySQL', date: '28th Apr, 2021', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 61.1},

        { certification: "BE 8th Semester's 2nd Internal Assessment",
        date: "6th May, 2021", institution: "SAKEC", percentage: 82.5},

        {certification: 'Python 3.4.3', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 85},
        {certification: 'Linux', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'RDBMS PostgreSQL', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 57.5},
        {certification: 'C++', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 70},
        {certification: 'Java', date: '19th Aug, 2020', 
        institution: 'SpokenTutorial, IIT Bombay', percentage: 57.5},
        
        { certification: "Spoken Sanskrit Course", date: "13th Aug, 2020",
          institution: "SankritBharati, IIT Roorkee", percentage: 76.25
        },
        {
          certification: "Diploma in Russian Language (536 hour practical course)",date: "31st May, 2019",
          institution: "Pushkin Institute, Moscow, Russia", percentage: 89.5
        },

        {certification: "Higher Secondary Certificate (12th)", date: 2015,
        institution: "Kirti M. Doongursee College, Dadar West", percentage: 69.38
        },
       {certification: "Secondary School Certificate (10th)", date: 2013,
        institution: "St Stanislaus’ High School, Bandra West",      
        percentage: 86.2
       },
      ]
    }
  }
}) 
 
app.component("curriculum-vitae-component", {
  template: "#grid-template",
  props: {
    entries: Array,
    columns: Array,
    filterKey: String
  },
  data: function() {
    return {
      sortKey: ""
    }
  },
  computed: {
    filteredTitles: function() {
      const sortKey = this.sortKey
      
      const filterKey = this.filterKey && this.filterKey.toLowerCase()

      const order = this.sortColumns[sortKey] || 1

      let entries = this.entries

      if (filterKey) {
        entries = entries.filter(function(row) {
          return Object.keys(row).some(function(key) {
            return (
              String(row[key])
              .toLowerCase()
              .indexOf(filterKey) > -1
            )
          })
        })
      }
      if (sortKey) {
        entries = entries.slice().sort(function(x, y) {
          x = x[sortKey]
          y = y[sortKey]
          return (x === y ? 0 : x > y ? 1 : -1) * order
        })
      }
      return entries
    },
      sortColumns() {
        const sortedColumns = {}

        this.columns.forEach(function(key) {
          sortedColumns[key] = 1
        })

        return sortedColumns
      }
    },
    methods: {
      capitalize(inputString) {
        return inputString.charAt(0).toUpperCase() + inputString.slice(1)
      },
      sortBy(key) {
        this.sortKey = key
        this.sortColumns[key] = this.sortColumns[key] * -1
      }
    }
  })

app.mount("#curriculum-vitae")
