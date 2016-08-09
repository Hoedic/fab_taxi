from os import path
from fabric.api import env, task

def make_default_values():
    if not hasattr(env, 'apitaxi_dir'):
        env.apitaxi_dir = lambda now: env.deployment_dir(now) + '/APITaxi-master'
    if not hasattr(env, 'fronttaxi_dir'):
        env.fronttaxi_dir = lambda now: env.deployment_dir(now) + '/APITaxi_front-master'
    if not hasattr(env, 'uwsgi_api_config_path'):
        env.uwsgi_api_config_path = lambda now: env.apitaxi_dir(now) + '/uwsgi_api.ini'
    if not hasattr(env, 'uwsgi_front_config_path'):
        env.uwsgi_front_config_path = lambda now: env.fronttaxi_dir(now) + '/uwsgi_front.ini'
    if not hasattr(env, 'uwsgi_api_file'):
        env.uwsgi_api_file = lambda now: env.apitaxi_dir(now) + '/api_taxi.uwsgi'
    if not hasattr(env, 'uwsgi_front_file'):
        env.uwsgi_front_file = lambda now: env.fronttaxi_dir(now) + '/front_taxi.uwsgi'
    if not hasattr(env, 'apitaxi_venv_path'):
        env.apitaxi_venv_path = lambda now: env.deployment_dir(now) + '/venvAPITaxi'
    if not hasattr(env, 'apitaxi_config_path'):
        env.apitaxi_config_path = lambda now: env.apitaxi_dir(now) + '/APITaxi/prod_settings.py'
    if not hasattr(env, 'fronttaxi_config_path'):
        env.fronttaxi_config_path = lambda now: env.fronttaxi_dir(now) + '/APITaxi_front/prod_settings.py'
    if not hasattr(env, 'geotaxi_authentication'):
        env.geotaxi_authentication = False

@task
def load_config_dev():
    env.name = 'dev'
    env.hosts = ['dev.api.taxi']
    env.user = 'deploy'
    env.use_ssh_config = True

    env.deploy_dir = '/srv/www'
    env.deployment_dir = lambda now: env.deploy_dir + '/deployment_{}'.format(now)

    env.wsgi_processes = 8
    env.wsgi_threads = 10
    env.uwsgi_logdir = '/var/log/uwsgi'
    env.uwsgi_launcher_logdir = '/var/log/uwsgi_launcher'
    env.uwsgi_pid_dir = '/var/run/uwsgi'
    env.uwsgi_api_pid_file = lambda now: '{}/uwsgi_api_{}.pid'.format(env.uwsgi_pid_dir, now)
    env.uwsgi_front_pid_file = lambda now: '{}/uwsgi_front_{}.pid'.format(env.uwsgi_pid_dir, now)

    env.server_name = 'dev.api.taxi'

    env.somaxconn = 65535
    env.tcp_max_syn_backlog = 65535

    env.uwsgi_socket_dir = '/var/run/uwsgi_socket'
    env.uwsgi_socket_api = lambda now: env.uwsgi_socket_dir + '/apitaxi_{}.sock'.format(now)
    env.uwsgi_socket_front = lambda now: env.uwsgi_socket_dir + '/fronttaxi_{}.sock'.format(now)
    env.postgres_locale = 'fr_FR.UTF-8'
    env.local_redis_conf = 'files/redis.conf'

    env.influx_conf = '/etc/influxdb/influxdb.conf'
    env.influx_db_dir = '/var/influx'
    env.geoserver_port = 80
    env.apitaxi_archive = u'https://github.com/hoedic/APITaxi/archive/{}.zip'
    env.fronttaxi_archive = u'https://github.com/openmaraude/APITaxi_front/archive/master.zip'
    env.geotaxi_authentication = True
    make_default_values()

@task
def load_config_local():
    env.name = 'local'
    env.hosts = ['127.0.0.1:2223']
    env.server_name = 'localhost'

@task
def load_config_test():
    env.name = 'test'
    env.hosts = ['test.api.taxi']
    env.user = 'deploy'
    env.use_ssh_config = True

    env.deploy_dir = '/srv/www'
    env.deployment_dir = lambda now: env.deploy_dir + '/deployment_{}'.format(now)

    env.wsgi_processes = 8
    env.wsgi_threads = 10
    env.uwsgi_logdir = '/var/log/uwsgi'
    env.uwsgi_launcher_logdir = '/var/log/uwsgi_launcher'
    env.uwsgi_pid_dir = '/var/run/uwsgi'
    env.uwsgi_api_pid_file = lambda now: '{}/uwsgi_api_{}.pid'.format(env.uwsgi_pid_dir, now)
    env.uwsgi_front_pid_file = lambda now: '{}/uwsgi_front_{}.pid'.format(env.uwsgi_pid_dir, now)

    env.server_name = 'test.api.taxi'

    env.somaxconn = 65535
    env.tcp_max_syn_backlog = 65535

    env.uwsgi_socket_dir = '/var/run/uwsgi_socket'
    env.uwsgi_socket_api = lambda now: env.uwsgi_socket_dir + '/apitaxi_{}.sock'.format(now)
    env.uwsgi_socket_front = lambda now: env.uwsgi_socket_dir + '/fronttaxi_{}.sock'.format(now)
    env.postgres_locale = 'fr_FR.UTF-8'
    env.local_redis_conf = 'files/redis.conf'

    env.influx_conf = '/etc/influxdb/influxdb.conf'
    env.influx_db_dir = '/var/influx'
    env.geoserver_port = 80
    env.apitaxi_archive = u'https://github.com/openmaraude/APITaxi/archive/{}.zip'
    env.fronttaxi_archive = u'https://github.com/openmaraude/APITaxi_front/archive/master.zip'
    env.geotaxi_authentication = True
    make_default_values()

@task
def load_config_prod():
    env.name = 'prod'
    env.hosts = ['api.taxi']
    env.user = 'deploy'
    env.use_ssh_config = True

    env.deploy_dir = '/srv/www'
    env.deployment_dir = lambda now: env.deploy_dir + '/deployment_{}'.format(now)

    env.wsgi_processes = 24
    env.wsgi_threads = 10
    env.uwsgi_logdir = '/var/log/uwsgi'
    env.uwsgi_launcher_logdir = '/var/log/uwsgi_launcher'
    env.uwsgi_pid_dir = '/var/run/uwsgi'
    env.uwsgi_api_pid_file = lambda now: '{}/uwsgi_api_{}.pid'.format(env.uwsgi_pid_dir, now)
    env.uwsgi_front_pid_file = lambda now: '{}/uwsgi_front_{}.pid'.format(env.uwsgi_pid_dir, now)

    env.server_name = 'api.taxi'

    env.somaxconn = 65535
    env.tcp_max_syn_backlog = 65535

    env.uwsgi_socket_dir = '/var/run/uwsgi_socket'
    env.uwsgi_socket_api = lambda now: env.uwsgi_socket_dir + '/apitaxi_{}.sock'.format(now)
    env.uwsgi_socket_front = lambda now: env.uwsgi_socket_dir + '/fronttaxi_{}.sock'.format(now)
    env.postgres_locale = 'fr_FR.UTF-8'
    env.local_redis_conf = 'files/redis.conf'

    env.influx_conf = '/etc/influxdb/influxdb.conf'
    env.influx_db_dir = '/var/influx'
    env.geoserver_port = 80
    env.apitaxi_archive = u'https://github.com/openmaraude/APITaxi/archive/{}.zip'
    env.fronttaxi_archive = u'https://github.com/openmaraude/APITaxi_front/archive/master.zip'
    make_default_values()


env.contours_fichier = u'http://osm13.openstreetmap.fr/~cquest/openfla/export/communes-20150101-5m-shp.zip'
env.zupc_fichier = u'https://www.data.gouv.fr/s/resources/zones-uniques-de-prises-en-charge-des-taxis-zupc/20151023-174638/zupc.geojson'
env.shell = '/bin/bash -l -i -c'
