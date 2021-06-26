# Online Judge Tools Wrapper

[atcoder-cli](https://github.com/Tatamo/atcoder-cli)用の[Online Judge Tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)極薄ラッパー

## やりたいこと

### テスト部分を自動化

`ojw test|t [filename] [Options]`

Options:
<!-- - -c --compile                      コンパイルを（強制）実行 -->
- -p --passed \<passed options\>    oj側に渡されるオプション

1. 必要ならコンパイル
1. サンプルケースのテスト (oj t)
    * sourceの指定がなければ既定のファイルをテスト
    * oj側に引数を渡す

<!-- コマンドをコンテストディレクトリから扱う

* `ojw submit|s tasklabel [source]` -->
