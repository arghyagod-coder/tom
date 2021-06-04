import click
import pickle
import subprocess as sb
from click.utils import echo
from buildkit import buildPython, buildPygame

def run(command):
    sb.run(command, shell=True)

langs = ['1. python', '2. go', '3. py-pkg', '4. java', '5. c', '6. c++', '7. webdev', '8. flask', '9. pygame', '10. django', '11. swift', '12. py-ml', '13. CLI']
licenses = ['apache', 'mit', 'gpl', 'bsd', 'epl', 'mpl', 'uni']

@click.group()
@click.version_option('0.1.4', prog_name='Lola')
def main():
    '''I am Tom, and I will help you build your project structure'''
    pass

@main.command('list')
@click.argument('arg1', nargs=1)
def list(arg1):
    '''list a particular set of supported arguments'''
    if arg1.lower()=='langs':
        click.echo('Tom supports these languages currently \n\n')
        for lang in langs:
            print(lang)
        print('\n')

    elif arg1.lower()=='license':
        click.echo('Available Licenses:  \n\n')
        for licensee in licenses:
            print(licensee)
        print('\n')

    else:
        click.echo('Invalid Argument')

@main.command('config', help='Setup your details for Tom')
@click.argument('id', nargs=1)
def conf(id):
    global uname
    global ghname
    global glang
    global ulic
    if id=='name':
        uname = click.prompt('Enter your Username: ')
        click.echo(f'{uname} was set as the Catname! :)')
        pickle.dump(uname, open('tom//config//uname.dat', 'wb'))
    elif id=='github-username':
        ghname = click.prompt('Enter your github username: ')
        click.echo(f'{ghname} was set as the Cheesename! :)')
        pickle.dump(ghname, open('tom//config//ghname.dat', 'wb'))
    elif id=='lang':
        glang = click.prompt('Enter your default language: ')
        click.echo(f'{glang} was set as the default language! :)')
        pickle.dump(glang, open('tom//config//dlang.dat', 'wb'))
    elif id=='lic':
        ulic = click.prompt('Enter your default license: ')
        click.echo(f'{ulic} was set as the default license! :)')
        pickle.dump(ulic, open('tom//config//ulic.dat', 'wb'))
    else:
        click.echo('Invalid Input!')


@main.command('profile', help='View your profile registered for Tom')
def profile():
    try:
        uname = pickle.load(open('tom/config/uname.dat', 'rb'))
        ghname = pickle.load(open('tom/config/ghname.dat', 'rb'))
        dlang = pickle.load(open('tom/config/dlang.dat', 'rb'))
        ulic = pickle.load(open('tom/config/ulic.dat', 'rb'))
        click.echo(f'''User Profile

Username: {uname}
Github ID: {ghname}
Default Language: {dlang}
Default License: {ulic}

All set!''')
    except Exception as e:
        click.echo("\n You have not setup your account properly! But you can do it by 'tom config name' and 'tom config github-username' \n")
            

if __name__=='__main__':
    main()

