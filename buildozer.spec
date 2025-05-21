[app]
# (list) Application title
title = MyApp

# (string) Package name
package.name = myapp

# (string) Package version
package.version = 1.0

# (string) Package identifier
package.domain = org.myapp

# (list) Application requirements
# comma separated e.g. python3,kivy
# For a basic Kivy app:
# requirements = python3,kivy
requirements = python3,kivy,requests

# (list) Application source files
source.include_exts = py,png,jpg,kv,atlas

# (string) Custom source folders (e.g. 'src')
# source.include_dirs =

# (bool) Copy the library to the APK
# copy_libs = True

# (bool) Enable android (default is True)
android = True

# (string) Android NDK version (you may want to upgrade it)
android.ndk = 21b

# (string) Android SDK version
android.sdk = 20

# (string) Android API version
android.api = 29

# (bool) Enable debugging
debug = 1

