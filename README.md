# LabelMarker
A small tools for marking training set label in machine learning

## Install

1. Git clone this repository in your system.
2. Install python3 , django
3. Enter the root path in ternimal, execute:   sh django_server_start.sh
4. Enter https://127.0.0.1:8000, enjoy it!

## How to use

Homepage like this:

![image](https://raw.githubusercontent.com/qq547276542/blog_image/master/Labelmarker/1.png)

You can handwork mark training set in webpage , instead of other ways. It can improve you efficiency, and you can share this page to other. It like “crowdsourcing”.

Unlabed data will appear randomly, it can guarantee the labeled data evenly.

This is the marked data count,you can overview it:

![image](https://raw.githubusercontent.com/qq547276542/blog_image/master/Labelmarker/2.png)

The only thing that user should do is click the radio and click submit button, the new labeled data will append in **label_data/label_data.txt**. This file's format is:

y1 x1

y2 x2

y3 x3

…….

You should define label set in **label_data/label_list.txt**. This file's format is:

y1

y2

y3

….

And you should add unlabeled data in **label_data/unlabeled_data.txt**. This file's format is:

x1

x2

x3

...







