# Online Judge Tools Wrapper

[atcoder-cli](https://github.com/Tatamo/atcoder-cli)用の[Online Judge Tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)極薄ラッパー

## やりたいこと

* コンテストディレクトリ直下から`oj`コマンド、`acc`コマンドを実行

### テスト

`ojw test|t task [filename] [Options]`

1. 必要ならコンパイル
1. サンプルケースのテスト (oj t)
    * sourceの指定がなければ既定のファイルをテスト

Options:

* `-c --case <casename>`
    - テストケースを指定
    - `-c 1`と指定すれば`sample-1`がテストされる
* `-p --passed <passed options>`
    - oj側に渡されるオプション

### 提出

`ojw submit|s task [source]`

1. `cd {task} && acc submit`とほぼ等価
