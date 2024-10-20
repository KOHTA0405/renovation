# renovation
リノベーション計画の際に使用するプログラム

# 参照した記事
## ライブラリの使用方法
### gspread
* [[Python] GoogleドライブのフォルダにGoogleスプレッドシートを新規作成する2つの実装方法](https://note.com/kohaku935/n/nf69f13012eb8)
* [gspread で Python から Google スプレッドシートを扱えるようにするまで](https://zenn.dev/yamagishihrd/articles/2022-09_01-google-spreadsheet-with-python#fn-d711-5)

### dlt
* [dltでウェザーニュースの花粉APIからデータをロードする](https://zenn.dev/oxon/articles/cb36b5488da940)
* [【dltHub Docs】Tutorial](https://zenn.dev/yuichi_dev/articles/571253644f5f08)

## その他
* [駅名から所在地を取得するコマンド](https://lookbackmargin.blog/2019/08/31/address-from-station-name/)

## dltについて
### エラー遭遇
* 初回実行後、ターゲットのテーブルを削除したらエラー
* おそらくは、incrementalの設定になっていたからだとは思うが、.dlt/pipelineフォルダの中身を消してもエラーだった
* BQ上にあるdltのメタデータを削除したらもう一度動いた