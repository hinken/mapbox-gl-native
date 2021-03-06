{
  'targets': [
    {
      'target_name': 'platform-ios',
      'product_name': 'mbgl-platform-ios',
      'type': 'static_library',
      'standalone_static_library': 1,
      'hard_dependency': 1,
      'dependencies': [
        'version',
        'loop',
      ],

      'sources': [
        '../platform/default/default_file_source.cpp',
        '../platform/default/online_file_source.cpp',
        '../platform/default/mbgl/storage/offline.hpp',
        '../platform/default/mbgl/storage/offline.cpp',
        '../platform/default/mbgl/storage/offline_database.hpp',
        '../platform/default/mbgl/storage/offline_database.cpp',
        '../platform/default/mbgl/storage/offline_download.hpp',
        '../platform/default/mbgl/storage/offline_download.cpp',
        '../platform/default/sqlite3.hpp',
        '../platform/default/sqlite3.cpp',
        '../platform/darwin/src/log_nslog.mm',
        '../platform/darwin/src/string_nsstring.mm',
        '../platform/darwin/src/image.mm',
        '../platform/darwin/src/nsthread.mm',
        '../platform/darwin/src/reachability.m',
        '../platform/darwin/src/NSException+MGLAdditions.h',
        '../platform/darwin/src/NSString+MGLAdditions.h',
        '../platform/darwin/src/NSString+MGLAdditions.m',
        '../platform/darwin/src/MGLTypes.m',
        '../platform/darwin/src/MGLStyle.mm',
        '../platform/darwin/src/MGLGeometry_Private.h',
        '../platform/darwin/src/MGLGeometry.mm',
        '../platform/darwin/src/MGLShape.m',
        '../platform/darwin/src/MGLMultiPoint_Private.h',
        '../platform/darwin/src/MGLMultiPoint.mm',
        '../platform/darwin/src/MGLPointAnnotation.m',
        '../platform/darwin/src/MGLPolyline.mm',
        '../platform/darwin/src/MGLPolygon.mm',
        '../platform/darwin/src/MGLMapCamera.mm',
        '../platform/darwin/src/MGLOfflinePack.mm',
        '../platform/darwin/src/MGLOfflinePack_Private.h',
        '../platform/darwin/src/MGLOfflineStorage.mm',
        '../platform/darwin/src/MGLOfflineStorage_Private.h',
        '../platform/darwin/src/MGLOfflineRegion_Private.h',
        '../platform/darwin/src/MGLTilePyramidOfflineRegion.mm',
        '../platform/darwin/src/MGLAccountManager_Private.h',
        '../platform/darwin/src/MGLAccountManager.m',
        '../platform/darwin/src/NSBundle+MGLAdditions.h',
        '../platform/darwin/src/NSBundle+MGLAdditions.m',
        '../platform/darwin/src/NSProcessInfo+MGLAdditions.h',
        '../platform/darwin/src/NSProcessInfo+MGLAdditions.m',
        '../platform/ios/src/MGLMapboxEvents.h',
        '../platform/ios/src/MGLMapboxEvents.m',
        '../platform/ios/src/MGLAPIClient.h',
        '../platform/ios/src/MGLAPIClient.m',
        '../platform/ios/src/MGLLocationManager.h',
        '../platform/ios/src/MGLLocationManager.m',
        '../platform/ios/src/MGLMapView.mm',
        '../platform/ios/src/MGLUserLocation_Private.h',
        '../platform/ios/src/MGLUserLocation.m',
        '../platform/ios/src/MGLUserLocationAnnotationView.h',
        '../platform/ios/src/MGLUserLocationAnnotationView.m',
        '../platform/ios/src/MGLAnnotationImage_Private.h',
        '../platform/ios/src/MGLAnnotationImage.m',
        '../platform/ios/src/MGLCompactCalloutView.h',
        '../platform/ios/src/MGLCompactCalloutView.m',
        '../platform/ios/vendor/SMCalloutView/SMCalloutView.h',
        '../platform/ios/vendor/SMCalloutView/SMCalloutView.m',
        '../platform/ios/vendor/Fabric/FABAttributes.h',
        '../platform/ios/vendor/Fabric/FABKitProtocol.h',
        '../platform/ios/vendor/Fabric/Fabric.h',
        '../platform/ios/vendor/Fabric/Fabric+FABKits.h',
      ],

      'variables': {
        'cflags_cc': [
          '<@(boost_cflags)',
          '<@(sqlite_cflags)',
          '<@(zlib_cflags)',
          '<@(rapidjson_cflags)',
          '<@(variant_cflags)',
        ],
        'ldflags': [
          '<@(sqlite_ldflags)',
          '<@(zlib_ldflags)',
        ],
        'libraries': [
          '<@(sqlite_static_libs)',
          '<@(zlib_static_libs)',
          '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
          '$(SDKROOT)/System/Library/Frameworks/CoreLocation.framework',
          '$(SDKROOT)/System/Library/Frameworks/GLKit.framework',
          '$(SDKROOT)/System/Library/Frameworks/ImageIO.framework',
          '$(SDKROOT)/System/Library/Frameworks/MobileCoreServices.framework',
          '$(SDKROOT)/System/Library/Frameworks/OpenGLES.framework',
          '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
          '$(SDKROOT)/System/Library/Frameworks/Security.framework',
          '$(SDKROOT)/System/Library/Frameworks/SystemConfiguration.framework',
          '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
        ],
      },

      'include_dirs': [
        '../platform/ios/include',
        '../platform/darwin/include',
        '../include',
        '../src',
        '../platform/default',
      ],

      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
        'CLANG_ENABLE_OBJC_ARC': 'YES',
        'CLANG_ENABLE_MODULES': 'YES',
      },

      'link_settings': {
        'libraries': [ '<@(libraries)' ],
        'xcode_settings': {
          'OTHER_LDFLAGS': [ '<@(ldflags)' ],
        },
      },

      'direct_dependent_settings': {
        'include_dirs': [
          '../platform/ios/include',
          '../platform/darwin/include',
          '../include',
        ],
        'mac_bundle_resources': [
          '<!@(find ../platform/ios/resources -type f \! -name "README" \! -name \'.*\')',
          '<!@(find ../platform/default/resources -type f \! -name "README" \! -name \'.der\')',
        ],
      },
    },
  ],
}
