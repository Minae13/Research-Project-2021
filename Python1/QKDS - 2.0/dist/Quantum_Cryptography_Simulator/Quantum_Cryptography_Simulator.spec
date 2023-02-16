from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Quantum_Cryptography_Simulator.py'],
             pathex=['C:\\Users\\Min Aeji\\Desktop\\Studies\\Art Studies - Batxi\\TR\\Python1\\QKDS - 2.0'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('Code\quantumcryptographysimulator.kv',
'C:\\Users\\Min Aeji\\Desktop\\Studies\\Art Studies - Batxi\\TR\Python1\\QKDS - 2.0\quantumcryptographysimulator.kv',
'DATA')]
exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Quantum_Cryptography_Simulator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe, Tree('C:\\Users\\Min Aeji\\Desktop\\Studies\\Art Studies - Batxi\\TR\\Python1\\QKDS - 2.0\\'),
               a.binaries,
               a.zipfiles,
               a.datas, 
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Quantum_Cryptography_Simulator')
