# task3 and 5
task5の内容はtask3の派生であるため、ここではtask3とtask5をまとめて説明する<br>
![result](https://github.com/Chabuei/DQN_Practice/assets/102859047/d3c6a589-a8a4-4f61-a303-7a5ad0b61b65)
・1は移動可能場所を表す<br>
・0は移動不可能場所を表す<br>
・[数字]は製品を表し、数字は製品名を表す<br>
・→はその地点からの参照可能場所を表す<br>
・画像上部のstep、current optimized distance of the order No.x　は2-optの実行回数と各オーダーごとのその時点での最適ルートによる移動距離を表す<br>
・BFSで閉路がないか確認しているので絶対に閉路は発生しないが、時々参照できない位置に方角が指定されてしまうことがあるのでそれは改善したい(そうならないサブルーチンは組んであるが、カバーしきれていないパターンがある)。
