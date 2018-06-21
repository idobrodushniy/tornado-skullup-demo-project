from invoke import task


@task
def startTornadoApp(ctx):
    ctx.run('python3 -m tornado_app.main')
