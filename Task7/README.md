# task7
![solver1](https://github.com/Chabuei/DQN_Practice/assets/102859047/af98cdc3-22d6-4d8a-9bce-7b8e633b615f)
![solver2](https://github.com/Chabuei/DQN_Practice/assets/102859047/be5c4e79-808d-4bc5-8ce0-e57b41103205)<br>
・1は移動可能場所を表す<br>
・0は移動不可能場所を表す<br>
・[数字]は棚を表し、数字は棚名を表す<br>
・→はその地点からの参照可能場所を表す<br>
・画像上部のstep、Current optimized the sum of total distances of users　レイアウトの試行回数と、各オーダーの総移動距離の合計値を表示(より小さい値になっており、最適なレイアウトに近づいてることがわかる)<br>
・BFSで閉路がないか確認しているので絶対に閉路は発生しないが、時々参照できない位置に方角が指定されてしまうことがあるのでそれは改善したい(そうならないサブルーチンは組んであるが、カバーしきれていないパターンがある)。<br>
・今回はより少ない移動距離ですべてを取得できるレイアウトというクライアント目線でしか評価できていないので、task6の知見なども取り入れてオーナー目線(クライアントが欲しいもの以外でより多くの商品をクライアントに見てもらいたい)でも評価できるようなものにしていきたい。<br>
・Product listと Layputs of productsはそれぞれアルゴリズムの適用前後での各商品がどの棚に陳列されているか(belong to the shelve of)を表している。たしかに、変化しているのがわかる。
