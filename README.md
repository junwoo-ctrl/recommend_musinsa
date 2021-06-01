# recommend_musinsa

# commands
- 사전에 docker, pyenv가 설치되어 환경을 마련해야함.
- `requirements.txt` 설치 후 아래 커맨드 실행.

```
# image build
$ ENV=dev; python3 env_tools.py build

# infra setup
$ ENV=dev; python3 env_tools.py setup

# image test
$ ENV=dev; python3 env_tools.py test
```


# 더 해야할 것
- docker 내부 path 수정.
- rocust 기반 stress test.
