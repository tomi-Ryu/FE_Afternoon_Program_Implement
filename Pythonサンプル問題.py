"""

仕様書ソースURL
https://www.seplus.jp/dokushuzemi/ec/fe/fenavi/guide/sample_question_python/

基本的に一部の仕様(上記ページの最初の仕様説明部のみ)を見て実装。
サンプル問題の解答ソースコード同様、想定外の入力には一切対応しない。
以前に解答ソースコードに目を通したり、ヒントを得るために少し解答ソースコードを見た。

"""


"""

draw関数の引数が空文字列の時、エラーのはず

"""


import math  # 数学関数の標準ライブラリ 
import matplotlib.pyplot as plt  # グラフ描画の外部ライブラリ

class Marker():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.angle = 0
    plt.xlim(-320, 320)  # x軸の表示範囲を設定 
    plt.ylim(-240, 240)  # y軸の表示範囲を設定 
  
  def Forward(self, val: float):
    # math.radians / 度数法で表した角度を，ラジアンで表した角度に変換 
    angle_rad = math.radians(self.angle)
    next_x = self.x + val * math.cos(angle_rad)
    next_y = self.y + val * math.sin(angle_rad)
    plt.plot([self.x, next_x], [self.y, next_y], color='black', linewidth=2)
    self.x = next_x
    self.y = next_y

  def Turn(self, val: float):
    self.angle = (self.angle + val) % 360

  def draw(self, commandStr: str):
    # 命令文解析と命令実行準備
    perCommandList = commandStr.split(";")
    commandIdx = 0
    maxCommandIdx = len(perCommandList) - 1
    stackForRepetitionCmd = []

    while commandIdx <= maxCommandIdx:
      # 命令解析
      Cmd = perCommandList[commandIdx]
      CmdCode, numberParams = Cmd[0], float(Cmd[1:])

      # 通常、1だけ進める
      nextCommandIdx = commandIdx + 1
      #　命令実行
      if CmdCode == "F":
        self.Forward(numberParams)
      elif CmdCode == "T":
        self.Turn(numberParams)
      elif CmdCode == "R":
        stackForRepetitionCmd.append({"CmdIdx":commandIdx, "Rest":numberParams})
      elif CmdCode == "E":
        relatedCmdInfo = stackForRepetitionCmd[-1]
        if relatedCmdInfo["Rest"] == 1:
          stackForRepetitionCmd.pop()
        else:# まだ繰り返す(値が2以上)
          relatedCmdInfo["Rest"] -= 1
          nextCommandIdx = relatedCmdInfo["CmdIdx"] + 1
      # 次に実行する命令内容のIdx(OR maxCommandIdx + 1となりwhile文脱出)
      commandIdx = nextCommandIdx
    
    self.show()

  def show(self):
    plt.show()


marker = Marker()
marker.draw("R3;R4;F100;T90;E0;F100;E0")