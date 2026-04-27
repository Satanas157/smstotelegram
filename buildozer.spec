[app]

# (str) Title of your application
title = SMStoTelegram
# (str) Package name
package.name = smstotelegram
# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
# AJUSTE: Adicionado requests, openssl e certifi para garantir conexão segura
requirements = python3,kivy,pyjnius,requests,openssl,certifi

# (list) Permissions
android.permissions = INTERNET,READ_SMS,RECEIVE_SMS,WAKE_LOCK

# (int) Target Android API, should be as high as possible.
android.api = 33
# (int) Minimum API your APK will support.
android.minapi = 21
# (str) Android NDK version to use
android.ndk = 25b
# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0
# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

[buildozer]
