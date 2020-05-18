import os

dirs = [
    '~/Library/Developer/Xcode/DerivedData',
'~/Library/Developer/Xcode/Archives',
'~/Library/Developer/Xcode/iOS DeviceSupport',
'~/Library/Developer/CoreSimulator',
'~/Library/Caches/com.apple.dt.Xcode',
'~/Library/Application Support/MobileSync/Backup',
'~/Library/Logs',
'/Library/Logs/DiagnosticReports',
'/Library/Logs',
'/var/log',
'~/Library/Caches',
]

for dir in dirs:
    os.system(f'rm -Rf {dir}/*')
