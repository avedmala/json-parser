# How to use it
Run PyQtGui.pyw to launch the program.

<img src="/screenshots/home.png" width="600" >

The four buttons open up different visualizations of the data from the JSON file.

<img src="/screenshots/mod1.png" width="300" >

<img src="/screenshots/graph1.png" width="300" >
<img src="/screenshots/graph2.png" width="300" >
<img src="/screenshots/graph3.png" width="300" >
<img src="/screenshots/graph4.png" width="300" >

You can search for a specific version or area and find some statistics about it.
<img src="/screenshots/mod2-1.png" width="500" >
<img src="/screenshots/mod2-2.png" width="500" >

You can also enter the index of the entry from the JSON file and you can see what is in it.
<img src="/screenshots/mod3.png" width="500" >

# How I built it
First and foremost, I used python because it is much easier to make graphs in than in java. The three important libraries I used are 
matplotlib, PyQt5, and pandas. Matplotlib enabled me to make graphs and charts with the large amount of data I had. PyQt5 powered the GUI. 
I could've used tkinter but it doesn't look as nice in my opinion. Pandas gave me a more advanced way to analyze the data from the JSON.

# Challenges I ran into
Figuring out what data to visualize was tough at the start. I had no idea what the data meant and had know idea how it would be useable.
I eventually picked a direction and stuck with it.

Creating the GUI. I stumbled around with tkinter for a while until I found pyqt. It was way more intuitive and helped me with what I needed.
The tedious part was re-writing all my code into functions instead of a big block of code so it would work easily with pyqt.
