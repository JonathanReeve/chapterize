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
        print(self.headings)

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
        pat = re.compile('[Cc]hapter \d+')
        headings = [(self.lines.index(line), pat.match(line)) for line in self.lines if pat.match(line) is not None] 
        logging.info('Headings: %s' % headings) 
        return headings

if __name__ == '__main__':
    cli()
