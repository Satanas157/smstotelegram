[app]

title = Standard
package.name = smstotelegram
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,pyjnius

android.permissions = INTERNET,READ_SMS,RECEIVE_SMS

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

fullscreen = 0
orientation = portrait

[buildozer]
log_level = 2
