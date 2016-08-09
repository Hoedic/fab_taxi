from __future__ import with_statement
import importlib
from fabric.api import *
from fabric.contrib.console import confirm

from fabtools import supervisor

from load_config import load_config
from machine import install_machine, restart_services, install_system, install_fluentd
from geoserver import deploy_geoserver, restart_geotaxi
from tuning import tune_system
from api import deploy_api, clean_directories, test_uwsgi_is_started
from zupc import import_zupc
from dash import *
from env import env, load_config_dev, load_config_test, load_config_prod, load_config_local
import logging
logging.basicConfig()


@task
def deploy():
    load_config()
    install_machine()
    supervisor.update_config()
    tune_system()
    restart_services()
    deploy_api()
    deploy_geoserver()
    restart_geotaxi()
