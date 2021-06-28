# Online Judge Tools Wrapper

[atcoder-cli](https://github.com/Tatamo/atcoder-cli)用の[Online Judge Tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)極薄ラッパー

## やりたいこと

**操作はコンテストディレクトリ直下から**

### テスト部分を自動化

`ojw test|t task [filename] [Options]`

Options:
- -p --passed \<passed options\>    oj側に渡されるオプション

1. 必要ならコンパイル
1. サンプルケースのテスト (oj t)
    * sourceの指定がなければ既定のファイルをテスト
    * oj側に引数を渡す


<!-- * `ojw submit|s tasklabel [source]` -->
