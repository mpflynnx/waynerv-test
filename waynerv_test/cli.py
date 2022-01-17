"""Console script for waynerv_test."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("waynerv-test")
    click.echo("=" * len("waynerv-test"))
    click.echo("Skeleton project created by Cookiecutter PyPackage")

# Just some random text for next version bump tag 0.1.1




if __name__ == "__main__":
    main()  # pragma: no cover
