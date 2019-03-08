require('es6-promise/auto');  // polyfill Promise on IE

var PageConfig = require('@jupyterlab/coreutils').PageConfig;
__webpack_public_path__ = PageConfig.getOption('publicUrl');

// This needs to come after __webpack_public_path__ is set.
require('font-awesome/css/font-awesome.min.css');
var app = require('@jupyterlab/application').JupyterLab;


function main() {
    var version = PageConfig.getOption('appVersion') || 'unknown';
    var name = PageConfig.getOption('appName') || 'JupyterLab';
    var namespace = PageConfig.getOption('appNamespace') || 'jupyterlab';
    var devMode = PageConfig.getOption('devMode') || 'false';
    var settingsDir = PageConfig.getOption('settingsDir') || '';
    var assetsDir = PageConfig.getOption('assetsDir') || '';

    if (version[0] === 'v') {
        version = version.slice(1);
    }

    // Get the disabled extensions.
    var disabled = [];
    try {
        var option = PageConfig.getOption('disabledExtensions');
        disabled = JSON.parse(option);
    } catch (e) {
        // No-op
    }

    // Handle the registered mime extensions.
    var mimeExtensions = [];
    try {
        if (disabled.indexOf('@jupyterlab/pdf-extension') === -1) {
            mimeExtensions.push(require('@jupyterlab/pdf-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/vega2-extension') === -1) {
            mimeExtensions.push(require('@jupyterlab/vega2-extension/'));
        }
    } catch (e) {
        console.error(e);
    }

    lab = new app({
        namespace: namespace,
        name: name,
        version: version,
        devMode: devMode.toLowerCase() === 'true',
        settingsDir: settingsDir,
        assetsDir: assetsDir,
        mimeExtensions: mimeExtensions
    });

    // Handled the registered standard extensions.
    try {
        if (disabled.indexOf('@jupyterlab/application-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/application-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/apputils-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/apputils-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/codemirror-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/codemirror-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/completer-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/completer-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/console-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/console-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/csvviewer-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/csvviewer-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/docmanager-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/docmanager-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/faq-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/faq-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/filebrowser-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/filebrowser-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/fileeditor-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/fileeditor-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/help-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/help-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/imageviewer-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/imageviewer-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/inspector-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/inspector-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/launcher-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/launcher-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/markdownviewer-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/markdownviewer-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/notebook-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/notebook-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/running-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/running-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/settingeditor-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/settingeditor-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/shortcuts-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/shortcuts-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/tabmanager-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/tabmanager-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/terminal-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/terminal-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/theme-dark-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/theme-dark-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/theme-light-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/theme-light-extension/'));
        }
    } catch (e) {
        console.error(e);
    }
    try {
        if (disabled.indexOf('@jupyterlab/tooltip-extension') === -1) {
            lab.registerPluginModule(require('@jupyterlab/tooltip-extension/'));
        }
    } catch (e) {
        console.error(e);
    }

    // Handle the ignored plugins.
    var ignorePlugins = [];
    try {
        var option = PageConfig.getOption('ignorePlugins');
        ignorePlugins = JSON.parse(option);
    } catch (e) {
        // No-op
    }
    lab.start({ "ignorePlugins": ignorePlugins });

    // Handle a selenium test.
    var seleniumTest = PageConfig.getOption('seleniumTest');
    if (seleniumTest.toLowerCase() === 'true') {
        var caught_errors = []
        window.onerror = function(msg, url, line, col, error) {
           caught_errors.push(String(error));
        };
        lab.restored.then(function() {
            var el = document.createElement('div');
            el.id = 'seleniumResult';
            el.textContent = JSON.stringify(caught_errors);
            document.body.appendChild(el);
        });
    }

}

window.onload = main;
