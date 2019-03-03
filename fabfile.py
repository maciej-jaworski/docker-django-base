from fabric.api import local


def ssh(service):
    assert service in ['backend', 'database'], "%s is unrecognized service"
    local('docker-compose exec %s bash' % service)


def managepy(command=''):
    cmd = 'docker-compose exec backend python manage.py {}'.format(command)
    local(cmd)


def compose():
    local(' docker-compose stop && docker-compose up --build --abort-on-container-exit --remove-orphans')
