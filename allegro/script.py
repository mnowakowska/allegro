from lib import downolad_data
from lib import AllegroError
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-k",
                  action="store_false", default=True,
                  help="key")
(options, args) = parser.parse_args()


def main():
    try:
        url, price = downolad_data(' '.join(args))
    except AllegroError as e:
        print e
    except Exception as e:
        print e
    else:
        return 'Price: %s, Url: %s' % (price, url)
