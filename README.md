# QGIS Minimalist Plugin Skeleton

In various QGIS plugin tutorials you are told to use _Plugin Builder_ tool to create a skeleton for your plugin.
It is surely helpful as it helps you kickstart your plugin with stuff like UI designer file, auto tests, docs, i18n, scripts and so on.

This QGIS plugin is the complete opposite of a plugin built with _Plugin Builder_: it is a plugin skeleton cut down
to the bare minimum that still results in a valid QGIS plugin. It consists of two files only: a text file with metadata and a Python file with a bit of code.

## Why?

For educational purposes, it is useful to understand how a very basic plugin could look like.

For practical reasons, it is sometimes useful to create a single purpose plugin with the least amount of extra bells and whistles,
so the code that actually does something is not hidden among generated boilerplate code.

## How to use it?

1. Copy this folder (but not .git) into a new plugin folder e.g ```~/.qgis2/python/plugins/minimal```
2. Change the name and details in metadata.txt
3. Start QGIS and enable the plugin (search for the name you gave it) (menu Plugins > Manager and Install Plugins...)

Now you should see a "Go!" button in your "Plugins" toolbar (make sure it is enabled in menu Settings > Toolbars > Plugins).

4. Add code to __init__.py

Have fun!


### Loading resources

```
import resources
icon = resources.icon("myicon.svg")
```
