import click
import knowlify
import config


@click.command()
@click.argument('filename_or_url', type=click.STRING, default='https://en.wikipedia.org/wiki/Mathematics')
@click.option('-p','path', type=click.STRING, default=config.DATA_DIR)
def main(filename_or_url, path):
    return None


if __name__ == '__main__':
    main()
