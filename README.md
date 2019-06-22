# av-tools

## aconfig.py

背定ファイル、aconfig.json を読み描きするライブラリ。

```
$ cat aconfig.json 
{
    "sample_width" : 1,
    "unsigned" : false,
    "channels" : 1,
    "rate" : 8000,
    "chunk" : 512,
    "device_index" : 0,
    "duration": -1
}
```
- duration: 単位：秒

## aread.py

設定ファイルを読み込み、標準出力にバイナリで出力する。

- duration時間分出力したら停止する。
- duration設定が-1の場合 Ctl+Cまで止まらない。


## awave.py

wavファイルを作成

-  WAVファイル名: awave.wav
```
$ python aread.py | python awave.py
```

## alevel.py

```
$ python aread.py | python alevel.py
```

### afft.py

```
$ python aread.py | python afft.py
```

## ainfo.py

WAF ファイルの上表を表示する

```
$ python ainfo.py output.wav
```
