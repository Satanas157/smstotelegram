[app]
title = SMSMonitor
package.name = smsmonitor
package.domain = org.pericia.forense
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# REQUISITOS LIMPOS: Apenas o necessário para rodar e enviar via HTTPS
requirements = python3,kivy,pyjnius,requests,openssl,certifi

# PERMISSÕES CRÍTICAS
android.permissions = INTERNET,READ_SMS,RECEIVE_SMS,WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
fullscreen = 0
orientation = portrait

[buildozer]
log_level = 2
