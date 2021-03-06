# YouData
YouData helps users fetch data / metadata (E.g. title, views, likes, comments, video category) from all 
uploaded videos of a youtube channel. The output is saved in a csv file.

Feel free to experiment with the some of the functionalities and inputs to achieve the results you want.

Note the sample API key credentials in the code will NOT work. Please obtain your own API key from Youtube's Data API platform.

![demo](https://github.com/xuan-hh/Youtube-Data-Analytics/blob/master/img/yd.PNG)

## Usage

0. Install all dependency libraries.

1. Initialise / update your Youtube API key with the -api flag. (Refer to https://developers.google.com/youtube/v3/getting-started on how to obtain your own API key)

    ```python3 <api_key> -api```

2. Get your data.

    You have 2 options here:

    a) Use the channel name. (youtube.com/user/**universityofexeter**)

    ```python3 <channel_name/universityofexeter>```

    b) Use the channel id. You have to specify the -id flag.

    ```python3 <channel_id> -id```

3. Find output.csv in root directory.

    Done!

## Sample

Here is a quick demonstration ran on University Of Exeter's Youtube Channel [7/4/2020]

| Title                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Views  | Likes | Dislikes | Comments | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Five Mantras for life by Rik Mayall, Honorary Doctorate of the University of Exeter | Warning: This video contains some swearing.The comedian and actor Rik Mayall was given an Honorary Doctorate by the University of Exeter in 2008. In his entertaining acceptance speech he gave the rest of the year's graduates an insight into his guiding principles.                                                                                                                                                                                                                                                             | 628847 | 5813  | 159      | 596      | rik mayall,graduation,graduate,Actor (Profession),Comedy (TV Genre),Comedian (Profession),The Young Ones (TV Program),Bottom (TV Program),the new statesman,rik mayall presents,Blackadder Goes Forth (TV Season),Filthy Rich & Catflap (TV Program),Drop Dead Fred (Film),Student,Students,university of exeter,exeter uni,exeter,UK universities,top ranked universities,university,student life,mantras,campus,college freshman,guide for life |
| University of Exeter - we're open for clearing 2019                                 | Got your results? We're open for Clearing! Visit our dedicated Clearing 2019 website for our current list of vacancies and to apply now http://www.exeter.ac.uk/clearingStill waiting for your results? Visit our website for our top tips for Clearing and sign-up for more information http://www.exeter.ac.uk/clearing/pre-registerPlease note that not all of our subjects will go into clearing. We'll be constantly updating our list of Clearing places on the vacancies page here http://www.exeter.ac.uk/clearing/vacancies | 383641 | 11    | 4        | 0        | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life,clearing,clearing 2019,clearing 2020,exeter,cornwall,business,medical imaging,radiography,nursing,streatham campus,penryn campus,maths,mathematics,physics,liberal arts,english,international studies,natural sciences,computer science,data science,IT,modern languages,languages                                      |
| MSc Engineering Business Management                                                 | Study MSc Engineering Business Management at the University of Exeter. Find out more today.                                                                                                                                                                                                                                                                                                                                                                                                                                          | 281795 | 0     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |
| MSc Data Science and Artificial Intelligence                                        | Study MSc Data Science and Artificial Intelligence at the University of Exeter. Find out more today.                                                                                                                                                                                                                                                                                                                                                                                                                                 | 274948 | 0     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |
| MSc Renewable Energy Engineering                                                    | Study MSc Renewable Energy Engineering at the University of Exeter. Find out more today.                                                                                                                                                                                                                                                                                                                                                                                                                                             | 274274 | 0     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |
| MSc Statistics                                                                      | Study MSc Statistics at the University of Exeter. Find out more today.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 268806 | 1     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |
| MSc Applied Data Science and Statistics                                             | Study MSc Applied Data Science and Statistics at the University of Exeter. Find out more today.                                                                                                                                                                                                                                                                                                                                                                                                                                      | 266190 | 3     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |
| Creativity Business Hack clip 1                                                     | MA Creativity: Innovation and Business StrategyDuring their course, students took part in an intensive Creativity Business Hack, offering creative solutions to real-life business challenges.                                                                                                                                                                                                                                                                                                                                       | 121859 | 0     | 0        |          | University of exeter,exeter uni,exeter university,student life,undergraduate,postgraduate,degree,studying,university life                                                                                                                                                                                                                                                                                                                         |

The table above is an excerpt from the complete result after sorting for the most viewed videos on the channel. Some general observations include how Exeter University's Masters programmes are popular. Comment fields that are blank indicate that commenting is disabled on those videos.

## Metadata

Metadata fetched including:
- Title, Category ID, view count, like count, dislike count, favourite count, comment count, Date Published, Description, tags

## Extensions

1. Optimising the code so it runs faster.

2. Introducing a GUI for general use by non-programmers.

3. Introducing graphing methods such as view-to-like ratio.

4. Perform Graph Visualisation on Youtube Data.

5. Perform Statistical Inference / Machine Learning on Youtube Data.
