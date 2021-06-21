# Online Judge Tools Wrapper

[Online Judge Tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)の極薄ラッパー

## やりたいこと

[atcoder-cli](https://github.com/Tatamo/atcoder-cli)と[oj-prepare](https://github.com/online-judge-tools/template-generator)を足してnで割っている

* `ojw new {contest_id}`
    * ディレクトリの作成
    * テンプレートの貼り付け
    * サンプルケースのダウンロード(oj d)
* `ojw test {source}`
    * サンプルケースのテスト(oj t)
    * 必要ならコンパイル
* `ojw submit {source}`
    * 提出(oj s)

## 特化すること

* ソースファイル名を`{problem_id}.py`のようにすることで、問題を指定する
* ディレクトリ構造は

```
{contest_id}/
    ├ a.py
    ├ b.py
    ├ ...
    ├ f.py
    ├ info
    └ tests/
        ├ a/
        ...
```
