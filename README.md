# Chapterize

This command-line tool breaks up a plain text book into chapters. 
It works especially well with Project Gutenberg plain text ebooks.
It may also be used to strip metatextual text from a book, such as tables of contents, headings, and Project Gutenberg licenses. This may be useful for preparing an ebook for computational text analysis. Just use the --nochapters option.

## Usage

### Break a Novel into Chapters: 

```
# Grab a copy of Pride and Prejudice from Project Gutenberg: 
wget https://www.gutenberg.org/files/1342/1342-0.txt

# Give it a nicer name. 
mv pg1342.txt pride-and-prejudice.txt 

# Run Chapterize on it:  
chapterize pride-and-prejudice.txt
```

This should output a directory in the current working directory called `pride-and-prejudice-chapters`, containing files 01.txt through 56.txt. You can then change into that directory, and run text analysis programs, like my [macroetym](https://github.com/JonathanReeve/macro-etym) tool: 

```
cd pride-prejudice-chapters
macroetym *
```

This will compare the macroetymologies of all the chapters in _Pride and Prejudice_. 

### Extract Text from a Book

```
# Grab a copy of Pride and Prejudice from Project Gutenberg: 
wget http://www.gutenberg.org/cache/epub/1342/pg1342.txt

# Give it a nicer name. 
mv pg1342.txt pride-and-prejudice.txt 

# Run Chapterize on it, setting the --nochapters flag:  
chapterize pride-and-prejudice.txt --nochapters
```

This will grab all the text from all the chapters, but will remove titles, chapter headings, Project Gutenberg introductions and licenses, and most other metatext. It will write a file called pride-prejudice-extracted.txt to the current working directory. This could be useful if you want to run a kind of bag-of-words analysis on a text, but don’t want to have to do a lot of data cleanup yourself. 

## Installation 

Chapterize is now on PyPi, installable with `pip`. You can install it with: 

```
sudo pip3 install chapterize
```

Or, to get the very latest version from GitHub, run: 

```
git clone https://github.com/JonathanReeve/chapterize.git
cd chapterize
sudo pip3 install .
```

## State

This tool is in a pre-alpha state. There are a lot of types of chapter headings it can’t recognize. That having been said, if it doesn’t work with your text, please open up an issue here and describe the error messages you’re seeing. Please include a URL to the text you’re using. 

## Tested With

Chapterize has been tested successfully with these Project Gutenberg ebooks. Feel free to add yours to this list if you can get it to work with your text. 

* A Study in Scarlet
* A Tale of Two Cities
* Anna Karenina
* Frankenstein
* Huckleberry Finn
* Madame Bovary
* Middlemarch
* Moby Dick
* Oliver Twist
* Pride and Prejudice
* The Brothers Karamazov
* The Call of the Wild
* The Secret Agent
* The Turn of the Screw
* The War of the Worlds
* The Wind in the Willows
* This Side of Paradise
* Through the Looking Glass
* Treasure Island
* Uncle Tom’s Cabin
* Wuthering Heights

## Contributing

Pull requests welcome! Feel free to hack away on it to whatever extent you wish.
