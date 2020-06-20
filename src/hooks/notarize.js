require('dotenv').config();
const { notarize } = require('electron-notarize');

// Path from here to your build app executable:
const buildOutput = require('path').resolve(
    __dirname,
    '../../',
    'out',
    'VICREO-Listener-darwin-x64',
    'VICREO-Listener.app'
);
console.log("path",buildOutput);

module.exports = function () {
    if (process.platform !== 'darwin') {
        console.log('Not a Mac; skipping notarization');
        return;
    }

    console.log('Notarizing...');

    return notarize({
        appBundleId: 'com.electron.vicreo-listener',
        appPath: buildOutput,
        appleId: process.env.APPLE_ID,
        appleIdPassword: process.env.APPLE_ID_PASSWORD
    }).catch((e) => {
        console.error(e);
        throw e;
    });
}