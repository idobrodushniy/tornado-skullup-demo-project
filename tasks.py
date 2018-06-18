from invoke import task


@task
def startTornadoApp(ctx):
    print('enabled!')
    ctx.run('python3 ./tornado_app/server.py')
