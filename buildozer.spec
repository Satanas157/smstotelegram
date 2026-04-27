[app]
# Informações Básicas
title = SMSMonitor
package.name = smsmonitor
package.domain = org.pericia.forense

# ONDE ESTÁ O CÓDIGO (Muito importante estar como o ponto abaixo)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# REQUISITOS (Apenas o essencial para rede e SMS)
requirements = python3,kivy,pyjnius,requests,openssl,certifi

# PERMISSÕES DE PERÍCIA
android.permissions = INTERNET,READ_SMS,RECEIVE_SMS,WAKE_LOCK

# CONFIGURAÇÕES DE COMPILAÇÃO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_setup = False

# Interface
fullscreen = 0
orientation = portrait

[buildozer]
log_level = 2
