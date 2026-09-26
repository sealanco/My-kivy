[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code directory where main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1.0

# (list) Application requirements
# Add Python dependencies separated by commas (e.g., python3,kivy,requests)
requirements = python3,kivy

# (str) Supported orientation (landscape, sensorLandscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions required by your application
# android.permissions = INTERNET, READ_EXTERNAL_STORAGE

#
# Android specific settings
#

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (int) Target Android API level
android.api = 33

# (int) Minimum API supported by your APK
android.minapi = 21

# (str) Android NDK architecture to build for (arm64-v8a, armeabi-v7a, x86, x86_64)
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

#
# Buildozer global options
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
