import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Importa a classe gerada pelo arquivo convertido ui_interface.py
from fe15main import Ui_MainWindow

import banco
import calculos


class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()

    # Instancia e configura a interface desenhada no Qt Designer
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # Exemplo de conexão de evento e alteração de texto:
    # self.ui.meuBotao.clicked.connect(self.minha_funcao)
    self.ui.btnCalcular.clicked.connect(self.calcular)

    if self.ui.cbbPersonagem.count() > 0:
      self._on_personagem_changed(self.ui.cbbPersonagem.currentText())

  # Conexão com o banco de dados SQLite
    try:
      self.con, self.cur = banco.conectar()
    except Exception as e:
      QMessageBox.critical(
          self,
          "Erro de Conexão",
          f"Não foi possível conectar ao banco 'calcfe.db':\n{e}",
      )
      sys.exit(1)

    self.ui.cbbPersonagem.currentTextChanged.connect(
        self._on_personagem_changed
    )

    self.ui.cbbClasse.currentTextChanged.connect(
        self._on_classe_changed
    )

    self.ui.spbLevel.textChanged.connect(
      self._on_level_changed
    )

    self._load_characters()

  def _load_characters(self):
    try:
      self.cur.execute("SELECT name FROM characters ORDER BY name")
      # O fetchall retorna as linhas. Adaptado conforme o seu banco (dicionário/Row ou tupla)
      rows = self.cur.fetchall()

      chars = [
          row["name"] if isinstance(row, dict) else row[0] for row in rows
      ]

      self.ui.cbbPersonagem.clear()
      self.ui.cbbPersonagem.addItems(chars)

      # Dispara a atualização inicial para o primeiro personagem da lista
      if chars:
        self._on_personagem_changed(self.ui.cbbPersonagem.currentText())
    except Exception as e:
      QMessageBox.critical(
          self, "Erro SQL", f"Erro ao buscar personagens:\n{e}"
      )


  # TROCA DE PERSONAGEM
  def _on_personagem_changed(self, selected_char):
    """Atualiza as classes permitidas no cbbClasse de acordo com o personagem selecionado."""
    if not selected_char:
      self.ui.cbbClasse.clear()
      return

    try:
      caminho_recurso = f":/portraits/{selected_char}.png"

      self.ui.portrait.setStyleSheet(f"""
            border-image: url({caminho_recurso}) 0 0 0 0 stretch stretch;
            background-color: rgba(255, 255, 255, 0);
            border: 2px solid #682f28;
            border-radius: 6px;
        """)
    except Exception as e:
      pass

    try:
      # Busca as classes permitidas no banco chamando o módulo banco.py
      allowed_classes = banco.get_classes_for_char(self.cur, selected_char)
      # Suporta tanto retorno em tupla `(id, nome)` quanto `dict`
      class_names = [
          cls[1] if isinstance(cls, (tuple, list)) else cls["name"]
          for cls in allowed_classes
      ]

      self.ui.cbbClasse.clear()
      self.ui.cbbClasse.addItems(class_names)

      self.calcular()

    except Exception as e:
      QMessageBox.critical(self, "Erro SQL", f"Erro ao buscar classes:\n{e}")


  # TROCA DE CLASSE
  def _on_classe_changed(self, selected_class):
    if not selected_class:
      return

    self.calcular()

  def _on_level_changed(self):
    self.calcular()
    
  # CÁLCULO DE STATS MÉDIOS
  def calcular(self):
    """Lógica para ler os campos da interface e invocar o calculos.py."""
    name = self.ui.cbbPersonagem.currentText()
    job = self.ui.cbbClasse.currentText()
    level = self.ui.spbLevel.value()

    if not name or not job:
      QMessageBox.warning(
          self,
          "Campos Incompletos",
          "Por favor, selecione um personagem e uma classe.",
      )
      return

    try:
      char = banco.get_char(self.cur, name)
      clas, is_base = banco.get_class(self.cur, char, job)

      # Exemplo de chamada da sua função de calculo:
      stats = calculos.calc_avg(self.cur, char, clas, is_base, job, level)

      
      keys = ["HP", "ATK", "SKL", "SPD", "LCK", "DEF", "RES"]
      stats_keys_cap = ["chp", "catk", "cskl", "cspd", "clck", "cdef", "cres"]
      stat_labels = [
          (self.ui.lblHpInt, self.ui.lblHpDec),
          (self.ui.lblAtkInt, self.ui.lblAtkDec),
          (self.ui.lblSklInt, self.ui.lblSklDec),
          (self.ui.lblSpdInt, self.ui.lblSpdDec),
          (self.ui.lblLckInt, self.ui.lblLckDec),
          (self.ui.lblDefInt, self.ui.lblDefDec),
          (self.ui.lblResInt, self.ui.lblResDec)
        ]

      for idx, key in enumerate(keys):
        stat_str = f"{stats[idx]:.2f}"
        cap = char[stats_keys_cap[idx]]

        lbl_stat_int, lbl_stat_dec = stat_labels[idx]

        stat = stat_str.split('.')

        if stats[idx] < cap:
          lbl_stat_int.setStyleSheet(f"""
              background-color: rgba(255, 255, 255, 0);
              color: rgb(255, 255, 255);
              """)
          lbl_stat_dec.setStyleSheet(f"""
              background-color: rgba(255, 255, 255, 0);
              color: rgb(255, 255, 255);
              """)
        else:
          lbl_stat_int.setStyleSheet(f"""
              background-color: rgba(255, 255, 255, 0);
              color: rgb(85, 255, 0);
              """)
          lbl_stat_dec.setStyleSheet(f"""
              background-color: rgba(255, 255, 255, 0);
              color: rgb(85, 255, 0);
              """)

        lbl_stat_int.setText(f"{stat[0]}")
        lbl_stat_dec.setText(f".{stat[1]}")



    except Exception as e:
      QMessageBox.critical(
          self, "Erro no Cálculo", f"Ocorreu um erro ao calcular:\n{e}"
      )

  def closeEvent(self, event):
    """Fecha a conexão com o banco SQLite ao fechar o app PySide6."""
    if hasattr(self, "con") and self.con:
      self.con.close()
    event.accept()



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())