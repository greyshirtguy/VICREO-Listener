require('dotenv').config();
const config = {
  packagerConfig: {
    asar: true,
    osxSign: {
      "hardened-runtime": true,
      "gatekeeper-assess": false,
      "identity": "Developer ID Application: VICREO BV (XS47984U9A)"
    },
    "icon": "./src/img/icon"
  },
  makers: [
    {
      name: "@electron-forge/maker-squirrel",
      config: {
        name: "vicreo_listener",
        setupIcon: "./src/img/icon.ico"
      },
    },
    {
      name: "@electron-forge/maker-zip",
      platforms: ["darwin"],
    },
    {
      name: "@electron-forge/maker-deb",
      config: {},
    },
    {
      name: "@electron-forge/maker-rpm",
      config: {},
    },
  ],
  publishers: [
  {
    name: '@electron-forge/publisher-github',
    config: {
      repository: {
        owner: 'jeffreydavidsz',
        name: 'vicreo-listener'
      },
      draft: true,
      prerelease: false
    }
  }]
};

module.exports = config;
