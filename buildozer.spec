[app]
title = Calculadora Surfaçagem
package.name = calculadora
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.build_tools_version = 34.0.0
android.ndk = 25b
android.archs = armeabi-v7a

# Remover linhas que causam erro:
# android.sdk_path = ...
# android.ndk_path = ...
