# -*- mode: python -*-

block_cipher = None


a = Analysis(['VICREO_Listener_Windows.py'],
						 pathex=['D:\\VICREO-Listener'],
						 binaries=[],
						 datas=[],
						 hiddenimports=['pynput','plyer.platforms.win.notification','infi.systray','pkg_resources'],
						 hookspath=[],
						 runtime_hooks=[],
						 excludes=[],
						 win_no_prefer_redirects=False,
						 win_private_assemblies=False,
						 cipher=block_cipher,
						 noarchive=False)
a.datas += [('icon.ico','D:\\VICREO-Listener\\icon.ico','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
						 cipher=block_cipher)
exe = EXE(pyz,
					a.scripts,
					a.binaries,
					a.zipfiles,
					a.datas,
					[],
					name='VICREO_Listener_Windows',
					debug=False,
					bootloader_ignore_signals=False,
					strip=False,
					upx=True,
					runtime_tmpdir=None,
					console=False , icon='icon.ico')
