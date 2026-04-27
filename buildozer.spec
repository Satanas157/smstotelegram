[app]
title = SMSMonitor
package.name = smsmonitor
package.domain = org.pericia.forense
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,pyjnius,requests,openssl,certifi

android.permissions = INTERNET,READ_SMS,RECEIVE_SMS,WAKE_LOCK

# Ajustes de estabilidade
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_setup = False

fullscreen = 0
orientation = portrait

[buildozer]
log_level = 2
