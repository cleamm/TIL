# git 기초

## 개념
- vcs(Version Control System)
- Git vs Github
  - Working Directory
  - Stage
  - Commit

## 명령어
```
$ git init
$ git config --global user.name 'cleamm'
$ git config --global user.email 'ehdgus275@naver.com'
$ touch <filename> <- 파일 생성
$ git add <file> <- stage 업로드
$ git restored staged <file> <- stage 내림
$ git commit -m 'message' <-커밋
$ git push origin master <-푸시
```

`` ` `` = (quote=백틱)


## `init`
```
$ git init
```

## `commit`
```
$ git add .
$ git commit -m 'MESSAGE'
```

## `remote add`
```
# github 에 원격 저장소(repository) 생성 후 URL 획득
$ git remote add origin 'URL'
```
여기서 origin을 다른 명칭으로 변경해서 사용해도 되나 그런 경우 push 등에서도 여기서 사용된 명칭을 이용해야함.

## `push`
```
$ git push origin master
```

## `pull`
```
$ git pull origin (branch-name = master)
```

## `clone`
```
# 현재 터미널의 위치에 다운로드
$ git clone 'remote repo URL'
```

## `branch`
```
# 브랜치 생성
$ git branch (branch name)
# 브랜치 삭제
$ git branch -d (branch name)
```

## `switch`
```
# 브랜치 변경(head 변경)
$ git switch (branch name)
# 브랜치 생성 및 변경
$ git switch -c (new-branch name)
```

## `merge`
```
# 브랜치 병합
$ git merge (target-branch name)
```

## `vim`
```
# 파일 수정
$ vim (filename)
$ (write)
$ ESC
$ ':wq'(=exit)
```