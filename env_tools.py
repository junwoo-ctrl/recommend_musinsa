# Implement

### docker
### 0. database setup
### 1. generate commit id d
### 2. generate tag name d
### 3. build docker image d

import subprocess
import re

from clize import run

from server.util.tools import EnvTool


def get_git_commit_id() -> str:
    a = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    git_commit_id = a.decode(encoding='utf-8').strip()
    assert len(git_commit_id) == 40
    assert re.match('^[a-fA-F0-9]+$', git_commit_id)
    return git_commit_id


def get_image_latest() -> str:
    base_image_name = 'server'
    tag = 'musinsa'
    return ':'.join([base_image_name, tag])


def get_base_image_name() -> str:
    return 'mysql:8.0'


def run_commands(commands: str):
    subprocess.run(
        commands,
        shell=True,
        executable='/bin/bash',
        check=True,
    )


def build_image():
    git_commit_id = get_git_commit_id()
    image_latest = get_image_latest()
    base_image = get_base_image_name()
    build_env = EnvTool.get_env()

    commands = f"""
        set -x
        set -e
        VER={git_commit_id}
        echo git_commit_id=$VER
        docker build --label env={build_env} --label git-commit-id=$VER --build-arg BASE_IMAGE={base_image} \
        -t {image_latest} .
        echo done : git-commit-id is $VER
        echo done : build image '{image_latest}'
    """
    run_commands(commands)


def test():
    git_commit_id = get_git_commit_id()
    image_latest = get_image_latest()
    base_image = get_base_image_name()
    build_env = EnvTool.get_env()

    commands = f"""
        set -x
        set -e
        echo test : {image_latest} start!
        docker run -v `pwd`/tests/:/app/tests -v `pwd`/src:/app/src -e ENV={build_env} \
        {image_latest} test
    """
    run_commands(commands)



if __name__ == '__main__':
    run({
        'build': build_image,
        'test': test,
    })
