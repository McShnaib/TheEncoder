# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all necessary data files
datas = [
    ('requirements.txt', '.'),
]

# Hidden imports needed for the app
hiddenimports = [
    'pandas',
    'openpyxl',
    'xlsxwriter',
    'streamlit',
    'altair',
    'pyarrow',
    'pydeck',
    'gitpython',
    'watchdog',
    'tenacity',
    'toml',
]

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Include all Python files
a.datas += Tree('.', prefix='app', excludes=['__pycache__', '*.pyc', '.git', 'dist', 'build', '*.spec'])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SPSS_Prep_Tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    coerce_archive_mode=True,
    icon=None,
)
