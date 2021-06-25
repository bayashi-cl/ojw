# Online Judge Tools Wrapper

[Online Judge Tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)の極薄ラッパー

## やりたいこと

[atcoder-cli](https://github.com/Tatamo/atcoder-cli)と[oj-prepare](https://github.com/online-judge-tools/template-generator)を足してnで割っている

* `ojw new {contest_id}`
    1. ディレクトリの作成
        * ターゲットの指定 (`--target, -t {target_dir}`)
    1. テンプレートの貼り付け
        * 言語指定 (`--lang, -l {language}`)
    1. サンプルケースのダウンロード (oj d)
* `ojw test {source}`
    1. 必要ならコンパイル
    1. サンプルケースのテスト (oj t)
        * テストケース指定 (`--case, -c {test_name}`)
        * テストケース手入力 (`--interactive, -i`)
        * 誤差ジャッジ (`--error, -e`)
* `ojw submit {source}`
    1. 事前テスト (`--force, -f`で無効)
    1. 提出 (oj s)
        * 言語指定 (`--lang, -l {language}`)
            * デフォルトは拡張子依存
            * c++, python, pypy

## 特化すること

* ソースファイル名を`a.py`のようにすることで、問題を指定する
* ディレクトリ構造は

```
{contest_id}/
    ├ a.py||.cpp
    ├ b.py||.cpp
    ├ ...
    ├ f.py||.cpp
    ├ info
    └ tests/
        ├ a/
        ...
```
