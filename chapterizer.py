import click
import logging
import re

@click.command()
@click.argument('book')
@click.option('--verbose', is_flag=True, help='Get extra information about what\'s happening behind the scenes.')
@click.option('--debug', is_flag=True, help='Turn on debugging messages.')
@click.version_option('0.1')
def cli(book, verbose, debug):
    """ This tool breaks up a book into chapters. 
    """

    if verbose:
        logging.basicConfig(level=logging.INFO)

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    logging.info('Now attempting to break the file %s into chapters.' % book)

    bookObj = Book(book)

class Book(): 
    def __init__(self, filename): 
        self.filename = filename
        self.contents = self.getContents()
        self.lines = self.getLines()
        self.headings = self.getHeadings()
        self.headingLocations = [heading[0] for heading in self.headings]
        self.ignoreTOC()
        headingsPlain = [self.lines[loc] for loc in self.headingLocations]
        logging.info('Headings: %s' % headingsPlain) 
        logging.info('Heading locations: %s' % self.headingLocations) 
        self.chapters = self.getTextBetweenHeadings()
        # logging.info('Chapters: %s' % self.chapters) 
        self.endLocation = self.getEndLocation() 
        self.numChapters = len(self.chapters)
        self.writeChapters()

    def getContents(self): 
        """
        Reads the book into memory. 
        """
        with open(self.filename) as f: 
            contents = f.read()
        return contents

    def getLines(self): 
        """ 
        Breaks the book into lines.
        """
        return self.contents.split('\n')

    def getHeadings(self): 
        pat = re.compile('chapter (\d+|(C|I|V|X|L))', re.IGNORECASE)
        headings = [(self.lines.index(line), pat.match(line)) for line in self.lines if pat.match(line) is not None] 
        endLocation = self.getEndLocation()

        # Treat the end location as a heading. 
        headings.append((endLocation, None))
        return headings

    def ignoreTOC(self): 
        """
        Filters headings out that are too close together, 
        since they probably belong to a table of contents. 
        """
        lastHeading = len(self.headingLocations) - 1
        newHeadings = self.headingLocations
        for i, headingLocation in enumerate(self.headingLocations): 
            print('lastheading: ', lastHeading)
            print('i: ', i)
            if i is not lastHeading: 
                nextHeadingLocation = self.headingLocations[i+1]
                delta = nextHeadingLocation - headingLocation
                if delta < 4: 
                    # Include only headings that are fewer than 
                    # four lines apart from the next one. 
                    index = self.headingLocations.index(headingLocation)
                    del newHeadings[index]
                    del newHeadings[index+1]
        self.headingLocations = newHeadings

    def getEndLocation(self): 
        """
        Tries to find where the book ends. 
        """
        ends = ["End of the Project Gutenberg EBook", 
                "End of Project Gutenberg's"]
        joined = '|'.join(ends) 
        pat = re.compile(joined, re.IGNORECASE)
        endLocation = None
        for line in self.lines: 
            if pat.match(line) is not None: 
                endLocation = self.lines.index(line) 
                self.endLine = self.lines[endLocation] 
                break

        if endLocation is None: # Can't find the ending. 
            logging.info("Can't find an ending line. Assuming that the book ends at the end of the text.")
            endLocation = len(self.lines)-1 # The end
            self.endLine = 'None' 

        logging.info('End line: %s at line %s' % (self.endLine, endLocation)) 
        return endLocation

    def getTextBetweenHeadings(self):
        chapters = []
        lastHeading = len(self.headingLocations) - 1
        for i, headingLocation in enumerate(self.headingLocations):
            if i is not lastHeading: 
                nextHeadingLocation = self.headingLocations[i+1]
                chapters.append(self.lines[headingLocation+1:nextHeadingLocation])
        return chapters

    def zeroPad(self, numbers): 
        """ 
        Takes a list of ints and zero-pads them, returning
        them as a list of strings. 
        """
        maxNum = max(numbers) 
        maxDigits = len(str(maxNum))
        numberStrs = [str(number).zfill(maxDigits) for number in numbers] 
        return numberStrs

    def writeChapters(self): 
        chapterNums = self.zeroPad(range(1, len(self.chapters)+1))
        logging.debug('Writing chapter headings: %s' % chapterNums)
        dir = 'chapters'
        ext = '.txt'
        for num, chapter in zip(chapterNums, self.chapters):
            path = dir + '/' + num + ext
            logging.debug(chapter)
            chapter = '\n'.join(chapter)
            with open(path, 'w') as f: 
                f.write(chapter)

if __name__ == '__main__':
    cli()
