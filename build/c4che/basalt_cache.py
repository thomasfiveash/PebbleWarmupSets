AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'basalt'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'basalt'
BUNDLE_NAME = 'PebbleWarmupSets.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['basalt']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'barWeight': 2000, u'unitSystem': 1000, u'cleanFour': 25000, u'deadThree': 13000, u'cleanTwo': 23000, u'benchOne': 7000, u'rowThree': 20000, u'pressOne': 14000, u'squatTwo': 4000, u'cleanOne': 22000, u'deadOne': 11000, u'benchTwo': 8000, u'squatFour': 6000, u'cleanThree': 24000, u'rowTwo': 19000, u'rowFour': 21000, u'deadTwo': 12000, u'pressFour': 17000, u'benchFour': 10000, u'squatThree': 5000, u'pressTwo': 15000, u'rowOne': 18000, u'squatOne': 3000, u'pressThree': 16000, u'benchThree': 9000}
MESSAGE_KEYS_DEFINITION = '/Users/thomasfiveash/Desktop/PebbleWarmupSets/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/thomasfiveash/Desktop/PebbleWarmupSets/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/thomasfiveash/Desktop/PebbleWarmupSets/build/js/message_keys.json'
PEBBLE_SDK_COMMON = '/Users/thomasfiveash/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/thomasfiveash/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/basalt'
PEBBLE_SDK_ROOT = '/Users/thomasfiveash/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['basalt', 'color', 'rect'], 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'basalt', 'BUNDLE_BIN_DIR': 'basalt', 'BUILD_DIR': 'basalt', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH']}
PLATFORM_NAME = 'basalt'
PREFIX = '/usr/local'
PROJECT_INFO = {u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'652a77c0-44a0-4eeb-846b-3bb95008a646', u'appKeys': {u'barWeight': 2000, u'unitSystem': 1000, u'cleanFour': 25000, u'deadThree': 13000, u'cleanTwo': 23000, u'benchOne': 7000, u'rowThree': 20000, u'pressOne': 14000, u'squatTwo': 4000, u'cleanOne': 22000, u'deadOne': 11000, u'benchTwo': 8000, u'squatFour': 6000, u'cleanThree': 24000, u'rowTwo': 19000, u'rowFour': 21000, u'deadTwo': 12000, u'pressFour': 17000, u'benchFour': 10000, u'squatThree': 5000, u'pressTwo': 15000, u'rowOne': 18000, u'squatOne': 3000, u'pressThree': 16000, u'benchThree': 9000}, u'companyName': u'thomasfiveash', u'enableMultiJS': True, u'targetPlatforms': [u'aplite', u'basalt', u'chalk'], u'capabilities': [u'configurable'], u'versionLabel': u'2.0', u'longName': u'Warmup Sets', 'messageKeys': {u'barWeight': 2000, u'unitSystem': 1000, u'cleanFour': 25000, u'deadThree': 13000, u'cleanTwo': 23000, u'benchOne': 7000, u'rowThree': 20000, u'pressOne': 14000, u'squatTwo': 4000, u'cleanOne': 22000, u'deadOne': 11000, u'benchTwo': 8000, u'squatFour': 6000, u'cleanThree': 24000, u'rowTwo': 19000, u'rowFour': 21000, u'deadTwo': 12000, u'pressFour': 17000, u'benchFour': 10000, u'squatThree': 5000, u'pressTwo': 15000, u'rowOne': 18000, u'squatOne': 3000, u'pressThree': 16000, u'benchThree': 9000}, u'shortName': u'Warmup Sets', u'watchapp': {u'watchface': False}, u'resources': {u'media': [{u'targetPlatforms': None, u'type': u'bitmap', u'name': u'play_reset_button', u'file': u'images/play_reset_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'reset_button', u'file': u'images/reset_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'pause_button', u'file': u'images/pause_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'15_minus_button', u'file': u'images/15_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'15_plus_button', u'file': u'images/15_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'25_minus_button', u'file': u'images/25_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'25_plus_button', u'file': u'images/25_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'5_minus_button', u'file': u'images/5_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'5_plus_button', u'file': u'images/5_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'minus_button', u'file': u'images/minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'plus_button', u'file': u'images/plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'check_mark_button', u'file': u'images/check_mark_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'up_arrow_button', u'file': u'images/up_arrow_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'down_arrow_button', u'file': u'images/down_arrow_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'play_button', u'file': u'images/play_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'arrow_button', u'file': u'images/arrow_button.png'}]}}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk']
RESOURCES_JSON = [{u'targetPlatforms': None, u'type': u'bitmap', u'name': u'play_reset_button', u'file': u'images/play_reset_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'reset_button', u'file': u'images/reset_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'pause_button', u'file': u'images/pause_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'15_minus_button', u'file': u'images/15_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'15_plus_button', u'file': u'images/15_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'25_minus_button', u'file': u'images/25_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'25_plus_button', u'file': u'images/25_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'5_minus_button', u'file': u'images/5_minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'5_plus_button', u'file': u'images/5_plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'minus_button', u'file': u'images/minus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'plus_button', u'file': u'images/plus_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'check_mark_button', u'file': u'images/check_mark_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'up_arrow_button', u'file': u'images/up_arrow_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'down_arrow_button', u'file': u'images/down_arrow_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'play_button', u'file': u'images/play_button.png'}, {u'targetPlatforms': None, u'type': u'bitmap', u'name': u'arrow_button', u'file': u'images/arrow_button.png'}]
RPATH_ST = '-Wl,-rpath,%s'
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 78
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk']
TARGET_PLATFORMS = ['chalk', 'basalt', 'aplite']
TIMESTAMP = 1466371568
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
