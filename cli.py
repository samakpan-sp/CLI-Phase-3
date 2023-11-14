import click
from task_manager.models import User, Task, engine
from task_manager.models import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('username')
def add_user(username):
    user = User(username=username)
    session.add(user)
    session.commit()
    click.echo(f'User {username} added successfully.')

@cli.command()
def list_users():
    users = session.query(User).all()
    for user in users:
        click.echo(f'User ID: {user.id}, Username: {user.username}')

# Other CLI commands can be added for tasks, etc.
