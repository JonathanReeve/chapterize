import click
import logging

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
        self.contents = self.readFile(filename)

    def readFile(self, book): 
        """
        Reads the book into memory. 
        """
        with open(book) as f: 
            contents = f.read()
        print(contents[:50])

if __name__ == '__main__':
    cli()
