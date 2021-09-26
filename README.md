# mac2vendor

MACアドレスからベンダー名を取得して表示する。

oui.csvファイルを読み込んでオフラインで処理します。

Cisco機器の show arp や arp -an などの結果を矩形選択で貼り付けなどして使うイメージです。

MACアドレスの表記は、「ab-cd-ef-00-11-22」や、「AA:BB:CC:00:11:22」や、「aabb.cc00.1122」など区切り文字は、「-」、「:」、「.」に対応

MA-Lの範囲に対応。

## 必要ファイル

 - mac2vendor_gui.exe
 - oui.csv

## 使い方

mac2vendor_gui.exe を実行
 
![image](https://user-images.githubusercontent.com/19838489/134797372-2260becd-5d00-4a6b-9c35-237443c3c547.png)

MACアドレスをフォームに入力して OK クリックでベンダー情報が別ウィンドウに表示される。

![image](https://user-images.githubusercontent.com/19838489/134797498-0d566fbf-3b5f-4e7a-b489-9632733a8572.png)

## oui.csvファイルのUpdate

以下のバッチファイル等でアップデートください。

update_oui-csv.bat

取得URLは以下です。

http://standards-oui.ieee.org/oui/oui.csv
