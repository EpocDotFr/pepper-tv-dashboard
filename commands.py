from ptvd import app
import click


@app.cli.command()
def cc():
    """Clear the cache."""
    from ptvd import cache

    click.echo('Clearing cache')

    cache.clear()

    click.secho('Done', fg='green')
